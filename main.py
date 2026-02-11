import random
import matplotlib.pyplot as plt
''' created a dictionary (aka named lists)'''
my_dict = {}
prices = {
    "A": [],
    "B": [],
    "C": [],
    "D": [],
    "E": []
}
''' gave 5 stocks and starting price is 100'''
prices["A"].append(100)
prices["B"].append(100)
prices["C"].append(100)
prices["D"].append(100)
prices["E"].append(100)
''' the outer for loop ,loops the stocks from a to e
and the inner for loop ranges the day from 1 to 60 '''
for stock in prices:
    for i in range(59):
        last_price = prices[stock][-1]
        change = random.uniform(-0.01,0.01)
        new_price = last_price * (1+change)
        prices[stock].append(new_price)
print(len(prices["A"]))
print(len(prices["B"]))
print(len(prices["C"]))
print(len(prices["D"]))
print(len(prices["E"]))
cash = 10000
shares  = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "E": 0
}
money_per_stock = cash // 5
total_spent = 0 
for stock in shares:
    shares[stock] = money_per_stock//prices[stock][0]
for stock in shares:
    total_spent += (shares[stock] * prices[stock][0])
''' calculated the total spent till now '''
portfolio_value = cash
for stock in shares:
    portfolio_value += shares[stock] * prices[stock][20]

target_value = portfolio_value/5
desired_shares = {}
for stock in shares:
    current_price = prices[stock][20]
    desired_shares[stock] = target_value // current_price
''' we are doing the sell phase now'''

diff = {}
for stock in shares:
    diff[stock] = desired_shares[stock] - shares[stock]
for stock in shares:
    if diff[stock] < 0:
        shares_to_sell = -diff[stock]
        current_price = prices[stock][20]
        shares[stock] -= shares_to_sell
        cash += shares_to_sell * current_price
''' buy phase'''
for stock in shares:
    if diff[stock] > 0:
        shares_to_buy = diff[stock]
        shares[stock] += shares_to_buy
        cash -= shares_to_buy * current_price
cash_after_20 = cash
shares_after_20 = shares.copy()
''' day 40 now'''
portfolio_value = cash
for stock in shares:
    portfolio_value += shares[stock] * prices[stock][40]

target_value = portfolio_value/5
desired_shares = {}
for stock in shares:
    current_price = prices[stock][40]
    desired_shares[stock] = target_value // current_price
diff = {}
for stock in shares:
    diff[stock] = desired_shares[stock] - shares[stock]
for stock in shares:
    if diff[stock] < 0:
        shares_to_sell = -diff[stock]
        current_price = prices[stock][40]
        shares[stock] -= shares_to_sell
        cash += shares_to_sell * current_price
''' buy phase'''
for stock in shares:
    if diff[stock] > 0:
        shares_to_buy = diff[stock]
        current_price = prices[stock][40]
        shares[stock] += shares_to_buy
        cash -= shares_to_buy * current_price
print("Day 40 cash:", cash)
print("Day 40 shares:", shares)
cash_after_40 = cash
shares_after_40 = shares.copy()

ew_value = cash

for stock in shares:
    ew_value += shares[stock] * prices[stock][59]

print("Equal-Weight final value:", ew_value)
''' comparing without rebalancing '''
cash_bh = 0

shares_bh = {
    "A": 20,
    "B": 20,
    "C": 20,
    "D": 20,
    "E": 20
}
bh_value = cash_bh
for stock in shares_bh:
    bh_value += (shares_bh[stock] * prices[stock][59])
print("Buy & Hold final value:", bh_value)
days = list(range(60))
''' we want  a plot so we appending values to a list'''
bh_curve = []
for d in days:
    value = 0
    for stock in shares_bh:
        value += shares_bh[stock] * prices[stock][d]
    bh_curve.append(value)
ew_curve = []
for d in range(0,20):
    value = cash_bh
    for stock in shares_bh:
        value += shares_bh[stock]* prices[stock][d]
    ew_curve.append(value)
for d in range(20,40):
    value = cash_after_20
    for stock in shares_after_20:
        value += shares_after_20[stock] * prices[stock][d]
    ew_curve.append(value)
for d in range(40, 60):
    value = cash
    for stock in shares:
        value += shares[stock] * prices[stock][d]
    ew_curve.append(value)


plt.plot(days,bh_curve,label = "buy and hold")
plt.plot(days,ew_curve, label = "rebalanced")
plt.xlabel("Day")
plt.ylabel("portfolio value")
plt.title("buy and hold vs equal weight rebalanced")
plt.legend()
plt.show()
plt.axvline(20, linestyle='--', alpha=0.5)
plt.axvline(40, linestyle='--', alpha=0.5)