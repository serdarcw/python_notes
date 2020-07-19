https://edabit.com/challenge/ozMMLxJRPXBwm3yTP

Is the Input Factorial of an Integer?
Create a function that checks if a given integer is exactly the factorial of an integer or not. True if it is, False otherwise.

Examples
is_factorial(2) ➞ True
# 2 = 2 * 1 = 2!

is_factorial(27) ➞ False

is_factorial(24) ➞ True
# 24 = 4 * 3 * 2 * 1 = 4!
Notes
No error handling is necessary. Inputs are all positive integers.
Alternatively, you can solve this via a recursive approach if you get the hang of recursion as simplistic solution to inline functions.

n = 24
k, A = 1, 1
while A<n:
	A*=k
	k+=1
	if A==n:
		print(True)
print(False) 



def is_factorial(n,n2=1,i=2):
	if n==n2:
	 	return True
	elif n2>n:
		return False
	return is_factorial(n,n2*i,i+1)



def is_factorial(n,k=1):
	if n==1: return True
	return False if n%k else is_factorial(n//k,k+1)