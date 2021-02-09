import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import datetime
import os
from ta.trend import SMAIndicator

#Make a Dataset

def RSI(df):
    def computeRSI (data, time_window):
        diff = data.diff(1).dropna()        
        up_chg = 0 * diff
        down_chg = 0 * diff
        up_chg[diff > 0] = diff[ diff>0 ]
        down_chg[diff < 0] = diff[ diff < 0 ]
        up_chg_avg   = up_chg.ewm(com=time_window-1 , min_periods=time_window).mean()
        down_chg_avg = down_chg.ewm(com=time_window-1 , min_periods=time_window).mean()
        rs = abs(up_chg_avg/down_chg_avg)
        rsi = 100 - 100/(1+rs)
        return rsi
    df['RSI-1'] = computeRSI(df['Close'],1)
    df['RSI-2'] = computeRSI(df['Close'],2)
    df['RSI-3'] = computeRSI(df['Close'],3)
    df['RSI-4'] = computeRSI(df['Close'],4)
    df['RSI-5'] = computeRSI(df['Close'],5)
    df['RSI-6'] = computeRSI(df['Close'],6)
    df['RSI-7'] = computeRSI(df['Close'],7)
    df['RSI-8'] = computeRSI(df['Close'],8)
    df['RSI-9'] = computeRSI(df['Close'],9)
    df['RSI-10'] = computeRSI(df['Close'],10)
    df['RSI-11'] = computeRSI(df['Close'],11)
    df['RSI-12'] = computeRSI(df['Close'],12)
    df['RSI-13'] = computeRSI(df['Close'],13)
    df['RSI-14'] = computeRSI(df['Close'],14)
    df['RSI-15'] = computeRSI(df['Close'],15)
    df['RSI-16'] = computeRSI(df['Close'],16)
    df['RSI-17'] = computeRSI(df['Close'],17)
    df['RSI-18'] = computeRSI(df['Close'],18)
    df['RSI-19'] = computeRSI(df['Close'],19)
    df['RSI-20'] = computeRSI(df['Close'],20)
    
    return df

def SMA(df,n):
    sma = SMAIndicator(df['Close'],n)
    df['SMA-'+str(n)] = sma.sma_indicator()
    return df

#train
start = datetime.datetime(1997,1,1)
end = datetime.datetime(2006,12,31)
#test
st = datetime.datetime(2007,1,1)
ed = datetime.datetime(2017,12,31)

Dow30 = ['MMM','AXP','AAPL','BA','CAT','CVX','CSCO','KO','DIS','DD','XOM','GE','GS','HD','IBM','INTC','JNJ','JPM','MCD',
                 'MRK','MSFT','NKE','PFE','PG','TRV','UNH','VZ','WMT']

for stock in Dow30:
    df = web.DataReader(stock,'yahoo',start,end)
    df = RSI(df)
    df = SMA(df,50)
    df = SMA(df,200)

    # directory = stock
    # parent_dir = "/finance/buysellsignalpaper/python/Dataset/"
    # path = os.path.join(parent_dir, directory) 
    # os.mkdir(path) 

    df.to_csv('Dataset/train/'+str(stock)+'19972006.csv')

# for stock in Dow30:
#     df = web.DataReader(stock,'yahoo',st,ed)
#     df = RSI(df)
#     df = SMA(df,50)
#     df = SMA(df,200)

#     # directory = stock
#     # parent_dir = "/finance/buysellsignalpaper/python/Dataset/"
#     # path = os.path.join(parent_dir, directory) 
#     # os.mkdir(path) 

#     df.to_csv('Dataset/test/'+str(stock)+'20072017.csv')
  


  