#write a function that converts price to pips.
class Instrument(object):
    #spread,digits, stop levels, pending orders GTC, contract size, profit calculation mode, swap type
    ##swap long, swap short, margin calculation, margin hedge
    def getspread(self):
        spread = raw_input("Spread: ")
        return spread
    def getdigits(self):
        digits = int(input("Digits: "))
        return digits
    def get_stoplevel(self):
        stoplvl = input("Stop level: ")
        return stoplvl
    def contsize(self):
        contsize = float(input("Contract Size: "))
        while contsize < 0:
            print("Your contract size cannot be negative.")
            contsize = float(input("Contract Size: "))
        return contsize
    def swaptype(self):
        swaptype = raw_input("Swap type: ")
        return swaptype

class MktData(object):
    def getcurrpr(self):
        currpr = float(input("Current price: "))
        while currpr < 0:
            print("Your current price cannot be negative")
            currpr = float(input("Current price: "))
        return currpr
    def getquoteUSDrate_entry(self):
        quoteUSD = float(input("Market entry quote currency to USD rate: "))
        while quoteUSD < 0:
            print("Your quote currency to USD rate cannot be negative.")
            quoteUSD = float(input("Market entry quote currency to USD rate: "))
        return quoteUSD
    def getquoteUSDrate_current(self):
        quoteUSD = float(input("Current base currency to USD rate: "))
        while quoteUSD < 0:
            print("Your base currency to USD rate cannot be negative.")
            quoteUSD = float(input("Market entry base currency to USD rate: "))
        return quoteUSD

class UserSetting(object):
    def getminmarlev(self):
        minmarlev = float(input("Minimum margin level (in %): "))
        while minmarlev < 100:
            print("Your minimum margin level cannot be less than 100%.")
            minmarlev = float(input("Minimum margin level (in %): "))
        return minmarlev

    def getaddcharges(self):
        addcharges = float(input("Additional charges: "))
        return addcharges

    def getbal(self):
        bal = float(input("Balance: "))
        while bal < 0:
            print("Your balance cannot be negative.")
            bal = float(input("Balance: "))
        return bal

    def getlev(self):
        lev = float(input("Leverage: "))
        while lev < 0:
            print("Your leverage cannot be negative.")
            lev = float(input("Leverage: "))
        return lev

    def get_tradpo(self):
        tradpo = raw_input("Trade Position (long or short): ")
        while tradpo!= "long" and tradpo!= "short":
            print("You have to enter either long or short.")
            tradpo = raw_input("Trade Position (long or short): ")
        return tradpo
    def get_currency(self):
        currency = raw_input("Currency Base Symbol: ")
        return currency
    def get_currquote(self):
        currency_base = raw_input("Currency Quote Symbol: ")
        return currency_base


class TradeSignal(object):
    def getentryprice(self):
        entpr = float(input("Entry price: "))
        while entpr < 0:
            print("Your entry price cannot be negative.")
            entpr = float(input("Entry price: "))
        return entpr

class RiskSignal(object):
    def getposize(self):
        posize = float(input("Position size (number of lots): "))
        while posize < 0:
            print("Your position size cannot be negative.")
            posize = float(input("Position size (number of lots): "))
        return posize

    def getcurrmar(self):
        currmar = float(input("Current Margin: "))
        return currmar
    



