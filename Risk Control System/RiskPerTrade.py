#==Raw inout data variables==
#remaxdown: required maximum drawdown as double
#avgwin: average wins as double
#winrate: win rate as double
#avgloss: average loss as double
#lossrate: loss rate as double
#maxprob: maximum probability of n consecutive losing trades as double

#==Derived outputs==
#n: the number of consecutive trades you are going to execute as int
#riskcap: the percentage of capital you are willing to risk for each trade as double

#==User settings==
import numpy as np
def conlose(lossrate, maxprob):
    return np.log(maxprob)/np.log(lossrate)
def riskptrade(maxdrawdown, numtrades):
    return 1 - np.power(1-maxdrawdown,1/numtrades)
def result():
    remaxdown = float(input("Input your required maximum drawdown (in%): "))
    #avgwin = float(input("Input your average win: "))
    #winrate = float(input("Input your win rate: "))
    #avgloss = float(input("Input your average loss: "))
    lossrate = float(input("Input your loss rate: "))
    maxprob = float(input("Input your maximum probability of n consecutive losing trades: "))

#Data validation

    while remaxdown < 0:
        print("Your required maximum drawdown has to be non-negative")
        remaxdown = float(input("Input your required maximum drawdown"))
    #while avgwin < 0:
        #print("Your average win cannot be negative")
        #avgwin = float(input("Input your average win: "))

    n = conlose(lossrate, maxprob)
    riskcap = riskptrade(remaxdown/100,n)*100
    return riskcap
    #print("Your risk per trade is : " + str(riskcap))