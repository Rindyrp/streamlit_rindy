import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy.stats import pearsonr
from pathlib import Path

@st.cache
def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

explanation_md = read_markdown_file('explanation.md')


# Title
st.title('Exploring Correlations')


# Dropdown
num_points = st.selectbox(label='Number of points', options=[10,50,100,1000])

# Slider
rho = st.slider('Population Rho', min_value=-1.0, max_value=1.0, value=0.0, step=0.1)

# Generate data 

cov_mat = np.array([[1,rho],
                    [rho,1]])
mean = np.array([0.0,0.0])
m = np.random.multivariate_normal(mean=mean,cov=cov_mat,size=num_points).T

sample_rho = np.corrcoef(m)[0,1]

# Line of best fit
beta_1 = ((m[0,:]-m[0,:].mean())*(m[1,:]-m[1,:].mean())).sum()/(((m[0,:]-m[0,:].mean())**2).sum())
beta_0 = m[1,:].mean() - beta_1*(m[0,:].mean())

ols_eq = beta_0 + beta_1*np.arange(-5,6,1)

### CREATE PLOTLY GRAPH

fig = go.Figure()

fig.add_trace(
        go.Scatter(
                x= m[0,:],
                y= m[1,:],
                mode='markers',
                visible=True,
                name=f'sample rho = {np.around(sample_rho,3)}, p_value={np.around(pearsonr(m[0,:],m[1,:])[1],4)}'
                ),  
    
             )

fig.add_trace(
        go.Scatter(
                x=np.arange(-5,6,1), 
                y=ols_eq, 
                visible=True,
                mode='lines',
                line=dict(
                        color="Red",
                        width=2
                        ),                       
                name=f'OLS B1 = {beta_1.round(2)}'
                )
            )

# Add axis dashed line
fig.add_shape(type="line",
            x0=-5, y0=0, x1=5, y1=0,
            line=dict(
                color="Black",
                width=3,
                dash="dash",
                )
            )

fig.add_shape(type="line",
            x0=0, y0=-5, x1=0, y1=5,
            line=dict(
                color="Black",
                width=3,
                dash="dash",
                )
            )            

# Update chart layouts

# Force axis to remain same 
fig.update_layout(yaxis=dict(range=[-5,5]))
fig.update_layout(xaxis=dict(range=[-5,5]))

# Update height

fig.update_layout(height=600, width=700,
                margin=dict(
                        l=0,
                        r=0,
                        b=50,
                        t=50,
                        pad=5
                            )
                 )
                

# Adjust some legend attributes
fig.update_layout(
    legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
            )
)

    
# plot with streamlit
st.plotly_chart(fig, use_container_width=False)


# Explanations
st.subheader('How does it work?')
st.markdown(explanation_md)