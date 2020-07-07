
https://edabit.com/challenge/o7u9hqTW5AY3SoZgT

A Subtle Switcheroo
Create a function which replaces all instances of "nts" with "nce" and vice versa if they are at the end of a word.

Examples
switcheroo("The elephants in France were chased by ants!") ➞ "The elephance in Frants were chased by ance!"

switcheroo("While he rants, I fall into a trance...") ➞ "While he rance, I fall into a trants..."

switcheroo("Bounced over the fence!") ➞ "Bounced over the fents!"
Notes
Empty strings should return just an empty string (see example #2).
Ignore punctuation and any instances where "nts" or "nce" are not at the end of a word (see example #3).

txt = ""
A=txt.split()
B=[]
if txt=='':
    print(txt)
for i in A:
    if i[-3:]=='nce' or (i[-4:-1]=='nce' and i[-1] in '/&%.,!;:)([]=?+#'):
        B.append(i.replace('nce','nts'))
    elif i[-3:]=='nts' or (i[-4:-1]=='nts' and i[-1] in '/&%.,!;:)([]=?+#'):
        B.append(i.replace('nts','nce'))
    else:
        B.append(i)
for i,n in enumerate(A[-1]):
    if n in '/&%.,!;:)([]=?+#':
        if A[-1][i-3:i]=='nce':
            B[-1]=(A[-1].replace('nce','nts'))
        elif A[-1][i-3:i]=='nts':
            B[-1]=A[-1].replace('nts','nce')
print(' '.join(B))




def switcheroo(txt):
	chars = [i for i in txt]
	for i in range(len(chars)+3):
		if chars[i:i+3] == [i for i in 'nts'] and chars[i+3] in ' ,.!?': 
			chars[i:i+3] = [i for i in 'nce']
		elif chars[i:i+3] == [i for i in 'nce'] and chars[i+3] in ' ,.!?': 
			chars[i:i+3] = [i for i in 'nts']
	return ''.join(chars)



def switcheroo(txt):
	txt = txt.split(" ")
	for i in range(len(txt)):
			w = "".join([c for c in txt[i] if c.isalpha()])
			if "nts" in w:
					if w[-3:] == "nts":
							txt[i] = txt[i].replace("nts", "nce")
			elif "nce" in w:
					if w[-3:] == "nce":
							txt[i] = txt[i].replace("nce", "nts")
	return " ".join(txt)


def switcheroo(txt):
	chars = [i for i in txt]
	for i in range(len(chars)+3):
		if chars[i:i+3] == [i for i in 'nts'] and chars[i+3] in ' ,.!?': 
			chars[i:i+3] = [i for i in 'nce']
		elif chars[i:i+3] == [i for i in 'nce'] and chars[i+3] in ' ,.!?': 
			chars[i:i+3] = [i for i in 'nts']
	return ''.join(chars)
