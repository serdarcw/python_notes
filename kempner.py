
https://edabit.com/challenge/qQnWXBsQaH73yY8r4


The Kempner Function
The Kempner Function, applied to a composite number, permits to find the smallest integer greater than zero which factorial is exactly divided by the number.

kempner(6) ➞ 3

1! = 1 % 6 > 0
2! = 2 % 6 > 0
3! = 6 % 6 === 0

kempner(10) ➞ 5

1! = 1 % 10 > 0
2! = 2 % 10 > 0
3! = 6 % 10 > 0
4! = 24 % 10 > 0
5! = 120 % 10 === 0
A Kempner Function applied to a prime will always return the prime itself.

kempner(2) ➞ 2
kempner(5) ➞ 5
Given an integer n, implement a Kempner Function.

Examples
kempner(6) ➞ 3

kempner(10) ➞ 5

kempner(2) ➞ 2
Notes
Try to solve this using a recursive method, with an approach oriented to higher order functions.
If you need to get more confident with recursion and factorials, try this challenge.






A=6
import math
for i in range(1,A+1):      
    if math.factorial(i)%n==0:
        break
print(i)





def kempner(n, i=1, total=1):
    return max(1, i-1) if total%n == 0 else kempner(n, i+1, total*i)




from math import factorial as f
def kempner(n, i=1):
    return kempner(n, i +1) if f(i)%n else i






def kempner(n):
	mult = 1
	for x in range(1 , n+1):
		mult *= x
		if mult % n == 0:
			return (x)






def kempner(n):
	import math
	for i in range(1,n+1):      
		if math.factorial(i)%n==0:
			break
	return(i)






def kempner(num):
    if num ==1:
        return 1
    def factorial(n):
        fac = 1
        for l in range(1,n+1):
            fac *= l
        return fac
    for i in range(2,num+1):
        if factorial(i)%num == 0:
            return i





from functools import reduce
def kempner(n):
	for i in range(1,n+1):
		if reduce(lambda x, y: x*y, range(1,i+1)) % n == 0:
			return i


#import time
#start = time.time()
#code blok
#end  = time.time()
#print(end-start) 