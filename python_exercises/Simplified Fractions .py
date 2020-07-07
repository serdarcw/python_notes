https://edabit.com/challenge/vQgmyjcjMoMu9YGGW


A="40/20"
B=A.split("/")
k= min(B)
A=[[str(int(B[0])//i), str(int(B[1])//i)] for i in range(1,int(k)+1) if int(B[0])%i==0 and int(B[1])%i==0]
print(A)
if A[-1][-1]=='1':
    print(A[-1][0])
else:
    print('/'.join(A[-1]))




def simplify(txt):
	a, b = map(int, txt.split('/'))
	if a % b == 0:
		return str(a//b)
	for i in range(min(a, b), 1, -1):
		if a % i == 0 and b % i == 0:
			return '{}/{}'.format(a//i, b//i)
	return txt



def simplify(txt):
	fst, snd = txt.split('/')
	fst, snd = int(fst), int(snd)
	
	if fst % snd == 0:
		return str(fst // snd)
		
	g = gcd(fst, snd)
	return str(fst // g) + '/' + str(snd // g)

def gcd(x, y):
	while (y):
		x, y = y, x % y
	
	return x