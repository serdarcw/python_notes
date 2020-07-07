
Combined Consecutive Sequence
Write a function that returns True if two lists, when combined, form a consecutive sequence.

Examples
consecutive_combo([7, 4, 5, 1], [2, 3, 6]) ➞ True

consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]) ➞ False

consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]) ➞ False

consecutive_combo([44, 46], [45]) ➞ True
Notes
The input lists will have unique values.
The input lists can be in any order.
A consecutive sequence is a sequence without any gaps in the integers, e.g. 1, 2, 3, 4, 5 is a consecutive sequence, but 1, 2, 4, 5 is not.





A=[7,4,5,1]
B=[2,3,6]
A.extend(B)
A.sort()
print(A==list(range(min(A),max(A)+1)))




def consecutive_combo(lst1, lst2):
	lst3 = lst1 + lst2
	return max(lst3) - min(lst3) == len(lst3) - 1





def consecutive_combo(lst1, lst2):
  lst = sorted(lst1+lst2)
  return all(lst[i]-lst[i-1]==1 for i in range(1,len(lst)))





  def consecutive_combo(lst1, lst2):
	tmp = lst1 + lst2
	return sorted(tmp) == list(range(min(tmp), max(tmp) + 1))




def consecutive_combo(lst1, lst2):
	lst1.extend(lst2)
	lst1.sort()
	return lst1==list(range(min(lst1),max(lst1)+1))





    