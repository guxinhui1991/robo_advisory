class GeneralUserSetting(object):
    def getmaxdrawdown(self):
        maxdrawdown = float(input("Maximum Drawdown(in %): "))
        return maxdrawdown

    def getdrawdownwarning(self):
        drawdownwarning = float(input("Drawdown Warning Level(in %): "))
        return drawdownwarning

    def getmarginlevelcontrol(self):
        marginlevelcontrol = float(input("Margin Level Control: "))
        return marginlevelcontrol