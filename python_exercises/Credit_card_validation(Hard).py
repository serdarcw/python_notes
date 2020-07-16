https://edabit.com/challenge/XKEDTh2NMtTLSyCc2

Mod 10 Algorithm
Create a function that takes a number and checks whethers the given number is a valid credit card number using Luhn Algorithm. The return value is boolean.

Examples
valid_credit_card(4111111111111111) ➞ True
# Visa Card

valid_credit_card(6451623895684318) ➞ False
# Not a valid credit card number.

valid_credit_card(6451623895684318) ➞ False
Notes
American Express/VISA/Discover/Diner Club may be the credit card type.
Check the Resources for help.

number = 7777777777777777
A= list(str(number//10))[::-1]
number1= list(map(lambda x : 2*int(x), A[::2]))
number2= list(map(lambda x : x-9 if int(x)>9 else int(x), number1))
K=list(map(lambda x : int(x), A[1::2]))
print(((sum(K)+sum(number2))*9)%10==number%10)