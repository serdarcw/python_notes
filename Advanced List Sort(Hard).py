https://edabit.com/challenge/6vSZmN66xhMRDX8YT

Advanced List Sort
Create a function that takes a list of numbers or strings and returns a list with the items from the original list stored into sublists. Items of the same value should be in the same sublist.

Examples
advanced_sort([2, 1, 2, 1]) ➞ [[2, 2], [1, 1]]

advanced_sort([5, 4, 5, 5, 4, 3]) ➞ [[5, 5, 5], [4, 4], [3]]

advanced_sort(["b", "a", "b", "a", "c"]) ➞ [["b", "b"], ["a", "a"], ["c"]]
Notes
The sublists should be returned in the order of each element's first appearance in the given list.

A=['c','c','b','c','b',1,1]
B, C=[], []
for i in A:
    if i not in B:
        B.append(i)
        k=A.count(i)
        if type(i)==str: C.append(list(k*[i]))
        else: C.append(k*[i])
print(C)


def advanced_sort(lst):
	return [[i] * lst.count(i) for i in sorted(set(lst), key=lst.index)]


def advanced_sort(lst):
	lst = [[i]*lst.count(i) for i in lst]
	ans = []
	for i in lst:
		if i not in ans:
			ans.append(i)
	return ans