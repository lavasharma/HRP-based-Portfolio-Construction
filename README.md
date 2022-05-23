# HRP-based-Portfolio-Construction
Asset Allocation and Portfolio Construction based on Hierarchical Risk Parity (Clustering) Approach  


# ABSTRACT
In this study, we explore the concepts of Hierarchical Risk Parity (HRP). We begin by understanding the constraints and limitations of the methodology for finding a well-diversified portfolio using the concepts of Critical Line Algorithm (CLA), well-known as Efficient Frontier from Markowitz’ Modern Portfolio Theory and the Inverse Variance Portfolio Algorithm. We explore how HRP applies modern mathematics (graph theory and machine learning techniques) to build a diversified portfolio based on the information contained in the covariance matrix. This approach addresses the hierarchy shortfall in the operations involving covariance matrix of the Critical Line Algorithm. We understand the intuitive nature of the algorithm using an application on the S&P500 Index. We compare the performance of portfolios obtained by the HRP, CLA and IVP algorithms.


# Mean Variance Optimization / Critical Line Algorithm
After tackling the problem of security selection, the challenge for an asset manager is to construct a portfolio of these securities. Portfolio selection is one of the most evergreen problem in finance and with the invention of new securities and products, the field has been evolving. Portfolio construction is the process of understanding how different asset classes, funds and weightings impact each other, their performance & risk and how decisions ladder up to an investor's objectives. Harry Markowitz attempted to answer these questions more than 6 decades ago in his paper on “Portfolio Selection”. He was a pioneer in this field and gave us the “Critical Line Algorithm”, a quadratic optimization procedure specifically designed for linear inequality-constrained portfolio optimization problems. The algorithm guarantees that the exact solution is found after a known number of iterations, and that it ingeniously circumvents the Karush-Kuhn-Tucker conditions. In mathematical optimization, the Karush-Kuhn-Tucker (KKT) conditions, are first derivative tests (sometimes called first-order necessary conditions) for a solution in nonlinear programming to be optimal, provided that some regularity conditions are satisfied.

Despite its mathematical and conceptual soundness, the CLA algorithm has its own drawbacks. Quadratic Programming requires matrix inversion and ‘Ill-conditioned’ matrices (with high condition numbers) are prone to large errors while inverting. Therefore, small deviations in forecasted returns cause different (mostly unexplainable) allocations. In financial terms, this is called the Markowitz’s Curse - The more correlated the investments, the greater the need for diversification, and yet the more likely we will receive unstable solutions.


# Hierarchical Clustering Algorithm

Hierarchical clustering, also known as hierarchical cluster analysis, is an algorithm that groups similar objects into groups called clusters. The endpoint is a set of clusters, where each cluster is distinct from each other cluster, and the objects within each cluster are broadly similar to each other. Clustering is basically a technique that groups similar data points such that the points in the same group are more similar to each other than the points in the other groups. In clustering, the distance between two clusters can be computed based on the length of the straight line drawn from one cluster to another also commonly known as Euclidean distance. Many other distance metrics have been developed like MIN, MAX, Group Average, Ward’s Method, Distance Between Centroids. The choice of distance metric should be made based on theoretical concerns from the domain of study. That is, a distance metric needs to define similarity in a way that is sensible for the field of study. For example, if clustering crime sites in a city, city block distance may be appropriate. Or, better yet, the time taken to travel between each location. Where there is no theoretical justification for an alternative, the Euclidean should generally be preferred, as it is usually the appropriate measure of distance in the physical world. 

Marcos Lopez De Parado, in his original work introduced the notion of hierarchy in the correlation matrix. Such a hierarchical notion, doesn’t regard the assets as perfect substitutes for each other, rather restricts the ‘free weighting’ scheme of CLA. For example, JP Morgan and Goldman Sachs will be more closely related than an bank based out of Asia for example SBI. Then from a diversification stand-point, we would want to choose JP Morgan with SBI and overweight Goldman Sachs for a Pairs-Trading Strategy. 


