import requests
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime, timedelta
import os


def get_data(ticker, url = None):

    if os.path.isfile(f'{ticker}.csv'):
        
        return pd.read_csv(f'{ticker}.csv', index_col= [0])
    else:
        r = requests.get(url).json()
        r = pd.DataFrame(r['results'])
        r.to_csv(f'{ticker}.csv')
    return r


def get_dates(df):
    startDate = datetime(2021, 2, 16)
    endDate = datetime(2023, 2, 10)
    dates = pd.date_range(startDate,endDate-timedelta(days=1),freq='d')
    dates = dates[dates.dayofweek < 5]
    dates = dates.drop(['2021-04-02', '2021-05-31', '2021-07-05', '2021-09-06', '2021-11-25', '2021-12-24', '2022-01-17', 
            '2022-02-21', '2022-04-15', '2022-05-30', '2022-07-04', '2022-09-05', '2022-11-24', '2022-12-26', 
            '2023-01-02', '2023-01-16'])
    df['Date'] = dates
    df = df.set_index('Date')
    return df

def prep_data(df):
    df = df.drop(columns = ['v', 'vw', 't', 'n'])
    return df


