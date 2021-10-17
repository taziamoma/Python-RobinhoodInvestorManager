import robin_stocks.robinhood as rs

username = input("What is your username?")
password = input("what is your password?")
print();

rs.login(username=username, password=password, expiresIn=86400, by_sms=True)

portfolio = rs.profiles.load_portfolio_profile(info=None)
acc = rs.account.load_phoenix_account()
portfolio = acc['portfolio_equity']['amount']
