1. 

#a = str(input())
#b = list(a)
#c = sorted(b)
#d = ''.join(c)
#print(d)


2. 
#a = str(input())
#b = sorted(list(a))
#c = ''.join(b)
#print(c)



3. 
#a = str(input())
#b = ''.join(sorted(list(a)))
#print(b)


4. 
#def alphabet_soup(text):
#  return ''.join(sorted(text))
#


def alphabet_soup(text):
  ret = ''
  lst = list(text)
  lst.sort()
  return ret.join(lst)





def alphabet_soup(text):
  result=[]
  for i in range(97,97+26):
    for j in text:
      if chr(i) == j:
        result.append(j)
  return ''.join(result)





def alphabet_soup(text):
  name = ""
  sorted_text = sorted(text)
  for i in sorted_text:
    name = name + i
  return name




def alphabet_soup(text):
    l = sorted(list(text))
	return ''.join(l)




def alphabet_soup(text):
  tmp = []
  for each in text:
    tmp.append(each)
  tmp.sort()
  return "".join(tmp)




def alphabet_soup(text):
  word = ""
  for c in sorted(text):
    word += c
  return word

  