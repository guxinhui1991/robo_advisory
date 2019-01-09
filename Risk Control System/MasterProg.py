###Part 1: Account Risk Control:
#==Raw data input variables==
#bal: balance value as double
#lev: leverage value as int
#tradpo: trade position as string
#entrypr: entry price as double
#currpr: current price as double
#contsize: contract size as double
#minmarlev: minimum margin level as double (in percentage form)
#addcharges: additional charges as double

#==Derived Output Variables
#equ: equity as double
#mar: margin as double
#freemar: free margin as double

###Part 2: Entry Position Size
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
#lots: the number of lots to be placed for trade as double

##User settings:
print("Part 1: Account Level Risk Control")
bal = input("Enter your account balance: ")
while bal < 0:
    print "Your balance has to be 0 or positive"
    bal = input("Enter your account balance: ")
bal = float(bal)
lev = input("Enter your leverage number (ex: 1:10, enter 10, has to be integer number): ")
lev = float(lev)
tradpo = raw_input("Enter your trade position - enter long if it's long, enter short if it's short: ")
while tradpo!= "long" and tradpo != "short":
    print "You enter the wrong letter"
    tradpo = raw_input("Enter your trade position - enter long if it's long, enter short if it's short: ")

entrypr = input("Entry price: ")
while entrypr< 0:
    print "Entry price cannot be negative"
    entrypr = input("Entry price: ")
entrypr = float(entrypr)
currpr = input("Current price: ")
while currpr < 0:
    print "Error in current price input"
    currpr = input("Current price: ")
currpr = float(currpr)
contsize = input("Contract size: ")
while contsize < 0:
    print "Contract price cannot be negative"
    contsize = input("Contract size: ")
contsize = float(contsize)
minmarlev = input("Minimum Margin Level: ")
minmarlev = float(minmarlev)
addcharges = input("Additional charges: ")


##Functions:
def equity(bal,st, s0, size):
    return bal + (st-s0)*size
def margin(st, lev, size):
    return st*size/lev
def freemargin(equity, margin):
    return equity - margin
def marginlev(equity, margin):
    return (equity/margin)*100
def AcctRiskControl():
    equ = equity(bal,currpr,entrypr,contsize)
    mar = margin(currpr,lev,contsize)
    freemar = freemargin(equ,mar)
    marlev = marginlev(equ,mar)
    if marlev < minmarlev:
        print("Your trades break the account's minimum margin level. Hence, you can't execute these trades")
        maxexpo = (freemar - mar * minmarlev)/(1+minmarlev)
        print("The maximum additional lots you can trade is: " + maxexpo)
    else:
        print("You are allowed to execute the trades")
        maxexpo = ((freemar - mar * minmarlev)/(1+minmarlev)/currpr)/contsize
        print("The maximum additional lots you can trade is: " + maxexpo)

AcctRiskControl()
print("Part 2: Market Entry Position Size")

def EntPosSize():
    print("Position size: ")
