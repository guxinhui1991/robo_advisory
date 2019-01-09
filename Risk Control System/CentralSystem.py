import InfoClass as info
import AcctRiskControl as acct
import EntPosSize as posize
import RiskPerTrade as risktrade
#update information from user settings and market

#update instrument information
spread = info.Instrument().getspread()
digits = info.Instrument().getdigits()
stop_lvl = info.Instrument().get_stoplevel()
contsize = info.Instrument().contsize()
swap = info.Instrument().swaptype()


#update User settings information
bal = info.UserSetting().getbal()
lev = info.UserSetting().getlev()
currency = info.UserSetting().get_currency()
# base and quote. if the quote is not in USD, need to pass in conversion rate to USD
currquote = info.UserSetting().get_currquote()
tradpo = info.UserSetting().get_tradpo()
minmarlev = info.UserSetting().getminmarlev()
addcharges = info.UserSetting().getaddcharges()

#update Market Data information
if currquote != "USD" and currquote != "JPY":
    quoterate_ent = info.MktData().getquoteUSDrate_entry()
    quoterate_curr = info.MktData().getquoteUSDrate_current()
elif currquote== "JPY":
    quoterate_ent = 1/info.MktData().getquoteUSDrate_entry()
    quoterate_curr = 1/info.MktData().getquoteUSDrate_current()
else:
    quoterate_ent = 1
    quoterate_curr = 1
currpr = info.MktData().getcurrpr()

#update Trade Signal information
entrypr = info.TradeSignal().getentryprice()

#update Risk Signal information
potsize = info.RiskSignal().getposize()
currmar = info.RiskSignal().getcurrmar()

#Part 1: Account Level Risk Control
acct.AcctRiskControl(bal,currpr,entrypr,quoterate_curr,quoterate_ent,potsize,contsize,tradpo,lev,currmar,minmarlev,addcharges)
#Part 2: Market Entry Position Size
lots = posize.result(bal)
print("You should trade %f number of trades" %lots)
#Part 3: Risk Per Trade Control
