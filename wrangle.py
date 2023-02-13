import acquire as a
import datetime as dt
import pandas as pd
import new_lib as nl
def wrangle_data(ticker, url = None):
    df =  a.get_data(ticker, url)
    df = a.get_dates(df)
    df = a.prep_data(df)
    return df

def split_data(df):
    train_size = int(round(df.shape[0] * 0.5))
    val_size = int(round(df.shape[0] * 0.3))
    val_index = train_size + val_size
    train = df[:train_size]
    val = df[train_size : val_index]
    test = df[val_index :]
    return train, val, test