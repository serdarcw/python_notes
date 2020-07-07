
https://edabit.com/challenge/D6XfxhRobdQvbKX4v


First Before Second Letter
You are given three inputs: a string, one letter, and a second letter.

Write a function that returns True if every instance of the first letter occurs before every instance of the second letter.

Examples
first_before_second("a rabbit jumps joyfully", "a", "j") ➞ True
# Every instance of "a" occurs before every instance of "j".

first_before_second("knaves knew about waterfalls", "k", "w") ➞  True

first_before_second("happy birthday", "a", "y") ➞ False
# The "a" in "birthday" occurs after the "y" in "happy".

first_before_second("precarious kangaroos", "k", "a") ➞ False
Notes
All strings will be in lower case.
All strings will contain the first and second letters at least once.


A= "knaves knew about waterfalls"
print(len(A)-1-A[::-1].index('a')>A.index('k'))




print(s.rindex(first) < s.index(second))



def first_before_second(s, first, second):
	fInd = max([i for i in range(len(s)) if s[i] == first])
	sInd = min([i for i in range(len(s)) if s[i] == second])




def first_before_second(s, first, second):
	if first in s[s.index(second):]:
		return False
	return True