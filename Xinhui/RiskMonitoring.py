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
import RiskBudgeting as riskbudget

##### TO-DO
##### Placeholder for the following two classes
import RiskSetting as risksetting
import PnL as pnl

#General settings information
maxdrawdown = info.GeneralUserSetting().getmaxdrawdown()
drawdownwarning = info.GeneralUserSetting().getdrawdownwarning()
marginlevelcontrol = info.GeneralUserSetting().getmarginlevelcontrol()
warninglevel = drawdownwarning * maxdrawdown

#Input for risk monitoring
riskbudget = riskbudget.getriskbudget(maxdrawdown)
riskperday = riskbudget.getriskpday()##### TO-DO

##### TO-DO
##### Placeholder for currentDrawdown, portfolio returns
currentDrawdown = 0.1
portfolioreturns = np.ndarray(shape=(1, 100), dtype=double)
#portfolioreturns  = portfolioreturns.getreturns()
winrate = riskbudget.getwinrate(portfolioreturns)



def getportfolioexpectedloss(portfolioreturns, winrate): 
    sortedreturns = np.sort(portfolioreturns)
    cvarconfidence =  winrate
    index = int(np.size(portfolioreturns)*cvarconfidence)
    sumloss = 0
    for i in range(0, index):
        sumloss+=portfolioreturns[index]
    portfolioexpectedloss = sumloss/(index+1)
    return portfolioexpectedloss

def getportfoliotailrisk(portfolioreturns):
    confidence = 0.99
    index = int(np.size(portfolioreturns)*confidence)
    return portfolioreturns[index]


portfolioexpectedloss = getportfolioexpectedloss(portfolioreturns, winrate)
portfoliotailrisk=getportfoliotailrisk(portfolioreturns)

if(riskperday < portfolioexpectedloss|riskbudget < portfoliotailrisk):
    ##### TODO
    #Placeholder for adjusing portfolio class
    print("Warning: Adjust portfolio")

if(currentDrawdown>warninglevel):
    print("Warning: ")

        
    