https://edabit.com/challenge/riF3RkrcKpBp3sKCX

Capital Split
Create a function which adds spaces before every capital in a word. Uncapitalize the whole string afterwards.

Examples
cap_space("helloWorld") ➞ "hello world"

cap_space("iLoveMyTeapot") ➞ "i love my teapot"

cap_space("stayIndoors") ➞ "stay indoors"
Notes
The first letter will stay uncapitalized.



data = "iLoveMyTeapot"
sentence=''
for chrc in data:
  if not chrc.islower():
    sentence+=' '+ chrc.lower()
  else:
    sentence+=chrc
print(sentence)




print(''.join([' '+i.lower() if i.isupper() else i for i in data]))