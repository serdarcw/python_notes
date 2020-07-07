https://edabit.com/challenge/GaXXfmpM72yCHag9T



Which Number Is Not like the Others?
Create a function that takes a list of numbers and return the number that's unique.

Examples
unique([3, 3, 3, 7, 3, 3]) ➞ 7

unique([0, 0, 0.77, 0, 0]) ➞ 0.77

unique([0, 1, 1, 1, 1, 1, 1, 1]) ➞ 0
Notes
Test cases will always have exactly one unique number while all others are the same.


def unique(lst):
	return [i for i in lst if lst.count(i)==1][0]


def unique(lst):
    d = {}
    for x in lst:
        d[x] = d.get(x,0)+1
    for k,v in d.items():
        if v == 1:
            return k



def unique(lst):
	for i in lst:
		if lst.count(i) <= 1:
			return i


def unique(lst):
	for i in lst:
		if lst.count(i) == 1:
			return i
