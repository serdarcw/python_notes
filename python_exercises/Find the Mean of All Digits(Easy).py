https://edabit.com/challenge/BZ4mMcEz3aqosEtbC


Find the Mean of All Digits
Create a function that returns the mean of all digits.

Examples
mean(42) ➞ 3

mean(12345) ➞ 3

mean(666) ➞ 6
Notes
The mean of all digits is the sum of digits / how many digits there are (e.g. mean of digits in 512 is (5+1+2)/3(number of digits) = 8/3=2).
The mean will always be a integer.


def mean(num):
	k=0
	for i in str(num):
		k=k+int(i)
	return k/len(str(num))

def mean(num):
	x = [int(x) for x in str(abs(num))]
	return sum(x)/len(x)


def mean(num):
	all = 0.0
	count = len(str(num))
	for i in str(num):
		all = all+int(i) 
	return all/count

def mean(num):
	res = [int(x) for x in str(num)]
	return sum(res)/len(res)

def mean(num):
	res = list(map(int, str(abs(num))))
	sum=0
	for x in res: 
		sum=sum+x
	return sum/len(res)