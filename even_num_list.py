
# Herhangi bir sayı verildiğinde o sayı dahil
#  o sayıya kadar olan çift sayıları bir list in içine yazdırma

num = int(input())
liste = list()
for i in range(1,num+1):
    if i%2 ==0: 
      liste.append(i)
print(liste)




def find_even_nums(num):
	return [ x for x in range(2,num+1,2)]




def find_even_nums(num):
	return [ i for i in range(1,num+1) if i%2==0 ]



def find_even_nums(num):
	return list(range(2, num + 1, 2))





def find_even_nums(num):
	return [i for i in range(1, num+1) if i % 2 == 0]







def find_even_nums(num):
  return [x+1 for x in range(num) if x%2]










def find_even_nums(num):
	if num%2 == 0:
		return [x for x in range(2,num+2,2)]
	else:
		return [x for x in range(2,num+1,2)]









