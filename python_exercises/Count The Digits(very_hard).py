https://edabit.com/challenge/dLYhGnWQ5Q8DRmnbR

Count The Digits
Create a function that will count the number of digits of a number. Conversion of the number to a string is not allowed, thus, the approach is either recursive or via loops.

Examples
digits_count(0) ➞ 1

digits_count(12345)  ➞ 5

digits_count(1289396387328) ➞ 13
Notes
All inputs are integers but some are in exponential form, so, deal with it accordingly.
A recursive version of this challenge can be found here.

n = 0
k, A, m=1, 0, 0
while m<=0:
    A=10**(k)
    m=A-n
    k+=1
print(k-1)


def digits_count(n):
	return 1 if -10<n<10 else 1+digits_count(n//10)


def digits_count(n, k=1):
  while abs(n) >= 10: n, k = n//10, k+1
  return k


def digits_count(n):
    res, n = 1, abs(n)
    while n > 9:
        res += 1
        n //= 10
    return res


def digits_count(n):
    '''
    Returns a count of the digits in integer n
    '''
    counter = lambda x: 1 if x < 10 else 1 + counter(x//10)

    return counter(int(abs(n)))