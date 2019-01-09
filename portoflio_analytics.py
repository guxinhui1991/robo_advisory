from pandas.tseries.offsets import BDay
import datetime as dt
import pandas as pd
import numpy as np
import xlwt
import xlrd
#from lxml import html,etree,objectify
#from urllib2 import urlopen
#import urllib2
import urllib.request
import csv
import imp
#import win32com
import codecs
import base64
from scipy.stats import norm
import math
import numpy.random as nrand
import scipy

##
def var_cov_var(P, c, mu, sigma):
    """
    Variance-Covariance calculation of daily Value-at-Risk
    using confidence level c, with mean of returns mu
    and standard deviation of returns sigma, on a portfolio
    of value P.
    P: Asset Value of Portfolio           eg: 1,000,000 USD
    c: Confidence Level                   eg: 99 precent confidence
    mu: mean
    signa: std dev
    """
    alpha = norm.ppf(1-c, mu, sigma)
    return P - P*(alpha + 1)

##  return the CVAR (expected shortfall of the return series)
def cvar(returns, alpha):
    """
    returns: a series of return
    alpha: the level of significance
    """
    # This method calculates the condition VaR of the returns
    sorted_returns = np.sort(returns)
    # Calculate the index associated with alpha
    index = int(alpha * len(sorted_returns))
    # Calculate the total VaR beyond alpha
    sum_var = sorted_returns[0]
    for i in range(1, index):
        sum_var += sorted_returns[i]
    # Return the average VaR
    # CVaR should be positive
    return abs(sum_var / index)


# InputFile = 'C:\\Users\\Ku Yeuh Dau GuoYutao\\Desktop\\Hedga\\portoflio analytics\\PortfolioInput_short.xls'
InputFile = 'C:\\Users\\Ku Yeuh Dau GuoYutao\\Desktop\\Hedga\\portoflio analytics\\PortfolioInput.xls'
InputFile = pd.io.excel.read_excel(InputFile,skiprows=0, header =0, na_values=['NA'],sep='\t')

Return_Period = 2
Confidence_Level = 0.99

Current_DF = InputFile[:2]
Current_DF= Current_DF.set_index('Instrument name')
Current_DF_T = Current_DF.transpose()

## Calculate Position Value and Abs Position Value
Current_DF_T['Position Value'] = (Current_DF_T['Position'].astype(float))*(Current_DF_T['Current Price'].astype(float))
Current_DF_T['Abs Position Value'] = (abs(Current_DF_T['Position'].astype(float)))*(Current_DF_T['Current Price'].astype(float))

## Gross_Exposure / Net_Exposure
Gross_Exposure = Current_DF_T['Abs Position Value'].sum()
Net_Exposure = Current_DF_T['Position Value'].sum()

## Weights
Current_DF_T['Weight'] = Current_DF_T['Position'] * Current_DF_T['Current Price']/ Gross_Exposure

## Long or Short
Current_DF_T['L or S'] =''
for i in range(0,len(Current_DF_T)):
    if(Current_DF_T['Position'][i] >0):
        Current_DF_T['L or S'] = 'L'
    else:
        Current_DF_T['L or S'] = 'S'

Current_DF = Current_DF_T.transpose()

History_DF = InputFile[3:]
History_DF.rename(columns={'Instrument name':'Date'}, inplace=True)
History_DF.sort(['Date'], ascending = [False],inplace = True)
History_DF= History_DF.set_index('Date')

## Return Matrix based on Return Period
Return_DF= pd.DataFrame(columns = History_DF.columns)
for i in range(0,(len(History_DF) - Return_Period)):
    Return_DF.loc[i] = 0
    for col in History_DF.columns:
        if Current_DF[col]['L or S'] =='L' :
            Return_DF[col][i] = (History_DF[col][i])/(History_DF[col][i + Return_Period]) - 1
        elif Current_DF[col]['L or S'] =='L' :
            Return_DF[col][i] = (History_DF[col][i]/History_DF[col][i + Return_Period] - 1) *(-1)
        else:
            pass

