#https://edabit.com/challenge/rSa8y4gxJtBqbMrPW
#
#
#
#LCM of Two Numbers
#Write a function that returns the least common multiple (LCM) of two integers.
#
#Examples
#lcm(9, 18) ➞ 18
#
#lcm(8, 5) ➞ 40
#
#lcm(17, 11) ➞ 187
#Notes
#Both values will be positive.
#The LCM is the smallest integer that divides both numbers such that the remainder is zero.




#import time
#start = time.time()
#
#n1=3368
#n2=1509
#mindiv = max(n1, n2)
#while mindiv % n1 != 0 or mindiv % n2 != 0:
#    mindiv += 1
#print(mindiv)
#
#end  = time.time()
#print(end-start) 







#A=33
#B=15
#C=min([i for i in range(min(A,B),A*B+1) if i%A==0 and i%B==0 ])
#print(C)







#A=187
#B=209
#D=[]
#for i in range(max(A,B),A*B+1):
#    if i%A==0 and i%B==0:
#        D.append(i)
#print(min(D))
#
#
#
#
#
#def lcm(n1, n2):
#  n=max(n1,n2)
#  while n:
#    if n%n1==0 and n%n2==0:
#      return n
#    n+=max(n1,n2)
#
#
#
#def lcm(n1, n2):
#	if n1 > n2:
#		z = n1
#	else:
#		z = n2
#	while(True):
#		if((z % n1 == 0) and (z % n2 == 0)):
#			lcm = z
#			break
#		z += 1
#	return lcm
#
#


#def lcm(n1, n2):
#	for i in range(min([n1, n2]), n1 * n2, min([n1, n2])):
#		if i % max([n1, n2]) == 0:
#			return i
#	else:
#		return n1 * n2
#
#
#
#
#def lcm(n1, n2):
#	if n1%n2==0 or n2%n1==0:
#		return max(n1,n2)  
#	else:
#		return n1*n2
#
#
#
#
#
#def lcm(n1, n2):
#	mult = n1
#	for i in range(1,n2+1) :
#		mult = n1*i
#		if mult%n2==0 :
#			return mult
#	return 0




#testlist = [187,209]
#lcm = 1
#num = 2
#while num <= max(testlist):
#    if not (testlist[0] % num):
#        lcm *= num
#        testlist[0] = testlist[0] // num
#        if not (testlist[1] % num):
#            testlist[1]  = testlist[1] // num
#    elif not (testlist[1] % num):
#            lcm *= num
#            testlist[1] = testlist[1] // num
#    else:
#        num += 1
#print(lcm)

