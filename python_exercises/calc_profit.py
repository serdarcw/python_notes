
profit = {
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}
#14796

#profit({
#  "cost_price": 225.89,
#  "sell_price": 550.00,
#  "inventory": 100
#}) ➞ 32411
#
#profit({
#  "cost_price": 2.77,
#  "sell_price": 7.95,
#  "inventory": 8500
#}) ➞ 44030
#Notes

print(round(profit['inventory']*(profit['sell_price']-profit['cost_price'])))