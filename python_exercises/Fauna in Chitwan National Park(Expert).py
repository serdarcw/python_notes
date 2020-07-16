https://edabit.com/challenge/jecvfH5eyGLrSwzNh

Fauna in Chitwan National Park
Create a function that takes a string containing both name and number of animals and plants that may or may not be found in Chitwan National Park. The function should return a list of tuples where first element in the tuple is animal name and second element in the tuple is number of that particular animal that is found in Chitwan National Park.

Animals Present in Chitwan National Park
animals = ["muggercrocodile", "one-hornedrhino", "python", "moth", "monitorlizard", "bengaltiger"]
Examples
fauna_number("There are 24 one-hornedrhino,50 python and 20000 mango.") ➞ [("one-hornedrhino", "24"), ("python", "50")]
# Mango not present in animal list.

fauna_number("There are 244 bengaltiger,200 monitorlizard and 5000 apples .") ➞ [("bengaltiger", "244"), ("monitorlizard", "200")]
# Apples not present in animal list.
Notes
Input contains name and number of both animals and plants.
If there is no match, return an empty list.



animals = ["muggercrocodile", "one-hornedrhino", "python", "moth", "monitorlizard", "bengaltiger"]

txt = "There are 244 bengaltiger,200 monitorlizard and 5000 apples."
B,C=[], txt[:-1].split(',')
for i in C: B.extend(i.split())

print([(n,B[j-1]) for j,n in enumerate(B) if n in animals])


import re

def fauna_number(txt):
    animals = ["muggercrocodile","one-hornedrhino","python","moth","monitorlizard","bengaltiger"]
    return [(j, i) for i, j in re.findall('(\d+) ([a-z-]+)', txt) if j in animals]


import re
animals = ["muggercrocodile", "one-hornedrhino", "python", "moth",
           "monitorlizard", "bengaltiger"]
def fauna_number(txt):
    return [(m.group(2), m.group(1)) for m in re.finditer(r'(\d+) ([\w-]+)', txt)
            if m.group(2) in animals]


import re
def fauna_number(txt):
	animals = ["muggercrocodile","one-hornedrhino","python",
								"moth","monitorlizard","bengaltiger"]
	return [(b,a) for (a,b) in re.findall('(\d+) ({})'.format('|'.join(animals)),txt)]


def fauna_number(txt):
    animals = ["muggercrocodile","one-hornedrhino","python","moth","monitorlizard","bengaltiger"]
    numbers=[]
    txt=txt.replace(","," ").split()	
    for index in range (len(txt)):
        if  txt[index].find("-")==-1 and txt[index].find(".")==-1 and not txt[index].isalpha():
            if txt[index+1] in animals:
                numbers.append((txt[index+1],txt[index]))
    return numbers