# Methodology
The first step towards implementing various portfolio construction methods is collecting the required data. So, unlike the technique used by the author (HRP paper’s Lopez de Prado) wherein he has simulated synthetic data for correlated stocks, we have used data of DJIA’s and S&P500’s stocks from 2000-2022. DJIA contains 27 stocks whereas S&P500 contains 368 stocks, and this data is used to carry out the complete research.
After collection of data, we calculate the daily returns for in the selected universe (i.e., S&P500 or DJIA). Post that model is trained using HRP, CLA and IVP. All the models are trained on rolling one year’s data (i.e., 252 days) and the portfolio consists of 30 stocks which are randomly selected from the universe. Once the model is trained on returns securities weights, these weights are than used to test the model on consecutive one-month’s test dataset (i.e., 22 days) also called as out-sample dataset. Testing phase returns monthly PnL of the portfolio, standard deviation of daily returns of the portfolio and the Sharpe Ratio of the portfolio. This train and test are done recursively in walk forward kind of backtest from 2000-2022. After completion of one such process, we get around 240 observations, one for each month’s out sample data. This process is repeated for 100 different portfolios which in turn gives us about 24000 datapoints to comment on which portfolio construction method is the best or to compare between the methods.

# HRP Algorithm Process Flowchart

# Numerical Results

The correlation matrix of returns of 𝑁𝑥𝑁 matrix thus obtained is visualized as a heatmap. For example, the following chart shows the correlation diagram of stocks in the Dow Jones index for daily returns in the period from 1/1/2000 to 1/1/2022. Stocks from Dow Jones are selected
for plotting and demonstration purposes. 

![alt text](https://github.com/lavasharma/HRP-based-Portfolio-Construction/blob/main/QuasiDiagonlaization.png)

The dendrogram plot of clusters formed using HRP algorithm is obtained as follows.
![alt text](https://github.com/lavasharma/HRP-based-Portfolio-Construction/blob/main/Dendograms.png)

The above dendrogram plot is quite intuitive by itself. Strongly ‘related’ stocks form a link between themselves. For example, JP Morgan (JPM) and Goldman (GS) (coming from the banking sector with similar businesses and are impacted by same exogenous events) form a turquoise blue link which in turn is related to American Express Company, another financial services company. Another example is the for the stocks in Information Technology industry. Intel (INTC), Microsoft (MSFT), Cisco (CSCO) form a local group (green linkages).

Below charts show time series of Monthly Profit and Loss obtained from HRP (Magenta), CLA (Yellow) and IVP (Turquoise) Portfolios. A dollar invested in CLA’s portfolio in 2000 would grow to 3.074 in 2022, whereas it would have only grown to 2.5334 in IVP. HRP’s growth lies somewhere in between the two portfolios. However, an interesting feature is the degree of variation in the returns generated from these portfolios. CLA’s greater degree in variation with respect to HRP is evident from its lower Sharpe Ratio, contributed by higher Standard Deviation of returns, which turn is result of higher concentration risk.

![alt-text](https://github.com/lavasharma/HRP-based-Portfolio-Construction/blob/main/Over%20Time%20PnL.png)

![alt-text](https://github.com/lavasharma/HRP-based-Portfolio-Construction/blob/main/%241%20Invested.png)

There is a clear difference in weights allocated by CLA, HRP and IVP portfolios on a particular month. We can see the concentration / over-allocation issue clearly present in the weights obtained from CLA. It over allocates to few highest performing asset(s), and in some cases, does not even consider other assets to invest in the universe from. This concentration risk results in higher standard deviation, as a movement in one stock, drags along with it the overall portfolio value. HRP on the other hand gives out a relatively balanced distribution of weights.

![alt-text](https://github.com/lavasharma/HRP-based-Portfolio-Construction/blob/main/Weights%20Allocations.png)

# Simulations with S&P 500

Results explained above are depicting portfolio of 27 stocks (present in DJIA from 2000-2022) for a particular time. In order to validate the idea (i.e., The portfolio formed by using HRP (Hierarchical Risk Parity Approach) performs better in delivering risk adjusted returns (good Sharpe Ratio) compared to the traditional Efficient Frontier from Markowitz’ Modern Portfolio Theory (also known as CLA) and other risk parity approach IVP (Inverse Variance Portfolio)) in more robust way, we repeated the process of building portfolio using all the three methods several times (around 24000) as mentioned in the methodology section.

![alt-text](https://github.com/lavasharma/HRP-based-Portfolio-Construction/blob/main/S%26P500%20Sims.png)

Table above would be summarizing the results of Avg. monthly PnL, Avg. daily standard deviation of daily PnL, Avg. Sharpe Ratio for the portfolios created by HRP, CLA, IVP.
As we can see that after creating 24000 portfolios and taking the avg of those results, Avg. Sharpe Ratio of portfolios formed by HRP is the highest, followed by IVP and CLA underperforms on the out-sample data by around 30%.


