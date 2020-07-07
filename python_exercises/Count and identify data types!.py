Count and identify data types!
Given a function that accepts unlimited arguments. Check and count how many data types are in those arguments. Finally return the total in a list. List order is [int, str, bool, list, tuple, dictionary]

Examples
count_datatypes(1, 45, "Hi", False) ➞ [2,1,1,0,0,0]

count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1) ➞ [3, 0, 0, 1, 1, 0]

count_datatypes("Hello", "Bye", True, True, False, {'1': 'One', '2': 'Two'}, [1, 3], {'Brayan': 18}, 25, 23) ➞ [2, 2, 3, 1, 0, 2]

count_datatypes(4, 21, ("ES", "EN"), ('a', 'b'), False, [1, 2, 3], [4, 5, 6]) ➞ [2, 0, 1, 2, 2, 0]
Notes
If no arguments are given return [0, 0, 0, 0, 0, 0]




def count_datatypes(*args):
    lst = [type(i) for i in args]
    return [lst.count(i) for i in (int, str, bool, list, tuple, dict)]



def count_datatypes(*args):
	types = [int, str, bool, list, tuple, dict]
	return [sum(type(i) is t for i in args) for t in types]



def count_datatypes(*args):
	t = {int:0, str:1, bool:2, list:3, tuple:4, dict:5}
	res = [0,0,0,0,0,0]
	for arg in args:
		res[t[type(arg)]] += 1
	return res



def count_datatypes(*args):
	A = [0,0,0,0,0,0]
	s = []
	for i in args:
		s.append(i)
	for i in s:
		if type(i)==int: A[0]+=1
		elif type(i)==str: A[1]+=1
		elif type(i)==bool:A[2]+=1
		elif type(i)==list: A[3]+=1
		elif type(i)==tuple: A[4]+=1
		elif type(i)==dict: A[5]+=1
	return A


    def count_datatypes(*args):
    ans = [0, 0, 0, 0, 0, 0]
    for arg in args:
        for i in range(6):
            if type(arg) == arg_types[i]:
                ans[i] += 1            
    return ans





from collections import Counter


def count_datatypes(*args):
	c = Counter(type(i) for i in args)
	types = [int, str, bool, list, tuple, dict]
	return [c[t] for t in types]