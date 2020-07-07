https://edabit.com/challenge/7NCfAsF2Y4wamHvHx


Zipping Up a List
Two lists are part of the same zipper if the ending is identical. The identical section can be thought of as being "zipped-up". Below, [2, 2, 4] is "zipped-up".

List 1: [3, 5, 8, 9, 2, 2, 4]
List 2: [1, 7, 2, 2, 4]
Create a function that takes in two lists. Return False if none of the list is "zipped." Return True if the lists are identical. Otherwise, return a list with the first index in each list where the zipper diverges.

To illustrate:

zipper([3, 5, 8, 9, 2, 2, 4], [1, 7, 2, 2, 4]) ➞ [3, 1]
# Zipper 1: 9 (index-3) is first element to diverge.
# Zipper 2: 7 (index-1) is first element to diverge.
Examples
zipper([5, 5, 7, 8, 9, 1, 2], [3, 2, 1, 1, 6, 6, 6, 6, 1, 2]) ➞ [4, 7]

zipper([5, 4, 3, 2, 6], [6, 4, 3, 2, 6]) ➞ [0, 0]

zipper([5, 4, 3, 2, 7], [6, 4, 3, 2, 6]) ➞ False

zipper([5, 4, 3, 2, 6], [5, 4, 3, 2, 6]) ➞ True
Notes
Use zero-indexing for the lists.



A=[5, 5, 7, 8, 9, 1, 2]
B=[3, 2, 1, 1, 6, 6, 6, 6, 1, 2]
m=len(A)
k=min(len(A),len(B))
for i in range(1,k+1):
    if A[-1]==B[-1]:
        del A[-1]
        del B[-1]
if len(A)==0: print(True)
elif len(A)==m and len(B)==m: print(False)
else: print([len(A)-1,len(B)-1])




def zipper(lst1, lst2):
	if lst1==lst2: return True
	elif lst1[-1]!=lst2[-1]: return False
	for i in range(2, len(lst1)+1):
		if lst1[-i]!= lst2[-i]:
			return [len(lst1)-i, len(lst2)-i]



def zipper(lst1, lst2):
	if lst1 == lst2: return True
	tmp = lst2[::-1]
	for idx, val in enumerate(lst1[::-1]):
		if val != tmp[idx]:
			if not idx:
				return idx
			return [len(lst1[idx:])-1, len(tmp[idx:])-1]


def zipper(lst1, lst2):
	if lst1 == lst2:
		return True
	else:
		t1 = lst1[::-1]
		t2 = lst2[::-1]
		i = 0
		while t1[i] == t2[i]:
			i += 1
		l1 = len(lst1)
		l2 = len(lst2)
		x1 = l1-i-1
		x2 = l2-i-1
		if i == 0:
			return False
		else:
			return [x1,x2]



def zipper(lst1, lst2):
	lst1=lst1[::-1]
	lst2=lst2[::-1]
	if lst1==lst2: return True
	for i in range(min(len(lst1),len(lst2))):
		if lst1[i]!=lst2[i]:
			if i==0: return False
			else:
				ind=i+1
				break
	lst1=lst1[::-1]
	lst2=lst2[::-1]
	return [len(lst1)-ind,len(lst2)-ind]





def zipper(lst1, lst2):
	if lst1 == lst2:
		return True
	len_check = len(lst1)
	while lst1[-1] == lst2[-1]:
		lst1.pop()
		lst2.pop()
	if len(lst1) == len_check:
		return False
	return [len(lst1) - 1, len(lst2) - 1]




def zipper(lst1, lst2):
	if lst1 == lst2: return True
	if lst1[-1] != lst2[-1]: return False
	for i in range(-1, -min(len(lst1), len(lst2))-1, -1):
		if lst1[i] != lst2[i]: return [len(lst1)+i,len(lst2)+i]
