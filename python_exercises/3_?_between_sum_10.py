https://medium.com/coderbyte/the-5-hardest-code-challenges-for-beginners-e410da4474b


Challenge Description
Take an input string parameter and determine if exactly 3 question marks exist between every pair of numbers that add up to 10. If so, return true, otherwise return false. Some examples test cases are below:

Before reading further, try and think of how you would solve this challenge (you can even write down some steps in pseudocode, or better yet you can write a solution on Coderbyte).

"arrb6???4xxbl5???eee5" => true
"acc?7??sss?3rr1??????5" => true
"5??aaaaaaaaaaaaaaaaaaa?5?5" => false
"9???1???9???1???9" => true
"aa6?9" => false


D='acc?7??sss?3rr1??????5'
A='0'+D+'0'
B=[]
k=0
for i,n in enumerate(A):
  if n.isdigit():
    B.append((A[k:i+1], A[k:i+1].count('?'), int(A[k])+int(A[i])))
    k=i
print(B) 
C, E =[], []
for i in B:
    if i[2]==10:
        C.append(i)
        if i[1]==3:
            E.append(i)
print(len(C)!=0 and len(C)==len(E))





A='aa9?0'
B=[]
k=0
for i,n in enumerate(A):
  if n.isdigit():
    B.append(A[k:i+1])
    k=i
count1=0
C=[]
for i in B:
  if  not i[0].isdigit():
    C.append(i)
  else:
      if int(i[0])+int(i[-1])==10:
          if i.count('?')!=3:
            count1+=1
      else:
        C.append(i)
print(count1==0 and not len(C)==len(B))



def qu_find(txt):
    digit = [i for i in range(len(txt)) if txt[i].isdigit()]
    txt_list = []
    for k in range(len(digit)):
        txt_list.append(txt[digit[k-1]:digit[k]+1])
    txt_list.pop(0)
    print(txt_list)
    return len([i for i in txt_list if int(i[0])+int(i[-1])==10])!=0 and (len([i for i in txt_list if int(i[0])+int(i[-1])==10]) == len([i for i in txt_list if int(i[0])+int(i[-1])==10 and i.count("?")==3]))

print(qu_find('9???1???9???1???9'))
