
https://edabit.com/challenge/NtsqbRPqtPYhR8tJe

3D Visual Block Sequence
A block sequence in three dimensions. We can write a formula for this one:

Sequence Step 1 - 5

Create a function that takes a number (step) as an argument and returns the amount of blocks in that step.

Examples
blocks(1) ➞ 5

blocks(5) ➞ 39

blocks(2) ➞ 12
Notes
Step 0 obviously has to return 0.
The input is always a positive integer.
Check the Resources tab for a video on finding quadratic sequences.

find the formula of Quadratic sequence:
https://www.youtube.com/watch?v=FfCq7bGAFoY


def blocks(step):
	if step<=0: return 0
	else: return int((1/2)*(step**2+11*step)-1)

def blocks(step):
	return 5*step + sum(range(2,step+1))

def blocks(n):
	return 0 if n < 1 else 6*n - 1 + (n-1) * n//2


def blocks(step):
	if step == 0:
		return 0
	if step == 1:
		return 5
	return 6 + (step - 1) + blocks(step - 1)