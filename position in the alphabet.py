https://www.codewars.com/kata/546f922b54af40e1e90001da/python

Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)


def alphabet_position(text):
    A={'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13,'n':14, 'o':15,16, 'q':17,'r':18, 's':19, 't':20, 'u':21, 'v':22, 'y':23, 'z':24, 'x':25}
    return ' '.join([str(A.get(i.lower())) for i in text if i.lower() in A.keys()])
    #for i in text:
    #    if i.lower() in A.keys():
    #        B.append(A.get(i.lower()))
    #return B
print(alphabet_position("The sunset sets at Twelve o clock."))


def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())



alphabet = 'abcdefghijklmnopqrstuvwxyz'

def alphabet_position(text):
    if type(text) == str:
        text = text.lower()
        result = ''
        for letter in text:
            if letter.isalpha() == True:
                result = result + ' ' + str(alphabet.index(letter) + 1)
        return result.lstrip(' ')