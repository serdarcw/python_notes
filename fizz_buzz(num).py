

#Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".
#
#If the number is a multiple of 3 the output should be "Fizz".
#If the number given is a multiple of 5, the output should be "Buzz".
#If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
#If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.
#The output should always be a string even if it is not a multiple of 3 or 5

def fizz_buzz(num):
	if int(num)%3 == 0 and int(num)%5 != 0:
		return "Fizz"
	elif int(num)%5 == 0 and int(num)%3 != 0:
		return "Buzz"
	elif int(num)%5 == 0 and int(num)%3 == 0:
		return "FizzBuzz"
	else:
		return str(num)





def fizz_buzz(num):
	return "Fizz"*(num%3==0) + "Buzz"*(num%5==0) or str(num)





def fizz_buzz(x):
if x % 3:
	return str(x) if x % 5 else "Buzz"
return "Fizz" if x % 5 else "FizzBuzz"






def fizz_buzz(num):
	if(num%3==0 and num%5==0):
		return "FizzBuzz"
	elif(num%3==0):
		return "Fizz"
	elif(num%5==0):
		return "Buzz"
	else:
		return str(num)







def fizz_buzz(num):
	if num%3 == 0 and num%5 == 0: return "FizzBuzz"
	elif num%3 == 0: return "Fizz"
	elif num%5 == 0: return "Buzz"
	else: return str(num)





    def fizz_buzz(num):
  return ''.join(['FizzBuzz' if num % 3 == 0 and num % 5 == 0 else 'Fizz' if num % 3 == 0 else 'Buzz' if num % 5 == 0 else str(num)])






def fizz_buzz(num):
    if num % 3 < 1 and num % 5 < 1: return "FizzBuzz"
	if num % 3 < 1: return "Fizz"
	if num % 5 < 1: return "Buzz"
	return str(num)




def fizz_buzz(num):
  s = ''
  if num%3 == 0: s += 'Fizz'
  if num%5 == 0: s += 'Buzz'
  return s if s else str(num)


