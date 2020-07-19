https://edabit.com/challenge/KQe5w8AdSLbweW8ck

Oddly or Evenly Positioned
Create a function that returns the characters from a list or string r on odd or even positions, depending on the specifier s. The specifier will be "odd" for items on odd positions (1, 3, 5, ...) and "even" for items on even positions (2, 4, 6, ...).

Examples
char_at_pos([2, 4, 6, 8, 10], "even") ➞ [4, 8]
# 4 & 8 occupy the 2nd & 4th positions

char_at_pos("EDABIT", "odd") ➞ "EAI"
# "E", "A" and "I" occupy the 1st, 3rd and 5th positions

char_at_pos(["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "odd") ➞ ["A", "B", "T", "A", "I", "Y"]
Notes
Lists are zero-indexed, so, index+1 = position or position-1 = index.
(Optional) Try solving this challenge in a single-line lambda function.
A more advanced version of this challenge can be found here.


r, s ="EDABIT", "odd"

if s[0]=='e': print(r[1::2])
else: print(r[0::2])


char_at_pos = lambda r, s: r[(s=='even')::2]


def char_at_pos(r, s):
	if s=="even": return r[1::2]
	return r[0::2]


