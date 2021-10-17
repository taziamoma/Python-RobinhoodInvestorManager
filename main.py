from robinhood import portfolio as rh_portfolio

class Investor:

    global rh_portfolio #Set as global to use the global variable that refers tot the total current porfolio percent increase
    global fullPortfolio
    def __init__(self, name, initInv):
        self.name = name
        self.initInv = initInv #Initial investment amount
        self.adjustedPortfolioAmt = self.initInv #Amount the portfolio was at plus the initial investment amount

    def getAdjustedPortfolioAmt(self):
        return self.adjustedPortfolioAmt

    def getCurrentInv(self):
        return (self.getAdjustedPortfolioAmt() * float(rh_portfolio)) + self.getAdjustedPortfolioAmt() #Current investment total

    def getEquityPercent(self):
        return (self.getCurrentInv() / fullPortfolio) * 100  # Total percent equity you have of the current portfolio

    def getProfit(self): #Returns the profit from subtracting the current investment value by the initial investment
        return self.adjustedPortfolioAmt * float(rh_portfolio)

    def addInv(self, addAmt): #Adds new investment and adjusts the currentPorfolio to reflect that
        global fullPortfolio
        self.adjustedPortfolioAmt += addAmt
        fullPortfolio += addAmt
        print("{} is adding {}".format(self.name, addAmt))


def getPorfolioPercent(investors, port):
    initInv = 0
    port = float(port)
    for investor in investors:
        initInv += investor.initInv
    percentInc = float(((port - initInv) / initInv) * 100)
    
    return percentInc


#Generate Investor Classes
Taz = Investor("Taz", 4000)
Hunter = Investor("Hunter", 1000)


#Create a list with all objects
investors = [Taz, Hunter]

print("Percent increase: {}".format(getPorfolioPercent(investors, rh_portfolio)))

#Handling Methods
def listInvestors(investors):
    for investor in investors:
        print("Name: {}".format(investor.name))
        print("Initial Investment: ${}".format(investor.initInv))
        print("Portfolio Percentage: {}%".format(investor.getEquityPercent()))
        print("Adjusted Portfolio: ${}".format(investor.getAdjustedPortfolioAmt()))
        print("Current Investment: ${}".format(investor.getCurrentInv()))
        print("Profit: ${}".format(investor.getProfit()))
        print()

#Calculates the total initial investments from all investors
def getTotalInitInvestment(investors):
    total = 0
    for investor in investors:
        total += investor.initInv
    return total

def getTotalCurrentInvestment(investors):
    total = 0
    for investor in investors:
        total += investor.getCurrentInv()
    return total

def printInvestorPorfolio(investors):
    for investor in investors:
        print("{} - {}".format(investor.name, investor.getCurrentInv()))

totalInitialInvestment = getTotalInitInvestment(investors)
fullPortfolio = getTotalCurrentInvestment(investors)


#Current section------------------------------------------
fullPortfolio = getTotalCurrentInvestment(investors)
listInvestors(investors)
totalCurrentInv = getTotalCurrentInvestment(investors)

print("Total Current Investment: {}".format(totalCurrentInv))
print("Investor Current Investments")
print(printInvestorPorfolio(investors))

print("Current Porfolio: {}".format(fullPortfolio))
print("Total profit: {}".format(fullPortfolio - totalInitialInvestment))

#Create method that updates all object related information