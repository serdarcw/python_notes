https://edabit.com/challenge/yXZhG7zq6dWhWhirt

Filter Primes from a List
Create a function that takes a list and returns a new list containing only prime numbers.

Examples
filter_primes([7, 9, 3, 9, 10, 11, 27]) ➞ [7, 3, 11]

filter_primes([10007, 1009, 1007, 27, 147, 77, 1001, 70]) ➞ [10007, 1009]

filter_primes([1009, 10, 10, 10, 3, 33, 9, 4, 1, 61, 63, 69, 1087, 1091, 1093, 1097]) ➞ [1009, 3, 61, 1087, 1091, 1093, 1097]
Notes
New list must maintain the order of primes as they first appear in the original list.
Check the Resources tab for help.



A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

def prime(j):
    return not ([1 for i in range(2, int(j**(1/2)+1)) if j%i==0])

print([i for i in A if prime(i)==True and i!=1])




def filter_primes(num):
	return [n for n in num if n > 1 and all(n%i for i in range(2,int(n**0.5)+1))]


def filter_primes(num):
	return [i for i in num if prime(i)]

def prime(n):
	for i in range(2,n):
		if n%i == 0:
			return False
	return n != 1


def filter_primes(N):
	return [n for n in N if 2 in [n, 2 ** n % n]]

