
https://edabit.com/challenge/HrQoXJYqpYZ2Rqvtb


Product of Digits of Sum
Create a function that takes numbers as arguments, adds them together, 
and returns the product of digits until the answer is only 1 digit long.

Examples
sum_dig_prod(16, 28) ➞ 6
# 16 + 28 = 44
# 4 * 4 =  16
# 1 * 6 = 6

sum_dig_prod(0) ➞ 0

sum_dig_prod(1, 2, 3, 4, 5, 6) ➞ 2
Notes
The input of the function is at least one number.

A=(8618, -2)
B=str(sum(list(A)))
while len(B)!=1:
    mult1=1
    for i in B:
        mult1=mult1*int(i)
    B=str(mult1)	
print(B)





def sum_dig_prod(*args):
    n = sum(args)
    while abs(n) > 9:
        p = 1
        for i in str(n):
            p *= int(i)
        n = p
    return n


def sum_dig_prod(*args):
    s = sum(args)
    p = 1
    for x in str(s):
        p *= int(x)
    while len(str(p)) > 1:
        s=p
        p=1
        for x in str(s):
            p *= int(x)
    return p



def sum_dig_prod(*args):
	n = sum(args)
	while n > 9:
		m = 1
		for i in str(n):
			m *= int(i)
		n = m
	return n





def sum_dig_prod(*n):
  s = str(sum(n))
  while len(s)>1:
    p=1
    for i in range(len(s)):
      p*=int(s[i])
    s=str(p)
  return int(s)





def sum_dig_prod(*ns):
	def prod(n):
		s = str(n)
		p = 1
		for dig in s:
			p *= int(dig)
		if p >= 10:
			p = prod(p)
		return p
	s = sum(ns)
	return prod(s)