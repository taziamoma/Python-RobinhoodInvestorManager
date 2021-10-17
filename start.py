from robinhood import portfolio as rh_portfolio

rh_portfolio = float(rh_portfolio)
class Investor:
    global rh_portfolio  # Set as global to use the global variable that refers tot the total current porfolio percent increase
    global fullPortfolio

    def __init__(self, name, initInv):
        self.name = name
        self.initInv = initInv  # Initial investment amount

    def getCurrentInv(self):
        global percentInc
        return self.initInv * (1 + (percentInc / 100))  # Current investment total

    def getEquityPercent(self):
        return (self.getCurrentInv() / rh_portfolio) * 100  # Total percent equity you have of the current portfolio

    def getProfit(self):  # Returns the profit from subtracting the current investment value by the initial investment
        global percentInc
        return self.initInv * (percentInc / 100)

    def addInv(self, addAmt):  # Adds new investment and adjusts the currentPorfolio to reflect that
        global fullPortfolio
        fullPortfolio += addAmt
        print("{} is adding {}".format(self.name, addAmt))


# Generate Investor Classes
Taz = Investor("Taz", 24000)
Hunter = Investor("Hunter", 2000)

# Create a list with all objects
investors = [Taz, Hunter]


# Handling Methods
def listInvestors(investors):
    for investor in investors:
        print("Name: {}".format(investor.name))
        print("Initial Investment: {}".format("${:,.2f}".format(investor.initInv)))
        print("Portfolio Percentage: {}%".format( "{:.2f}".format(investor.getEquityPercent())))
        print("Current Investment: {}".format("${:,.2f}".format(investor.getCurrentInv())))
        print("Profit: {}".format("${:,.2f}".format(investor.getProfit())))
        print()


def getTotalInitInvestment(investors):
    total = 0
    for investor in investors:
        total += investor.initInv
    return total


def printInvestorPorfolio(investors):
    for investor in investors:
        print("{}: {}".format(investor.name, "${:,.2f}".format(investor.getCurrentInv())))


totalInitialInvestment = getTotalInitInvestment(investors)

percentInc = float(((rh_portfolio - totalInitialInvestment) / totalInitialInvestment) * 100)

print("INVESTORS ----------------------------")
listInvestors(investors)


print("Investor Current Investments")
printInvestorPorfolio(investors)

print()
print("Initial investments: {}".format("${:,.2f}".format(totalInitialInvestment)))
print("Current Porfolio: {}".format("${:,.2f}".format(rh_portfolio)))
print("Percent increase: {}%".format("{:.2f}".format(percentInc)))
print("Total profit: {}".format("${:,.2f}".format(rh_portfolio - totalInitialInvestment)))

# Create method that updates all object related information