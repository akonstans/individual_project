import pandas as pd
import new_lib as nl
import wrangle as w
import acquire as a
from matplotlib import pyplot as plt
import seaborn as sns
from datetime import datetime
import statsmodels.api as sm
from statsmodels.tsa.api import Holt, ExponentialSmoothing
from sklearn.metrics import mean_squared_error
from math import sqrt
import warnings
warnings.filterwarnings("ignore")
from statsmodels.tsa.arima.model import ARIMA
from datetime import datetime, timedelta


def first_look(train, val, test, stock):
    plt.figure(figsize=(12,6))
    plt.plot(train.c, color='#2E2EFE', label = 'Train')
    plt.plot(val.c, color='#33EBDC', label = 'Validate')
    plt.plot(test.c, color='#B051DE', label = 'Test')
    plt.legend()
    plt.ylabel('Stock Price')
    plt.title(f'{stock} Stock Price')
    plt.show()

def evaluate(target, preds, val):
    '''
    Fast way to find RMSE for models
    '''
    rmse = round(sqrt(mean_squared_error(val[target], preds[target])), 0)
    return rmse
# Function to evaluate rmse of a model


def plot_and_eval(target, preds, train, val, stock):
    '''
This function will plot and evaluate a model using target predicitons from a dataset and return a graph of the data
It will also calculate the rmse of the data and report that along with the data
    '''
    plt.figure(figsize = (14,6))
    plt.plot(train[target], label='Train', linewidth=1, color='#2E2EFE')
    plt.plot(val[target], label='Validate', linewidth=1, color='#33EBDC')
    plt.plot(preds[target], label='predictions', linewidth=2, color='#EF080C')
    plt.legend()
    plt.title(f'{stock} Stock Price')
    rmse = evaluate(target, preds.iloc[29:], val.iloc[29:])
    print(stock , '-- RMSE: {:.0f}'.format(rmse))
    plt.show()
# Plot the model and state Rmse

def baseline(train, val, stock):
    base = train.c.mean()
    base = pd.DataFrame(base, columns = {'c'}, index = val.index)
    plot_and_eval('c', base, train, val, stock)
    # creating baselines

startDate = datetime(2022, 9, 19)
endDate = datetime(2024, 2, 11)
ari_dates = pd.date_range(startDate,endDate-timedelta(days=1),freq='d')
ari_dates = ari_dates[ari_dates.dayofweek < 5]

def arima(df, train, val, test, stock):
    train_size = int(round(df.shape[0] * 0.8))
    ar_train = df[:train_size]
    ar_test = df[train_size:]
    arima = ARIMA(ar_train.c, order = (30,2,5))
    fit = arima.fit()
    ar_preds = fit.forecast(ar_test.shape[0] + 265)
    ar_df = pd.DataFrame({'c': ar_preds, 'dates': ari_dates})
    ar_df = ar_df.set_index('dates')
    plt.figure(figsize = (14,6))
    plt.plot(train['c'], label='Train', linewidth=1, color='#2E2EFE')
    plt.plot(val['c'], label='Validate', linewidth=1, color='#33EBDC')
    plt.plot(test['c'], label='Test', linewidth=2, color='#EF080C')
    plt.plot(ar_df['c'], label = 'ARIMA predictions', linewidth = 2, color='#30DF19')
    plt.legend()
    plt.title(f'{stock} Stock Price')
    plt.show()

def seasonal_decomp(train):
    sm.tsa.seasonal_decompose(train['c'], period = 30).plot()
    None