https://edabit.com/challenge/rQkriLJBc9CbfRbJb

Return the Index of All Capital Letters

Create a function that takes a single string as argument and returns an ordered list containing the indices of all capital letters in the string.

Examples
index_of_caps("eDaBiT") ➞ [1, 3, 5]

index_of_caps("eQuINoX") ➞ [1, 3, 4, 6]

index_of_caps("determine") ➞ []

index_of_caps("STRIKE") ➞ [0, 1, 2, 3, 4, 5]

index_of_caps("sUn") ➞ [1]
Notes
Return an empty list if no uppercase letters are found in the string.
Special characters ($#@%) and numbers will be included in some test cases.

A="eDaBiT"
B=[]
[i for i,n in enumerate(A) if n.isupper()]


def index_of_caps(word):
    ret = []
    for i, c in enumerate(word):
        if c.isupper():
            ret.append(i)
    return ret


def index_of_caps(word):
  answer = []
  for i in range(len(word)):
    if word[i].isupper():
      answer.append(i)
  return answer


def index_of_caps(word):
  aux = []
  for i in range(len(word)):
    if word[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
      aux.append(i)
  return aux