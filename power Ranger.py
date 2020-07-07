
https://edabit.com/challenge/abdsaD6gwjgAgevsG

Power Ranger
Create a function that takes in n, a, b and returns the number of values raised to the nth power that lie in the range [a, b], inclusive.

Examples
power_ranger(2, 49, 65) ➞ 2
# 2 squares (n^2) lie between 48 and 65, 49 (7^2) and 64 (8^2)

power_ranger(3, 1, 27) ➞ 3
# 3 cubes (n^3) lie between 1 and 27, 1 (1^3), 8 (2^3) and 27 (3^3)

power_ranger(10, 1, 5) ➞ 1
# 1 value raised to the 10th power lies between 1 and 5, 1 (1^10)

power_ranger(5, 31, 33) ➞ 1

power_ranger(4, 250, 1300) ➞ 3
Notes
Remember that the range is inclusive.
a < b will always be true.




a,b,c=2,49,65
import math
A=[]
A= [i if i**(1/a)-int(i**(1/a))==0 for i in range(b,c+1)]
#for i in range(b,c+1):
#    if i**(1/a)-int(i**(1/a))==0:
#        A.append(i)
print(len(A)




def power_ranger(power, minimum, maximum):
	x = ((minimum-1)**(1/power))//1
	y = (maximum**(1/power))//1
	return y-x


def power_ranger(power, minimum, maximum):
	return len([c for c in range(maximum+1) if c**power>=minimum and c**power<=maximum and int(c)==c])




import math

def power_ranger(power, minimum, maximum):
	low = math.ceil(minimum**(1/power))
	high = math.ceil(maximum**(1/power))
	count = 0
	for i in range(low, high+1):
		if (minimum <= i**power <= maximum):
			count += 1
	return(count)



def power_ranger(power, minimum, maximum):
	total = 0
	for i in range(int(minimum**(1/power)), int(maximum**(1/power) + 1)):
		if minimum <= i**power <= maximum:
			total += 1
	return total




def power_ranger(power, minimum, maximum):
    import math
    l = list(range(minimum, maximum+1))
    x = []
    for i in l:
        v = i ** (1 / float(power))
        if math.floor(v) == math.ceil(v):
            x.append(v)
    return len(x)





def power_ranger(power, minimum, maximum):
	x = 0
	for num in range(0,maximum+1):
		if num ** power in range(minimum, maximum+1):
			x += 1
	return x