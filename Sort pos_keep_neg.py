
https://edabit.com/challenge/6brSyFwWnb9Msu7kX

Sort Positives, Keep Negatives
Write a function that sorts the positive numbers in ascending order, and keeps the negative numbers untouched.

Examples
pos_neg_sort([6, 3, -2, 5, -8, 2, -2]) ➞ [2, 3, -2, 5, -8, 6, -2]

pos_neg_sort([6, 5, 4, -1, 3, 2, -1, 1]) ➞ [1, 2, 3, -1, 4, 5, -1, 6]

pos_neg_sort([-5, -5, -5, -5, 7, -5]) ➞ [-5, -5, -5, -5, 7, -5]

pos_neg_sort([]) ➞ []
Notes
If given an empty list, you should return an empty list.
Integers will always be either positive or negative (0 isn't included in the tests).

#A = [6, 3, -2, 5, -8, 2, -2]
#B=[]
#for i in A:
#	if i>0: B.append(i)
#B.sort()
#j=0
#for i in range(len(A)):
#	if A[i]>0:
#		A[i]=B[j]
#		j+=1
#print(A)


#lst = [6, 3, -2, 5, -8, 2, -2]
#pos = sorted([i for i in lst if i > 0])
#  
#for i in range(len(lst)):
#	if lst[i] > 0:
#		lst[i] = pos.pop(0)
#      
#print(lst)



#lst = [6, 3, -2, 5, -8, 2, -2]
#pos = sorted([i for i in lst if i > 0])
#it = 0
#for i in range(len(lst)):
#	if lst[i] > 0:
#		lst[i] = pos[it]
#		it += 1
#print(lst)




#lst = [6, 3, -2, 5, -8, 2, -2]
#pos = iter(sorted([i for i in lst if i >= 0]))
#print([i if i < 0 else next(pos) for i in lst])







#lst = [6, 3, -2, 5, -8, 2, -2]
#k = [i for i in range(len(lst)) if lst[i] > 0]
#y = sorted([lst[i] for i in k])
#r, v = [], 0
#for i in range(len(lst)):
#	if i in k:
#		r.append(y[v])
#		v = v + 1
#	else:
#		r.append(lst[i])
#print(r)







