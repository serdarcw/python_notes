#https://edabit.com/challenge/T4q8P8cxvBtaLPW4q


A=1029
C=str(A)
B=[]
D=[]
E=[C[i:i+k] for i in range(0,len(C)) for k in range(1,len(C)+1-i) ]
print(E)		
	
for t in E:
	if int(t[0])==0 or int(t)==1:
		continue
	if int(t)==2:
		D.append(2)
	else:
		count=0
		for j in range(2,int(t)):
			if int(t) % j == 0:
				count+=1
		if count<1: 
			D.append(int(t))
D.sort()
print(D)




#def extract_primes(num):
#	# get list of primes between 2 and num
#	primes = set(range(2,num+1))
#	for i in range(2,int(num**0.5 + 1)):
#		primes -= set(range(i*2,num+1,i))
#	# get list of numbers to check if prime
#	num_str = str(num)
#	chk_nums = [int(num_str[j:j+i+1]) for i in range(len(num_str)) for j in range(len(num_str)-i) if num_str[j] != "0"]
#	return sorted([n for n in chk_nums if n in primes])
#
#
#
#
#	def extract_primes(num):
#  num, res = str(num), []
#  p = lambda x: not any(not x%i for i in range(2,int(x**0.5)+1))
#  for i in range(len(num)):
#    for j in range(i+1,len(num)+1):
#      if num[i:j] not in ['0','1'] and not num[i:j].startswith('0'):
#        res.append(int(num[i:j]))
#  res = sorted([i for i in res if p(i)])
#  return res
#
#
#
#def is_prime(n):
#    if n < 2:
#        return False
#    for i in range(2, int(n**0.5) + 1):
#        if not n%i:
#            return False
#    return True
#
#def extract_primes(n):
#    s = str(n)
#    
#    primes = []
#    for i in range(len(s) + 1):
#        for j in range(i + 1, len(s) + 1):
#            group = s[i:j]
#            if group[0] != '0' and is_prime(int(group)):
#                primes.append(int(group))
#    
#    primes.sort()
#    return primes
#
#
#
#
#
#	def extract_primes(num):
#	C=str(num)
#	B=[]
#	m=len(C)
#	D=[]
#	for k in range(1,len(C)+1):
#		for i in range(0,m):
#			B.append(C[i:i+k])
#		m=m-1
#	for t in B:
#		if int(t[0])==0 or int(t)==1:
#			continue
#		if int(t)==2:
#			D.append(2)
#		else:
#			count=0
#			for j in range(2,int(t)):
#				if int(t) % j == 0:
#					count+=1
#			if count<1: 
#				D.append(int(t))
#	D.sort()
#	return D
#
#
#
#
#	def extract_primes(num):
#	num = str(num)
#	ans = []
#	for i in range(len(num)):
#		for x in range(i+1,len(num)+1):
#			print(num[i:x])
#			if num[i] != '0' and is_prime(int(num[i:x])):
#				ans.append(int(num[i:x]))
#	return sorted(ans)
#def is_prime(n):
#	for i in range(2,n):
#		if n%i == 0:
#			return False
#	return n != 1 and n != 0
#
#
#
#
#			a=str(num)
#		p=[]
#		b=[a[i:i+1+j]  for j in range(len(a)) for i in range(len(a)-j)]
#		for i in b:
#				if i[0]!='0':   
#						if int(i)>=2:
#								for j in range(2,int(i)):
#										if (int(i)%j)==0:
#												break
#								else:
#										p.append(int(i))
#		return sorted(p)