https://edabit.com/challenge/zZyeau2MYcEc8Fdtk

Round to Closest N
Creates a function that takes two integers, num and n, and returns an integer which is divisible by n and is the closest to num. If there are two numbers equidistant from num and divisible by n, select the larger one.

Examples
round_number(33, 25) ➞ 25

round_number(46, 7) ➞ 49

round_number(133, 14) ➞ 140
Notes
n will always be a positive number.


def round_number(num, n):
    for i in range(n):
        if (num+i)%n==0: return num+i
        if (num-i)%n==0: return num-i






def round_number(num, n):
	down, up = num%n, -num%n
	return num - down if down < up else num + up