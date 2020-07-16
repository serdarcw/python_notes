
https://edabit.com/challenge/frRRffQGSrPTknfxY

Keeping Count
Given a number, create a function that returns a new number based on these rules:

For each digit, replace it by the number of times it appears in the number.
The final instance of the number will be an integer, not as a string.
Worked Example
digit_count(136116) ➞ 312332
# The number 1 appears thrice, so replace all 1s with 3s.
# The number 3 appears only once, so replace all 3s with 1s.
# The number 6 appears twice, so replace all 6s with 2s.
# Return as an integer.
Examples
digit_count(221333) ➞ 221333

digit_count(136116) ➞ 312332

digit_count(2) ➞ 1
Notes
All test input will be positive whole numbers.


A=136116
print(int(''.join([n.replace(str(n), str(list(str(A)).count(n))) for i,n in enumerate(list(str(A)))])))

def digit_count(n):
	n = str(n)
	return int(''.join(str(n.count(k)) for k in n))


def digit_count(n):
	tempString = str(n)
	result = ""
	for i in range( len(tempString) ):
		result += str(tempString.count(tempString[i]))
	return int(result)



def digit_count(n):
	new_txt = ''
	
	for i in str(n):
		new_txt += str(str(n).count(i))
	
	return int(new_txt)

