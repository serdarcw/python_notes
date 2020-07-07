https://edabit.com/challenge/fRZMqCpyxpSgmriQ6

Sort the String
Create a function that takes a string consisting of lowercase letters, uppercase letters and numbers and returns the string sorted in the same way as the examples below.

Examples
sorting("eA2a1E") ➞ "aAeE12"

sorting("Re4r") ➞ "erR4"

sorting("6jnM31Q") ➞ "jMnQ136"




var = "2lZduOg1jB8SPXf5rakC37wIE094Qvm6Tnyh"
low=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num=[0,1,2,3,4,5,6,7,8,9]
rank=[]
for i in low:
    if i in var:
        rank.append(i)
    if i.upper() in var:
        rank.append(i.upper())
rank.extend([str(i) for i in num if str(i) in var])
print(''.join(rank))



def sorting(s):
    new_key = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789'
    return ''.join(sorted(s, key=new_key.index))

d=[]
for x in range(97,123):x=chr(x);d+=[x,x.upper()]
d+=['0','1','2','3','4','5','6','7','8','9']
def sorting(s,d=d):
	return ''.join(sorted(s,key=d.index))


def sorting(s):
	for k in (str.isupper, str.lower, str.isdigit):
		s = sorted(s, key=k)
	return "".join(s)











