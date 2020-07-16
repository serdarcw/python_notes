https://edabit.com/challenge/3Eia4oLLCcyyLN2L7

Remove Repeated Letters
Create a function which replaces all repeated letters in a word with single letters.

Examples
remove_repeats("aaabbbccc") ➞ "abc"

remove_repeats("bookkeeper") ➞ "bokeper"

remove_repeats("nananana") ➞ "nananana"
Notes
N/A


def remove_repeats(s):
	B=[s[0]]
	for i in range(1,len(s)):
		if s[i]!=B[-1]: B.append(s[i])
	return ''.join(B)



import re
def remove_repeats(s):
	return re.sub(r'(\w)\1+',r'\1', s)


def remove_repeats(s):
	s_final = ''
	for i in range(len(s)-1):
		if s[i] == s[i+1]:
			continue
		else:
			s_final += s[i]
	return s_final+s[-1]

def remove_repeats(s):
	no_rep = s[0]
	for i in s[1:]:
		if i != no_rep[-1]:
			no_rep += i
	return no_rep