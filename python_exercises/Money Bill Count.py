https://edabit.com/challenge/brJHwyof9NWpXFgS8

Create a function bill_count that takes two arguments. The first argument is the amount of money the user has and the second is the list of money bills available. Return the minimum count of money bills required to equal the user money amount.

bill_count(1001, [1, 10, 20])
# User Money = €1000 and Bills Available = [€1, €10, €20]

bill_count(1001, [1, 10, 20]) ->51 because 20*50+ 1*1 = 1001
# We require 50  20€ bill and 1 1€ bill to equal €1001.
# Therefore, Minimum Count Money Bills is 50 + 1 = 51.
Examples
bill_count(100, [1, 10, 20]) ➞ 5
# Because 20 * 5 = 100

bill_count(1050, [1, 10, 20, 100]) ➞ 13
# Because 100 * 10 + 20 * 2 + 10 * 1 = 1050

bill_count(3, [1, 10]) ➞ 3
# Because 3 * 1 = 3

bill_count(55, [1, 5, 10, 50]) ➞ 2
# Because 50 * 1 + 5 * 1 = 55


A=555
B=[1, 10, 100]
count=0
for i in sorted(B, reverse=True):
    if A//i>0:  
        count+=A//i
        A-=i*(A//i)
print(count)


def bill_count(money, bills):
	count = 0
	while money:
		for bill in bills[::-1]:
			count += money//bill
			money -= (money//bill)*bill
	return count


def bill_count(money, bills):
    notes =(bills[::-1])
    noteCounter =[0,0,0]
    count=0  
    for i, j in zip(notes, noteCounter): 
        if money >= i: 
            j = money // i 
            money = money - j * i 
            count+=j
    return count

def bill_count(money, bills):
    count = 0
    for bill in bills[::-1]:
        if money // bill:
            count += money // bill
            money %= bill
    return count

