A=[20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]

Find the Odd Integer
Create a function that takes a list and finds the integer which appears an odd number of times.

Examples
find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) ➞ -1

find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) ➞ 5

find_odd([10]) ➞ 10
Notes
There will always only be one integer that appears an odd number of times.



for i in lst:
    if lst.count(i)%2==1:
		print(i)

def find_odd(lst):
  for num in lst:
    if lst.count(num) % 2:
      return num

def find_odd(lst):
  return [x for x in set(lst) if lst.count(x)%2!=0][0]



def find_odd(lst):
  s = set(lst)
  for i in s:
    if lst.count(i) % 2 == 1: 
      return i



def find_odd(lst):
	return [num for num in lst if lst.count(num) % 2][0]



def find_odd(lst):
	for i in lst:
		if lst.count(i)%2==1: return i