import RiskPerTrade as risktrade
#==Raw input data variables ==
#x%: risk per trade
#cap: input the amount of capital invested

#==Derived outputs
#number of lots to trade

##==User settings ==
def result(bal):
    print("Part 2: Market Entry Position Size")
    x = risktrade.result()
    x = float(x)
    lots = (x*bal/100)/10
    return lots
