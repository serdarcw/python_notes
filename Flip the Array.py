https://edabit.com/challenge/QoavwQhmrDpXJhBW9

Flip the Array (Hard)

lst=[1, 2, 3, 4]
B=[]
if lst==[]:
    lst=B
if isinstance(lst[0], int):
    print([[i] for i in lst])
else:
    print([i[0] for i in lst])



