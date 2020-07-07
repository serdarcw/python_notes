
The Karaca's Encryption Algorithm


https://edabit.com/challenge/JzBLDzrcGCzDjkk5n

The Karaca's Encryption Algorithm
Make a function that encrypts a given input with these steps:

Input: "apple"

Step 1: Reverse the input: "elppa"

Step 2: Replace all vowels using the following chart:

a => 0
e => 1
o => 2
u => 3

# "1lpp0"
Step 3: Add "aca" to the end of the word: "1lpp0aca"

Output: "1lpp0aca"

Examples
encrypt("banana") ➞ "0n0n0baca"

encrypt("karaca") ➞ "0c0r0kaca"

encrypt("burak") ➞ "k0r3baca"

encrypt("alpaca") ➞ "0c0pl0aca"
Notes
All inputs are strings, no uppercases and all output must be strings.


A= "karaca"
B = A[::-1]
C=B.maketrans({ord('a'): ord('0'),ord('e'): ord('1'),ord('o'): ord('2'),ord('u'):ord('3')})
print(A.translate(C)+'aca')




def encrypt(word):
	return word[::-1].translate(str.maketrans('aeou', '0123')) + 'aca'




def encrypt(word):
  v= {'a':'0','e':'1','o':'2','u':'3'}
  return ''.join(v[i] if i in v else i for i in word[::-1]) +'aca'




def encrypt(word):
	word = word[::-1]
	for r in (("a", "0"), ("e", "1"), ("o", "2"), ("u", "3")):
		word = word.replace(*r)
		
	return word+'aca'







def encrypt(word):
	step1 = word[::-1]
	step2 = "".join([i if i not in "aeou" else str("aeou".index(i)) for i in step1])
	step3 = step2 + "aca"
	return step3



def encrypt(word):
    word = word[::-1]
    replaces = word.maketrans('aeou', '0123')
    return word.translate(replaces) + 'aca'

