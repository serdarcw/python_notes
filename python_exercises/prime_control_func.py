
def prime(num):
    return not bool([j for j in range(2,int(num**(1/2))+1) if num%j==0])
print(prime(6))



def prime(num):
    return [j for j in range(2,int(num**(1/2))+1) if num%j==0]
print(prime())
