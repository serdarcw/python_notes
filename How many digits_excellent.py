How Many Digits between 1 and N
Imagine you took all the numbers between 0 and n and concatenated them together into a long string. How many digits are there between 0 and n? Write a function that can calculate this.

There are 0 digits between 0 and 1, there are 9 digits between 0 and 10 and there are 189 digits between 0 and 100.

Examples
digits(1) ➞ 0

digits(10) ➞ 9

digits(100) ➞ 189

digits(2020) ➞ 6969
Notes
The numbers are going to be rather big so creating that string won't be practical.



def digits(number):
	sum = 0
	if 1<number<10:
		return number
	elif number ==1:
		return 0
	else:
		A = list(str(number))[::-1]
		for i in range(len(A)-1):
			sum +=((10**(i+1))-(10**i))*(i+1)
		B = int("".join(A[:-1][::-1]))
		C = int(A[-1])
		sum += ((C-1)*len(A)*(10**(len(A)-1)))+(B*(i+2))
		return sum



def digits(number):
  l = len(str(number))
  return sum([9*(10**x)*(x+1) for x in range(l-1)])+(number-10**(l-1))*l




def digits(n):
    if n == 1: return 0
    calcdigs = 0
    s = str(n)
    l = len(s)
    ones = "1"*l
   
    for i in range(0,l):
        d = int(s[i])
        p = l-1-i
        calcdigs += l*d*10**p
        
    return calcdigs-int(ones)




def digits(n):
	p10, ln, res = 10, 1, 0
	while p10 < n:
		res += ln*(p10 - p10//10)
		ln += 1
		p10 *=10
	return res + ln*(n - p10//10)





def digits(num):
	s = 0
	k = 1
	occ = 9
	n = 10
	while num >= n:
		s += k*occ
		k += 1
		occ *= 10
		n *= 10
	return s + (num-n//10)*k






def digits(number):
    n, count_zeros = number - 1, 0
    len_str_n = len(str(n))
    for i in range(1, len_str_n):
        count_zeros += 9 * 10 ** (i - 1) * (len_str_n - i)
    return n * len_str_n - count_zeros




def digits(number):
    list = []
    for i in range(0, number):
        list.append(str(i))
    return len(''.join(list)) - 1





def digits(number):
    exp=dig=0
    while number>0:
        _number=number
        _dig=dig
        x=9*10**exp
        number-=x
        dig+=x*(exp+1)
        exp+=1
    return _dig+(_number-1)*exp





def digits(number):
  return 0 if number<2 else len("".join(str(i) for i in range(1,number)))