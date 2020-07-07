https://edabit.com/challenge/gr4ihixfTaoEmZiin

Add the Index
Given a list of numbers, create a function which returns the list but with each element's index in the list added to itself. This means you add 0 to the number at index 0, add 1 to the number at index 1, etc...

Examples
add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]

add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9]

add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]
Notes
You'll only get numbers in the list.

def add_indexes(lst):
	return [i+n for i,n in enumerate(lst)]


def add_indexes(lst):
  for i in range(0,len(lst)):
    lst[i]=lst[i]+i
  return lst



def add_indexes(lst):
	a = []
	for index,value in enumerate(lst):
		a.append(index+value)
	return a


def add_indexes(lst):
	n = 0
	new_lst = []
	while n < len(lst):
		new_lst.append(lst[n] + n)
		n += 1
	return new_lst
