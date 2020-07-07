https://edabit.com/challenge/Rn3g3hokznLu8ZtDP

#String Incrementer
#Write a function which increments a string to create a new string.
#
#If the string ends with a number, the number should be incremented by 1.
#If the string doesn't end with a number, 1 should be added to the new string.
#If the number has leading zeros, the amount of digits should be considered.
#Examples
#increment_string("foo") ➞ "foo1"
#
#increment_string("foobar0009") ➞ "foobar0099"
#
#increment_string("foo099") ➞ "foo100"


A="foobar01002"
for i,n in enumerate(list(A)):
    if A[-1].isdigit()==False:
        print(A+'1')
        break
    if n.isdigit() and eval(n)!=0:
        K=A[:i]+str(eval(''.join(list(A)[i:]))+1)
        if len(K)!=len(A):
            print(A[:i-1]+str(eval(''.join(list(A)[i:]))+1))
        else:
            print(K)
        break


def increment_string(txt):
	tlen = len(txt)
	if txt[tlen-1] not in '1234567890' : 
		otxt = txt + '1'
		return otxt		
		exit()
	i = 1
	#find where the numbers stop
	while txt[tlen-i] in '1234567890' :
		i += 1
	#get the word portion
	wpor = txt[0:tlen-i+1]
	npor = txt[tlen-i+1:tlen]
	#increment the number portion
	npl = len(npor)
	npori = str(int(npor) + 1).zfill(npl)
	#assemble the return
	print(txt, "txt wpor", wpor, "wpor npor", npor, "npor i", i)
	return wpor + npori



    def increment_string(txt):
  if not txt[-1].isnumeric(): return txt + '1'
  i = 0
  for i in range(1, len(txt) + 1):
    if not txt[-i:].isnumeric(): break
  i -= 1
  string = txt[:-i]
  number = str(int(txt[-i:]) + 1)
  return string + '0' * max(len(txt) - len(number) - len(string), 0) + number


a = ""
s_yedek = s
while s_yedek[-1].isdigit():
	a = s_yedek[-1]+a
	s_yedek = s_yedek[:-1]
if a != "":
	sayi = int(a)+1
else: 
	sayi = 1
if len(a) >= len(str(sayi)):
	s = s[:-(len(str(sayi)))]+str(sayi)
elif a == "":
	s = s + str(sayi)
else:
	s = s[:len(a)]+str(sayi)
return s
