

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining. 

A=[0,0,1,2,3,0,2,1,2,1,0,0]

def zero_eraser(B):
    k=0
    for i,n in enumerate(B):
        if n <= 0: k+=1
        if n>0: return B[k:]; break
m=0
while len(A)>1:
    A=zero_eraser(A)
    A=zero_eraser(A[::-1])
    m+=list(map(lambda x : 0 if x<=0 else x, A)).count(0)
    A=[i-1 for i in A]

print(m)

