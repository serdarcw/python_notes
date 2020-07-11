https://edabit.com/challenge/8vBvgJMc2uQJpD6d7

Prime Factorization of an Integer
Create a function that returns a list containing the prime factors of whatever integer is passed to it.

Examples
prime_factors(20) ➞ [2, 2, 5]

prime_factors(100) ➞ [2, 2, 5, 5]

prime_factors(8912234) ➞ [2, 47, 94811]
Notes
Implement your solution using trial division.
Your solution should not require recursion.

Kendi çözümüm
A=8912234
B=[]
i=2
while A!=1:
	if A%i==0:
		B.append(i)
		A=A//i
	if A%i!=0: i+=1
print(B)


def prime_factors(num):
	res = []
	i=2
	while i<=num:
		while num%i==0:
			res.append(i)
			num = num//i
		i+=1
	return res



def prime_factors(num):
    output = []
    for i in range(2,  int(num/2)):
        while num % i == 0:
            output.append(i)
            num = int(num / i)

    return output



def prime_factors(num):
	l = []
	factor = 2
	while num > 1:
		if num % factor == 0:
			l.append(factor)
			num = num/factor
		else:
			factor = factor + 1
	return l