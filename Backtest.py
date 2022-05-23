import pandas as pd
import numpy as np
import HRP
import PreProcess as PP

from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt.expected_returns import mean_historical_return
from pypfopt.risk_models import CovarianceShrinkage

import warnings
warnings.filterwarnings("ignore")


def Pnl_funct(Weights, df_test):
    
    df_test = df_test[Weights.index.tolist()]
    df_EqCurve = pd.DataFrame(np.dot(df_test,np.array(Weights)), index = df_test.index, columns = ["DailyPortfolio_Pnl"])
    
    return round(float(np.sum(df_EqCurve)), 4), round(float(np.std(df_EqCurve)), 4)
    
def Backtest():
    
    df_result = pd.DataFrame()
    ntrainSet = 252
    ntestSet = 22
    
    #1) Generate correlated data
    #Data
    df_Complete, df_Price = PP.ProcessData()
    
    

    
    start = 0
    end = len(df_Complete) - ntestSet
    
    while ((start +ntrainSet) <= end):
        
        df_train_price, df_train, df_test, start = PP.PrepTrainTestData(df_Complete, df_Price, start, ntrainSet, ntestSet)
        
        ##Train Model
        Weights = HRP.HRP_weights(df_train)
        Weights_IVP = HRP.IVP_weights(df_train)
        Weights_CLA = CLA_weights(df_train_price)
        
        
        ##Test Model (OutSample)
        Pnl,Pnl_std = Pnl_funct(Weights, df_test)
        Pnl_IVP,Pnl_std_IVP = Pnl_funct(Weights_IVP, df_test)
        
        ###Call Pnl_funct for CLA 
        Pnl_CLA,Pnl_std_CLA = Pnl_funct(Weights_CLA, df_test)
        
        
        #df_result.loc[df_test.index.tolist()[0],["MonthlyPnl", "DailyStd_Pnl", "MonthlyPnl_IVP", "DailyStd_Pnl_IVP"]] = Pnl, Pnl_std, Pnl_IVP,Pnl_std_IVP 
        
        df_result.loc[df_test.index.tolist()[0],["MonthlyPnl_HRP", "DailyStd_Pnl_HRP",\
         "MonthlyPnl_CLA","DailyStd_Pnl_CLA","MonthlyPnl_IVP", "DailyStd_Pnl_IVP"]] = Pnl, Pnl_std, Pnl_CLA,Pnl_std_CLA,Pnl_IVP,Pnl_std_IVP 
    
    return df_result
    
def CLA_weights(df):
    
    #mu = (1 + df.mean())**365 -1
    # mu = df.mean()
    # S = df.cov()
    
    mu = mean_historical_return(df)
    S = CovarianceShrinkage(df).ledoit_wolf()
    
    
    ef = EfficientFrontier(mu, S)
    weights = ef.max_sharpe()
    
    df = pd.DataFrame.from_dict(dict(weights), orient = "index")
    
    return df[0]
    


    
if __name__=='__main__':
    
    #CLA_weights()
    df_result = Backtest()
    df_result.to_csv("df_result_HRP_daily_CLA.csv")
    #print(df_result)