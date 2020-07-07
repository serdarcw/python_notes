Is the Number a Repdigit
A repdigit is a positive number composed out of the same digit.

Create a function that takes an integer and returns whether it's a repdigit or not.

Examples
is_repdigit(66) ➞ True

is_repdigit(0) ➞ True

is_repdigit(-11) ➞ False
Notes
The number 0 should return True (even though it's not a positive number).
Check the Resources tab for more info on repdigits.





def is_repdigit(num):
  return len(set(str(num))) == 1





  def is_repdigit(num):
    b= set(str(num))
    if len(b)==1: return True
    else: return False




def is_repdigit(num):
	if num == 0 :
		return True
	n = str(num)
	for i in n:
		if n.count(i) == len(n):
			return True
		else:
			return False



def is_repdigit(num):
	if num<0: return False
	return len(set(str(num)))==1




def is_repdigit(num):
  return num > 0 and str(num).count(str(num)[0]) == len(str(num))




def is_repdigit(num):
	if num < 0:
		return False
	return sum([1 for i in set(str(num))]) == 1




def is_repdigit(num):
    for i in str(num):
        if i != str(num)[0]:
            return False
    return True





    def is_repdigit(num):
    if num<0: return False
    a = [int(i) for i in str(num)]
    return len(set(a))==1