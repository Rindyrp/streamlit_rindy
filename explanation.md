The data points on the graph are generated from a multivariate normal distribution with a population mean $\mu = 0$ and population $\rho$ that is set by the slider above (initial value of 0).

As we are drawing a **sample** based on the above population parameters. The sample statistics $\bar{x}$ and $r$ will likely be different to the population parameters. 

Play around with the the slider to see how two variables vary at different levels of correlation. Also, have a look at the impact of changing the number of data points and the p-value for the test of correlation significance.

### Key Formulas

**Correlation Coefficient:**

$$\text{Cor}(X,Y) = \frac{\text{Cov(X,Y)}}{\text{SD}(X)\text{SD}(Y)}$$

**Pearson's-r test of significance - test statistic:**

$$t = \frac{r\sqrt{n-2}}{\sqrt{1-r^2}}$$

**OLS estimate $\hat{\beta}_1$:**

$$\hat{\beta}_1 = \frac{\sum (X_i-\bar{X})(Y_i-\bar{Y})}{\sum (X_i-\bar{X})^2}$$
