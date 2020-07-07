
https://edabit.com/challenge/G9QRtAGXb9Cu368Pw

Combinations
Create a function that takes a variable number of groups of items, and 
returns the number of ways the items can be arranged, with one item from each group. Order does not matter.

Examples
combinations(2, 3) ➞ 6

combinations(3, 7, 4) ➞ 84

combinations(2, 3, 4, 5) ➞ 120
Notes
Don't overthink this one.


Not: Bu problemin verilişinde ilk verilen items i liste haline getirmek için *items yazmak gereklidir
Soruda bir de dikkat edilecek nokta 0 gelirse çarpıma dahil edilmememsidir


def combinations(*items):
	sum1=1
	for i in list(items):
		if i==0: pass
		else: sum1=sum1*i
	return sum1


fdsafdsafdsaf


  def combinations(*items):
	prod = 1
	for i in items:
		if i>0:
			prod*=i
	return prod



def combinations(*items):
	ret = 1
	for i in items:
		ret *= max(i,1)
	return ret


def combinations(*items):
	product = 1
	for item in items:
		if item:
			product *= item 
	return product


  def combinations(*items):
	prod = 1
	for i in items:
		if i != 0:
			prod *= i
	return prod




  def combinations(*items):
    ans = 1
    for c in items:
        if c > 0:
            ans *= c
    return ans



  def combinations(*items):
	prod = 1
	for i in items:
		if i > 0:
			prod *= i
	return prod


from numpy import prod
def combinations(*a):
	return prod([x for x in a if x>0])


	fefsfdsakifla