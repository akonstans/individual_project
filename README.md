# Individual Project

# Project Overview
This project is intended to be a time series analysis of 4 tech stocks(Apple, Google, Netflix, and Amazon) to create a predictive model to determine future stock prices. The end result is hopefully a model capable of predicting 4 stocks at once and be used to determine portential market trends. The first iteration of the model will be using just 1 stock at a time to predict future price.

# Project Goals
- To predict stock price with accuracy higher than a baseline given two years of prior data
- Create a model using 1 stock to determine future prices
- Create a model using all 4 stocks to determine future trends
- To use all 4 stocks in a time series at once and be able to use the predicitions to infer market trends in the tech industry
- Deliver a report on the project

# Data Being Used
The data used in this project was acquired from polygon.io using their API to gather data on the stocks for dates 02-16-21 through 02-12-23
- Link to polygon's API https://polygon.io/docs/stocks/get_v2_aggs_ticker__stocksticker__range__multiplier___timespan___from___to


# First Thoughts
I beleieve there will be a correlation between all the stocks as they are the biggest stocks in the tech market.
The pandemic will likely have affected price

# Process
- First I acquired the data and added a datetime index to facilitate the use of time series analysis models
- I then created a baseline, seasonal decomposition, moving average, Holt model, Holt Winters model, and ARIMA models
- After examining the models I determined that the ARIMA was the best model to use due to examining other works and concept behind it
- While running through models I tuned the orders for the ARIMA models to 30, 2, 5 respectivley and found that to be the best set of orders

# Final Thoughts
I think a more refined understanding of time series and ARIMA in particular is needed to create a more accurate and usable model
The biggest limitation is the scope of the data though. Two years simply is not enough to identify long term industry or individual trends
The predictions are also made without any knowledge of events yet to occur that could also drastically alter the prices
