Equality of 3 Values
Create a function that takes three integer arguments (a, b, c) and returns the amount of integers which are of equal value.

Examples
equal(3, 4, 3) ➞ 2

equal(1, 1, 1) ➞ 3

equal(3, 4, 1) ➞ 0 
Notes
Your function must return 0, 2 or 3.



def equal(a, b, c):
	uniq= set([a,b,c])
	if len(uniq)==3:
		return 0
	else:
		return (4 - len(uniq))



def equal(a, b, c):
    numbers = [a, b, c]
    res = numbers.count(max(numbers, key=numbers.count))
    return res if res > 1 else 0


t=len(set([a,b,c]))
  return   t!=3 and (4-t) or 0

  

def equal(a, b, c):
	return {3:0,2:2,1:3}[len({a,b,c})]



def equal(a, b, c):
	lst = [a,b,c]
	answer = max([ lst.count(x) for x in [a,b,c] ])
	return answer if answer != 1 else 0


def equal(a, b, c):
	matches = 4 - len(set([a,b,c]))
	if matches == 1:
		matches = 0
	return matches




def equal(a, b, c):
    if len({a, b, c}) == 3:
        return 0
    return 4 - len({a, b, c})






def equal(a, b, c):
    if a == b and a == c:
        return 3
    elif a == b or a == c:
        return 2
    else:
        return 0






def equal(a, b, c):
	A = set([a,b,c])
	if len(A)==1:
		return 3
	elif len(A)==2:
		return 2
	else:
		return 0