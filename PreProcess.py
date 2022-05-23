import yfinance as yf
import pandas as pd


###### Collecting daily price data for tickers from yahoo finance
def CollectData(tickerlist,filename):

    '''
    Add_read = "C:/Users/Shubham/Desktop/Code/Data/DowJones_Names.csv"
    df_tickers =  pd.read_csv(Add_read)
    tickerlist = df_tickers["Symbol"].tolist()

    tickerlist.remove("DOW")
    tickerlist.remove("V")
    tickerlist.remove("CRM")
    print((tickerlist))
    '''

    df_all = pd.DataFrame()
    for ticker in tickerlist:
        #print(ticker)
        df = yf.download(ticker, start='2000-01-01',end ='2022-12-31',progress=False)
        df.rename(columns = {"Adj Close": "{}".format(ticker)}, inplace = True)
        df = df[["{}".format(ticker)]]
        df_all = pd.concat([df_all,df],axis = 1)

    df_all.to_csv("{}.csv".format(filename))


def ProcessData():
    File_Address = "DowJones.csv"
    df_PriceData = pd.read_csv(File_Address)
    
    df_PriceData["Date"] = pd.to_datetime(df_PriceData["Date"], format = "%d-%m-%y")
    df_PriceData = df_PriceData.set_index("Date")

    df_PctChange = df_PriceData.pct_change()
    df_PctChange.dropna(inplace=True)
    
    return df_PctChange, df_PriceData


# df_train_price, df_train, df_test, start = PP.PrepTrainTestData(df_Complete, df_Price, start, ntrainSet, ntestSet)
def PrepTrainTestData(df_Complete, df_Price, start, ntrainSet, ntestSet):
    
    df_train = df_Complete.iloc[start : (start + ntrainSet), :]
    df_train_price = df_Price.iloc[start : (start + ntrainSet), :]
    
    df_test = df_Complete.iloc[(start + ntrainSet) : (start + ntrainSet + ntestSet), :]
    start = start + ntestSet
    
    return df_train_price, df_train, df_test, start


if(__name__ == '__main__'):
    
    
     #### Symbols of tickers that are present in DOW JONES IND AVG from 2000 - 2022
    tickerlist = ['MMM', 'AXP', 'AMGN', 'AAPL', 'BA', 'CAT', 'CVX', 'CSCO', 'KO', 'GS', 'HD',\
                    'HON', 'IBM', 'INTC', 'JNJ', 'JPM', 'MCD', 'MRK', 'MSFT', 'NKE', 'PG', 'TRV',\
                    'UNH', 'VZ', 'WMT', 'WBA', 'DIS']  
    
    filename = "DOWJONES"
    CollectData(tickerlist, filename)
    
