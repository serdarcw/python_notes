https://edabit.com/challenge/vLRpikwB9dqaR3HAj


smlst=[1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1]
biglst=[1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1]
k=-1
count=0
for i in smlst:
    biglst=biglst[k+1:]
    for j in biglst:
        print(biglst)
        if i==j:
            k=biglst.index(j)
            count+=1
            break
print(count)
if count==len(smlst):
    print(True)
else:
    print(False)
