
https://edabit.com/challenge/DG2HLRqxFXxbaEDX4

Return Only the Integer
Write a function that takes a list of elements and returns only the integers.

Examples
return_only_integer([9, 2, "space", "car", "lion", 16]) ➞ [9, 2, 16]

return_only_integer(["hello", 81, "basketball", 123, "fox"]) ➞ [81, 123]

return_only_integer([10, "121", 56, 20, "car", 3, "lion"]) ➞ [10, 56, 20, 3]

return_only_integer(["String",  True,  3.3,  1]) ➞ [1]


def return_only_integer(lst):
	return [i for i in lst if type(i)==int]



def return_only_integer(lst):
	lst2 = []
	for x in lst:
		if type(x) == int:
			lst2.append(x)
	return lst2




def return_only_integer(lst):
	newLst = []
	for i in range(len(lst)):
		if (type(lst[i]) == int):
			newLst.append(lst[i])
	return newLst


def return_only_integer(lst):
    result = []

    for i in range(0, len(lst)):
        if type(lst[i]) == int:
            result.append(lst[i])

    return result