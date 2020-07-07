
#Create a function that takes a string and censors words over four characters with *.
#
#Examples
#censor("The code is fourty") ➞ "The code is ******"
#
#censor("Two plus three is five") ➞ "Two plus ***** is five"
#
#censor("aaaa aaaaa 1234 12345") ➞ "aaaa ***** 1234 *****"
#
#
#Don't censor words with exactly four characters.
#If all words have four characters or less, return the original string.
#The amount of * is the same as the length of the word.




def censor(s):
	return ' '.join('*'*len(i) if len(i) > 4 else i for i in s.split())


    def censor(s):
	txt = s.split()
	for i in range(len(txt)):
		if len(txt[i]) > 4:
			txt2 =list(txt[i])
			for j in range(len(txt2)):
				txt2[j] = '*'
				txt[i]="".join(txt2)
	return " ".join(txt)



  def censor(s):
  return ' '.join(x if len(x)<5 else '*'*len(x) for x in s.split())  




  def censor(s):
  x = s.split(' ')
  r = []
  for i in x:
    if len(i) <= 4:
      r.append(i)
    else:
      r.append('*' * len(i))
  return ' '.join(r)







  def censor(s):
	lst = s.split()
	empty_lst = []
	for i in lst:
		if len(i) > 4:
			i = '*' * len(i)
		empty_lst.append(i)
	return (' ').join(empty_lst)






    def censor(s):
	return ' '.join([x if len(x) < 5 else '*' * len(x) for x in s.split()])







    def censor(s):
	cen_list = s.split(" ")
	for c in range(0, len(cen_list)):
		if len(cen_list[c]) > 4:
			cen_list[c] = "*" * len(cen_list[c])
	return " ".join(cen_list)






    def censor(s):
	def c(word):
		return '*' * len(word) if len(word) > 4 else word
	a = list(map(c, s.split(' ')))
	return " ".join(a)





txt1 = "The code is forty"

txt = txt1.split()

liste = []
for i in txt:
    if len(i) > 4: liste.append("*" * len(i))
    else:liste.append(i)
print(" ".join(liste))