https://edabit.com/challenge/zqMREZ2MQd9M5jNfM

Is the Number Symmetrical?
Create a function that takes a number as an argument and returns True or False depending on whether the number is symmetrical or not. A number is symmetrical when it is the same as its reverse.

Examples
is_symmetrical(7227) ➞ True

is_symmetrical(12567) ➞ False

is_symmetrical(44444444) ➞ True

is_symmetrical(9939) ➞ False

is_symmetrical(1112111) ➞ True



def is_symmetrical(num):
	return str(num)[::-1]==str(num)



def is_symmetrical(num):
    x = list(str(num))
    y = list(reversed(str(num)))
    if x != y:
        return False
    else:
        return True

def is_symmetrical(a):
    a = str(a)
    e = ''.join(reversed(a))
    if a == e:
        return True
    return False



