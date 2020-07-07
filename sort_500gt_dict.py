https://edabit.com/challenge/SxevRSmRcshgwnAKp


A={'Computer' : 600, 'TV' : 800, 'Radio' : 100}
C=[]
B=sorted(list(A.values()), reverse=True)
for i in B:
    for j in A.keys():
        if i>=500 and i==A[j]:
            C.append(j)
print(C)

