https://edabit.com/challenge/5ou6SKDtFRZugbpda

Persistence
The additive persistence of an integer, n, is the number of times you have to replace n with the sum of its digits until n becomes a single digit integer.

The multiplicative persistence of an integer, n, is the number of times you have to replace n with the product of its digits until n becomes a single digit integer.

Create two functions that take an integer as an argument and:

Return its additive persistence.
Return its multiplicative persistence.
Examples: Additive Persistence
additive_persistence(1679583) ➞ 3
# 1 + 6 + 7 + 9 + 5 + 8 + 3 = 39
# 3 + 9 = 12
# 1 + 2 = 3
# It takes 3 iterations to reach a single-digit number.

additive_persistence(123456) ➞ 2
# 1 + 2 + 3 + 4 + 5 + 6 = 21
# 2 + 1 = 3

additive_persistence(6) ➞ 0
# Because 6 is already a single-digit integer.
Examples: Multiplicative Persistence
multiplicative_persistence(77) ➞ 4
# 7 x 7 = 49
# 4 x 9 = 36
# 3 x 6 = 18
# 1 x 8 = 8
# It takes 4 iterations to reach a single-digit number.

multiplicative_persistence(123456) ➞ 2
# 1 x 2 x 3 x 4 x 5 x 6 = 720
# 7 x 2 x 0 = 0

multiplicative_persistence(4) ➞ 0
# Because 4 is already a single-digit integer.

def additive_persistence(n):
	count= 0
	while len(str(n))!=1: 
		n=sum([int(i) for i in str(n)])
		count+=1
	return count

def multiplicative_persistence(n):
    count =0
    while len(str(n))!=1:
        B=1
        for i in str(n):
            B*=int(i)
        count+=1
        n=B
    return count






def product(n):
    prod = 1
    for i in str(n):
        prod *= int(i)
    return prod

def additive_persistence(n):
    p = 0
    while n > 9:
        n = sum(int(i) for i in str(n))
        p += 1
    return p

def multiplicative_persistence(n):
    p = 0
    while n > 9:
        n = product(n)
        p += 1
    return p




func = lambda x, y: eval(x.join(str(y)))

def additive_persistence(n):
	if n < 10: return 0
	
	count = 0
	while n > 9:
		n = func('+', n)
		count += 1
	return count
		
def multiplicative_persistence(n):
	if n < 10: return 0
	
	count = 0
	while n > 9:
		n = func('*', n)
		count += 1
	return count






    def additive_persistence(n,step=0):
  if n < 10:
    return step
  else:
    step += 1
    n = sum(int(i) for i in str(n))
    return additive_persistence(n,step)
​
def multiplicative_persistence(n,step=0):
  if n < 10:
    return step
  else:
    step += 1
    prod = 1
    for i in [int(i) for i in str(n)]:
      prod *= i
    return multiplicative_persistence(prod,step)