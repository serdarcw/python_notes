https://edabit.com/challenge/kozqCJFi4de2JnR26

Fibonacci String

A Fibonacci string is a precedence of the Fibonacci series. It works with any two characters of the English alphabet (as opposed to the numbers 0 and 1 in the Fibonacci series) as the initial items and concatenates them together as it progresses in a similar fashion as the Fibonacci series.

Examples
fib_str(3, ["j", "h"]) ➞ "j, h, hj"

fib_str(5, ["e", "a"]) ➞ "e, a, ae, aea, aeaae"

fib_str(6, ["n", "k"]) ➞ "n, k, kn, knk, knkkn, knkknknk"
Notes
All values for n will be at least 2.
A recursive version of the challenge can be found here.


n = 5
txt = ['e','a']

for i in range(n-2):
    txt.append(txt[i+1]+txt[i])
print(', '.join(txt))



def fib_str(n, str):
	for _ in range(2,n):
		str.append(str[-1]+str[-2])
	return ", ".join(str)


def fib_str(n, st):
    while len(st) < n:
        st.append(st[-1] + st[-2])
    return ', '.join(x for x in st)


def fib_str(n, f):
  for i in range(2, n):
    f += [f[i-1] + f[i-2]]
  return ', '.join(f)