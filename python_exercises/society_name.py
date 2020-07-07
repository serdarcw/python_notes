
#verilen sayının faktöriyelini hesaplama...

def factorial(n):
  return n*factorial(n-1) if n>1 else 1


def factorial(Z):
  total = 1
  for i in range(1, Z+1):
      total *= i
  return total





def factorial(Z):
	if Z == 0:
		return 1
	elif Z == 1:
		return 1
	elif Z > 1:
		return Z * factorial(Z-1)
	else:
		return None

def factorial(Z):
  n = 1
  if int(Z) > 0:
    for i in range(1,int(Z)+1):
      n = n*i
    return n
  else:
    return 1



def factorial(Z):
	if Z == 0:
		return 1
	prod = 1
	for i in range(1,Z+1):
		prod*=i
	return prod




def factorial(n):
	if n==0: return 1
	return n*factorial(n-1)






def factorial(Z):
	return 1 if Z <= 1 else Z*factorial(Z-1)





def factorial(Z):
	r=1
	def rf(num):
		nonlocal r
		if num==0:
			return r
		else:
			r=r*num
			num=num-1
			return rf(num)
	return rf(Z)
