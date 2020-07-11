https://edabit.com/challenge/vTGXrd5ntYRk3t6Ma

Is the Word an Isogram?
An isogram is a word that has no repeating letters, consecutive or nonconsecutive. Create a function that takes a string and returns either True or False depending on whether or not it's an "isogram".

Examples
is_isogram("Algorism") ➞ True

is_isogram("PasSword") ➞ False
# Not case sensitive.

is_isogram("Consecutive") ➞ False
Notes
Ignore letter case (should not be case sensitive).
All test cases contain valid one word strings.


def is_isogram(txt):
	return len(set(txt.lower()))==len(txt.lower())


def is_isogram(txt):
    word = txt.lower()
    for i in word:
        if word.count(i) > 1:
            return False
    return True


def is_isogram(txt):
    txt = txt.lower()
    for letter in txt:
        if txt.count(letter) > 1:
            return False
    return True

