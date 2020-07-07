#Create a function that takes two numbers as arguments (num, length) and returns a list of multiples of num up to length.
#
#Examples
#list_of_multiples(7, 5) ➞ [7, 14, 21, 28, 35]
#
#list_of_multiples(12, 10) ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
#
#list_of_multiples(17, 6) ➞ [17, 34, 51, 68, 85, 102]
#Notes


num = int(input())
length = int(input())
liste = list()
#liste =[*range(1,length+1)]
for i in range(1,length+1):	    
    liste.append(num*i)
print(liste)


def list_of_multiples (num, length):
	return [i*num for i in range(1,length+1)]


def list_of_multiples (num, length):
	return list(range(num, num*length+1, num))


def list_of_multiples (num, length):
	return [(n + 1) * num for n in range(length)]



def list_of_multiples (num, length):
	factor_number = 1
	factors = []
	while factor_number <= length:
		factors.append(factor_number * num)
		factor_number += 1
	return factors





def list_of_multiples (num, length):
	lst = []
	for i in range(length):
		lst.append(num+i*num)
	return lst





def list_of_multiples (num, length):
	y = 0
	b = []
	for x in range(length):
		y = y + num
		b.append(y)
	return b






