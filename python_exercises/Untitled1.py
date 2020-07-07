Mark and Jane are very happy after having their first child. Their son loves toys,
so Mark wants to buy some. There are a number of different toys lying in front of him,
tagged with their prices.
Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money.


prices =[1 ,12, 5,5,5, 111 ,200 ,1000 ,10] # 1,5,10,12...1000
budget =16
prices.sort()
total_toys = 0 
while budget >= 0 and total_toys < len(prices):
    budget -= prices[total_toys]
    total_toys+=1
print(total_toys-1)