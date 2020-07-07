https://edabit.com/challenge/BfSj2nBc33aCQrbSg

Truncatable Primes
A left-truncatable prime is a prime number that contains no 0 digits and, when the first digit is successively removed, the result is always prime.

A right-truncatable prime is a prime number that contains no 0 digits and, when the last digit is successively removed, the result is always prime.

Create a function that takes an integer as an argument and:

If the integer is only a left-truncatable prime, return "left".
If the integer is only a right-truncatable prime, return "right".
If the integer is both, return "both".
Otherwise, return False.
Examples
truncatable(9137) ➞ "left"
# Because 9137, 137, 37 and 7 are all prime.

truncatable(5939) ➞ "right"
# Because 5939, 593, 59 and 5 are all prime.

truncatable(317) ➞ "both"
# Because 317, 17 and 7 are all prime and 317, 31 and 3 are all prime.

truncatable(5) ➞ "both"
# The trivial case of single-digit primes is treated as truncatable from both directions.

truncatable(139) ➞ False
# 1 and 9 are non-prime, so 139 cannot be truncatable from either direction.

truncatable(103) ➞ False
# Because it contains a 0 digit (even though 103 and 3 are primes).
Notes
The input integers will not exceed 10^6.



B=131
A=str(B)
left, right, contrl=[], [], ''
def prime(num):
    K=sum([1 for j in range(2,int(num**(1/2))+1) if num%j==0])
    if K==0: return True
    else: return False
if '0' in A: print('False')
else:
    for i in range(len(str(A))):
        if prime(int(A[0:i+1]))==False or int(A[0:i+1])==1: break
    else:
        contrl+='right'
    for i in range(1,len(str(A))+1):
        if prime(int(A[-i:]))==False or int(A[-i:])==1: break
    else:
        contrl+='left'
    print('both'*(len(contrl)>5) or 'False'*(len(contrl)==0) or 'left'*(len(contrl)==4) or 'right'*(len(contrl)==5))




import math
def is_prime(num):
    if num >= 2:
        i=2
        while i <= math.sqrt(num):
            if num % i == 0:
                return False
            i += 1
        else:
            return True
    else:
        return False
def truncatable(num):
    right= sum([ 1 for i in range(1,len(str(num))+1)  if is_prime(int(str(num)[:i])) ])==len(str(num))
    left= sum([ 1 for i in range(len(str(num))) if is_prime(int(str(num)[i:])) ])==len(str(num))
    if "0" in str(num):
        return False
    else:
        return "both"*left*right or "right"*right or "left"*left or False
truncatable(62383)





def isprime(n):
    # return all([n%i==0 for i in range(2,n//2)])
    return not any([n%i==0 for i in range(2,n//2)])
def l_truncatable(n):
    n=str(n)
    return  all([isprime(int(n[i:])) for i in range(len(n)) ] )
def r_truncatable(n):
    n=str(n)
    return  all([isprime(int(n[:i])) for i in range(len(n),0,-1) ] )
n = 317
print(l_truncatable(n)r_truncatable(n)"Both" or l_truncatable(n)'Left' or r_truncatable(n)"Right" )



def prime(x):
  return x > 1 and not any (x%i==0 for i in range (2,x))

def left(x):
  return all(prime(int(x[i:])) for i in range (len(x)))

def right(x):
  return all(prime(int(x[:i+1])) for i in range (len(x)))

def truncatable(n):
  n = str(n)
  if "0" in n:
    return False
  if left(n) and right(n):
    return "both"
  if left(n):
    return "left"
  if right(n):
    return "right"
  else:
    return False