## Portolio Expected Return
Expected_Return_Series = Return_DF.mean(axis =0)
Expected_Return_DF_T = pd.DataFrame(Expected_Return_Series, columns=['Expected Return'])
Expected_Return_DF_T.reindex(Current_DF_T.index)
Expected_Return_DF_T =pd.concat([Expected_Return_DF_T,Current_DF_T], axis =1)
Expected_Return_DF_T['Weighted Expected Return'] = Expected_Return_DF_T['Expected Return'] * Expected_Return_DF_T['Weight']
Portfolio_Expected_Return = Expected_Return_DF_T['Weighted Expected Return'].sum()

## Portfolio volatility
Covariance_DF = Return_DF.cov()
w = np.array(Expected_Return_DF_T['Weight'])
Portfolio_Volatility = np.sqrt(w.T.dot(Covariance_DF).dot(w))

## Portfolio VAR      ### More works
Portfolio_VAR = Net_Exposure * norm.ppf(1-Confidence_Level, Portfolio_Expected_Return, Portfolio_Volatility)

## Asset volatility
a = np.array(Covariance_DF)
b = np.sqrt(a.diagonal())
Volatility_DF_T = pd.DataFrame(b, index = Expected_Return_DF_T.index, columns = ['Volatility'])

## Marginal VAR
w = np.array(Expected_Return_DF_T['Weight'])
Marginal_VaR = Covariance_DF.dot(w) * norm.ppf(1-Confidence_Level, 0, 1)/ Portfolio_Volatility * Net_Exposure ## series
Marginal_VAR_DF_T = pd.DataFrame(Marginal_VaR, columns=['Marginal VaR'], index= Current_DF_T.index)

## Component VAR
compVaR = Marginal_VaR * w/Portfolio_VAR
compVaR_DF_T = pd.DataFrame(compVaR, columns=['Component VaR'], index= Current_DF_T.index)
Portfolio_VaR = compVaR_DF_T['Component VaR'].sum()
compVaR_DF_T['Component VaR Contribution'] = compVaR_DF_T['Component VaR']/Portfolio_VaR

## CVAR
CVaR_List=[]
for col in Return_DF.columns:
    CVaR_List.append(cvar(Return_DF[col], 0.05))
CVaR_DF_T = pd.DataFrame(CVaR_List, columns=['CVaR'] ,index= Current_DF_T.index)
Portfolio_CVaR = CVaR_DF_T['CVaR'].sum()
CVaR_DF_T['CVaR Contribution'] = CVaR_DF_T['CVaR']/Portfolio_CVaR

## Sknewness & Kurtosis
Daily_Return_List =[]
for row in range(0,len(Return_DF)):
    Daily_Return =0
    for col in range(0,len(Return_DF.columns)):
        Daily_Return += Return_DF.ix[row, col]*w[col]
    Daily_Return_List.append(Daily_Return)
Portfolio_Skewness=scipy.stats.skew(Daily_Return_List)
Portfolio_Kurtosis=scipy.stats.kurtosis(Daily_Return_List)

Final_Return_DF_T =pd.concat([Volatility_DF_T,Marginal_VAR_DF_T,compVaR_DF_T,CVaR_DF_T], axis =1)

##MCVAR
Final_Return_DF_T['Marginal CVAR'] = 0
ExportPath = "C:\\Users\\Ku Yeuh Dau GuoYutao\\Desktop\\Hedga\\portoflio analytics\\testing.csv"
Final_Return_DF_T.to_csv(ExportPath,sep=',',index=True,header=True)

### output
print("Gross_Exposure=", Gross_Exposure)
print("Portfolio_VaR=", Portfolio_VaR)
print("Portfolio_CVaR=", Portfolio_CVaR)
print("Portfolio_Expected_Return=", Portfolio_Expected_Return)
print("Net_Exposure=", Net_Exposure)
print("Portfolio_Volatility=", Portfolio_Volatility)
print("Portfolio_Skewness=", Portfolio_Skewness)
print("Portfolio_Kurtosis=", Portfolio_Kurtosis)
