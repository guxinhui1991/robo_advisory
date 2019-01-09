#=====Variables from General Settings=====
#Maximum Drawdown: required maximum drawdown as double
#Drawdown Warning: required warning percentage as double
#Margin Level Control: margin level control as double

#==Raw inout data variables==
#Maximum Drawdown: required maximum drawdown as double
#Current Drawdown: current drawdown as double
#Portfolio Returns: (a). weight vector as double array
#                   (b). historical returns as double array

#==Derived outputs==
#Risk Budget: Remaining risk budget, unit in percentage as double
#WinRate: Percentage of positive returns, unit in percentage as double
#MaxConsecutiveLosses: Maximum consecutive losses with the current win rate, unit inß int
#RiskPerDay: Maximum consecutive losses with the current win rate unit in percentage as double


import numpy as np
import RiskPerTrade as risktrade
import InfoClass as info

##### TO-DO
##### Placeholder for the following two classes
import RiskSetting as risksetting
import PnL as pnl
import PortfolioReturns as portfolioreturns

#General settings information
maxdrawdown = info.GeneralUserSetting().getmaxdrawdown()
drawdownwarning = info.GeneralUserSetting().getdrawdownwarning()
marginlevelcontrol = info.GeneralUserSetting().getmarginlevelcontrol()
warninglevel = drawdownwarning * maxdrawdown


#Input for risk budgeting
##### TO-DO
##### Placeholder for currentDrawdown, portfolio returns
currentDrawdown = 0.1
portfolioreturns = np.ndarray(shape=(1, 100), dtype=double)
#portfolioreturns  = portfolioreturns.getreturns()
currentDD = float(input("Input current drawdown"))

def getriskbudget(maxdrawdown): 
    return maxdrawdown - currentDD
def getwinrate(portfolioreturns):
    NumPosReturns = np.size(np.where(portfolioreturns>0))
    TotalNumReturns = np.size(portfolioreturns)
    return NumPosReturns/TotalNumReturns
def getmaxconsecutivelosses(WinRate):
    LossPercentage= float(input("Input required maximum consecutive losses(in %): "))
    return log(LossPercentage)/(1- WinRate)

def getriskpday():
    if(currentDD<=warninglevel):
        return 1-(1-getmaxdrawdown)^(1/n)
    else:
        return 1-(1-getriskbudget)^(1/n)

def getriskbudget(self):
    return riskbudget