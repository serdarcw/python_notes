
https://edabit.com/challenge/PxxZprxCjDrzaTcLQ

Vowel to Vowel Links
Given a sentence as txt, return True if any two adjacent words have this property: One word ends with a vowel, while the word immediately after begins with a vowel.

Examples
vowel_links("a very large appliance") ➞ True

vowel_links("go to edabit") ➞ True

vowel_links("an open fire") ➞ False

vowel_links("a sudden applause") ➞ False
Notes
You can expect sentences in only lowercase.


A="a sudden applause"
B=A.split()
C=[]
print([True for i in range(len(B)-1) if B[i][-1] in 'aeiou' and B[i+1][0] in 'aeiou'])

import re
def vowel_links(txt):
	return bool(re.findall('[aeiou] [aeiou]', txt))



def vowel_links(txt):
	txt= txt.split()
	for i in range(len(txt) - 1):
		if txt[i][-1] in 'aeiou' and txt[i+1][0] in 'aeiou': return True
	return False



def vowel_links(txt):
    lov = 'aeiou'
    low = (txt + ' x').split()
    for i in range(len(low)-1):
        if low[i][-1] in lov and low[i+1][0] in lov:
            return True
    return False


def vowel_links(txt):
	txt = txt.split()
	return any(x[-1] in 'aeiou' and y[0] in 'aeiou' for x, y




