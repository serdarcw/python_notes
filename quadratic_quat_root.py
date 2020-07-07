def quadratic_equation(a, b, c):
	return ((b**2-4*a*c)**0.5-b)/2/a



def quadratic_equation(a, b, c):
	return int((-b + (b**2 - 4*a*c) ** 0.5) / (2*a))



import math
def quadratic_equation(a, b, c):
	return (-1 * b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)



def quadratic_equation(a, b, c):
	pluseval = ((b * -1) + ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
	minuseval = ((b * -1) - ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
	return pluseval if pluseval > 0 else minuseval



def quadratic_equation(a, b, c):
  bsq = b ** 2 # b squared
  tsqexp = bsq - ( 4 * a * c) #expression to be square rooted (b^2 - 4ac)
  sqdexp = tsqexp ** (1/2) # square rooted expression
  b = -1 * b # -b
  x = (b + sqdexp) / (2 * a) #-b + rooted expression
  y = (b - sqdexp) / (2 * a) #-b - rooted expression
  if x > y: # we only want the positive number
    return x
  else:
    return y


def quadratic_equation(a, b, c):
	import math
	d = math.sqrt(b**2 - 4*a*c)
	x1 = (-b+d)/(2*a)
	x2 = (-b-d)/(2*a)
	if x1>0:
		return x1
	else:
		return x2


