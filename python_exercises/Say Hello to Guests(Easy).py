https://edabit.com/challenge/SKorutJdWGBzXJDRt

Say Hello to Guests
In this exercise you will have to:

Take a list of names.
Add "Hello" to every name.
Make one big string with all greetings.
The solution should be one string with a comma in between every "Hello (Name)".

Examples
greet_people(["Joe"]) ➞ "Hello Joe"

greet_people(["Angela", "Joe"]) ➞ "Hello Angela, Hello Joe"

greet_people(["Frank", "Angela", "Joe"]) ➞ "Hello Frank, Hello Angela, Hello Joe"
Notes
Each greeting has to be separated with a comma and a space.
If you're given an empty list [], return an empty string "".


A=["Frank", "Angela", "Joe"]

print(''.join(['Hello '+i+', ' for i in A])[:-2])



def greet_people(n):
  return ', '.join(['Hello ' + i for i in n])


