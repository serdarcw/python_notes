Create a function that reverses a boolean value and returns the string "boolean expected" if another variable type is given.

Examples
reverse(True) ➞ False

reverse(False) ➞ True

reverse(0) ➞ "boolean expected"

reverse(None) ➞ "boolean expected"




arg = input('Please enter your value')
print("boolean expected" if not isinstance(arg, bool) else not arg) 





arg = input('Please enter your value')
	if type(arg) != bool:
		return 'boolean expected'
	return not arg



arg = input('Please enter your value')
if type(arg) == bool: 
    return not arg
else:
    return "boolean expected"


