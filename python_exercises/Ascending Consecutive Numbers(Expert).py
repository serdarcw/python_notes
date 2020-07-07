https://edabit.com/challenge/9iLhKgqZn5exBrmWm

Ascending Consecutive Numbers
Write a function that returns True if a string consists of ascending AND consecutive numbers.

Examples
ascending("232425") ➞ True
# Consecutive numbers 23, 24, 25

ascending("2324256") ➞ False
# No matter how this string is divided, the numbers are not consecutive.

ascending("444445") ➞ True
# Consecutive numbers 444 and 445.
Notes
A number can consist of any number of digits, so long as the numbers are adjacent to each other, and the string has at least two of them.


def ascending(txt):
	for i in range(1,len(txt)//2+1):
		k,B,C=0,[],[]
		for j in range(len(txt)):
			if len(txt[k:k+i])==i and len(txt[k+i:k+2*i])==i:
				C.append([txt[k:k+i],txt[k+i:k+2*i]])
				B.append(int(txt[k:k+i])+1==int(txt[k+i:k+2*i]))
				k=k+i
		if all(B) and C[-1][-1][-1]==txt[-1]:
			return True
			break
	else:
		return False



def ascending(txt):
	for n in range(1, len(txt)//2 + 1):
		groups = [txt[i:i+n] for i in range(0, len(txt), n)]
		if all(int(a) + 1 == int(b) for a, b in zip(groups, groups[1:])):
			return True
	return False


def ascending(txt):
	print(txt)
	for i in range(1,len(txt)//2+1):
		temp = []
		for x in range(0,len(txt),i):
			temp.append(int(txt[x:x+i]))
		print(temp)
		if check(temp):
			return True
	return False

def check(lst):
	for i in range(1,len(lst)):
		if lst[i] != lst[i-1]+1:
			return False
	return True


def ascending(txt):
    for L in range(len(txt)//2+1):
        if L != 0:
            last = int(txt[0:L])-1
            go = "yes"
            pos = 0
            while pos < len(txt):
                inst = txt[pos:pos+L]
                pos = pos+L
                if inst == "9"*L:
                    L += 1
                if int(inst) != int(last)+1:
                    go = "no"
                last = inst
            if go == "yes":
                return bool(1)   
    return bool(0)