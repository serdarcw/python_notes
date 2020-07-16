https://edabit.com/challenge/arobBz954ZDxkDC9M

Next Prime
Given an integer, create a function that returns the next prime. If the number is prime, return the number itself.
Examples
next_prime(12) ➞ 13

next_prime(24) ➞ 29

next_prime(11) ➞ 11
# 11 is a prime, so we return the number itself.
Notes
N/A

def prime(num):
    K=sum([1 for j in range(2,int(num**(1/2))+1) if num%j==0])
    if K==0: return True
    else: return False
i, mathag =0, True
while mathag==True:
    if prime(num+i)==True:
        print(num+i)
        mathag=False
    else:
        i+=1



def prime(num):
    K=sum([1 for j in range(2,int(num**(1/2))+1) if num%j==0])
    if K==0: return True



def next_prime(num):
	for i in range(2,num):
		print(num,i)
		if i == num-1:
			return num
		if num%i == 0:
			return next_prime(num+1)



