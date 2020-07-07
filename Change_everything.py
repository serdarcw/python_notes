Create a function that changes all the elements in a list as follows:

Add 1 to all even integers, nothing to odd integers.
Concatenates "!" to all strings and capitalises them.
Changes all boolean values to its opposite.
Examples
change_types(["a", 12, True]) ➞ ["A!", 13, False]

change_types([13, "13", "12", "twelve"]) ➞ [13, "13!", "12!", "Twelve!"]

change_types([False, "False", "true"]) ➞ [True, "False!", "True!"]
Notes
There won't be any float values.
You won't get strings with both numbers and letters in them.
Although the task may be easy, try keeping your code as clean and as readable as possible!




	res = [13, "13", "12", "twelve"]
	for i in res:
		if type(i) == int:
			res.append(i if i%2 else i+1)
		elif type(i) == str:
			res.append(i.title() + '!')
		else:
			res.append(not i)
	print(res)






res = [13, "13", "12", "twelve"]
for i, j in enumerate(res):
	if type(j) is int and j % 2 == 0:
		lst[i] += 1
	elif type(j) is str:
		lst[i] = lst[i].capitalize() + '!'
	elif type(j) is bool:
		lst[i] = not lst[i]
return lst







A = ["a", 12, True, 13]
list = []
for i in A:
    if type(i)==str:
        i = i.swapcase()+"!"
        #i = i+"!" 
        list.append(i)
    elif i%2 == 0:
        i += 1
        list.append(i)
    elif i == True:
        i = (not i)
        list.append(i)
    else:
        list.append(i)
print(list)