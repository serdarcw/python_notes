Two Distinct Elements
In each input list, every number repeats at least once, except for two.

Write a function that returns the two unique numbers.

Examples
returnUnique([1, 9, 8, 8, 7, 6, 1, 6]) ➞ [9, 7]

returnUnique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]) ➞ [2, 1]

returnUnique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]) ➞ [5, 6]




def return_unique(lst):
  return [i for i in lst if lst.count(i)==1]



def return_unique(lst):
	result = []
	for char in lst:
		if lst.count(char) < 2:
			result.append(char)
	return result




    def return_unique(lst):
		return [i for i in lst if lst.count(i)==1]



import collections
def return_unique(lst):
	dictionary = collections.OrderedDict()
	mylist = []
	for i in range (len(lst)):
		if str(lst[i]) not in dictionary:
			dictionary[str(lst[i])] = 1
		else:
			dictionary[str(lst[i])] += 1
	for keys,values in dictionary.items():
			if (values==1):
				mylist.append(int(keys))
	return (mylist)





    from collections import Counter

def return_unique(lst):
	c = Counter(lst)
	lst = [n for n in lst if c[n] == 1]
	return lst


def return_unique(lst):
	liste =list()
	for i in lst:
		if lst.count(i)==1:
			liste.append(i)
	return liste