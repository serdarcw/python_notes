Alinin babasının cebinde budget miktar para var ve oyuncakların fiyat listesi mevcut
Alinin babası elindeki para ile kaç oyuncak alabilir

prices = [111,12,5,5,200,1,5,1000,10]
budget = 34
count=0
for i in sorted(prices):
    if budget>=i:
        budget= budget-i
        count+=1
print(count)

prices =[1 ,12, 5, 5, 5, 111 ,200 ,1000 ,10] # 1,5,10,12...1000
budget =16
prices.sort()
total_toys = 0 
while budget >= 0 and total_toys < len(prices):
    budget -= prices[total_toys]
    total_toys+=1
print(total_toys-1)