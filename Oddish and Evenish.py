
https://edabit.com/challenge/H3t4MkT9wGdL9P6Y3


Oddish vs. Evenish
Create a function that determines whether a number is Oddish or Evenish.
 A number is Oddish if the sum of all of its digits is odd, and a number is 
 Evenish if the sum of all of its digits is even. If a number is Oddish, 
 return "Oddish". Otherwise, return "Evenish".

For example, oddish_or_evenish(121) should return "Evenish", since 1 + 2 + 1 = 4. 
oddish_or_evenish(41) should return "Oddish", since 4 + 1 = 5.

Examples



def oddish_or_evenish(num):
	sum=0
	for i in str(num):
		sum+=int(i)
	if sum%2!=0: return "Oddish"
	else: return "Evenish"





def oddish_or_evenish(num):
	result = sum([int(x) for x in str(num)])
	if result%2 == 0:
		return ("Evenish")
	else:
		return ("Oddish")




def oddish_or_evenish(num):
	b=0
	for x in str(num):
		b=b+int(x)
	if b%2==0:
		return "Evenish"
	return "Oddish"






def oddish_or_evenish(num):
  total = 0
  for i in str(num):
      total += int(i)
  return 'Evenish' if total % 2 == 0 else 'Oddish'