https://edabit.com/challenge/XQwPPHE6ZSu4Er9ht

Ekonomik Sayı
Asal çarpanlarına ayırma basamaklarının sayısı (1'den büyük üsler dahil), sayının kendisinin sayı miktarına eşit veya bundan küçükse bu sayı Ekonomik Sayı'dır.
Verilen bir "n" sayısı için aşağıdaki str leri döndüren bir fonksiyon uygulayın:
"Equadigital" : Asal çarpanlarına ayırma basamaklarının sayısı (1'den büyük üsler dahil) n sayısının basamak miktarına eşit ise.
"Frugal" : Asal çarpanlarına ayırma basamaklarının sayısı (1'den büyük üsler dahil) n sayısının basamak miktarından küçük ise.
"Wasteful" : Bu iki durumdan birini sağlamıyorsa.
Örnekler:
Ekonomik Sayı(14) - "Equadigital"
# 14 (2 basamaklı) sayısının asal çarpanları [2, 7] (2 rakam) dir. (n sayısın basamak sayısı asal çarpanları rakam sayısına eşit olduğu için) 2=2
# 2 ve 7 asal çarpanlarının üsleri "1" olduğu için dikkate alınmamıştır.
Ekonomik Sayı(125) - "Frugal"
# 125 (3 basamaklı) sayısının asal çarpanları [5**3] (2 rakam) (n sayısının basamak sayısı asal çarpanlarından (5 ve 3) adet olarak fazladır.) 3 > 2
# Asal çarpanlarından 5 sayısının üs değeri 1 den büyük olduğu için işleme alınmıştır.
Ekonomik Sayı(1024) - "Frugal"
# 1024 (4 basamaklı) sayısının asal çarpanları [2**10] (3 rakam) 4 > 3
Ekonomik Sayı(30) - "Wasteful"
# 30 (2 basamaklı) sayısının asal çarpanları [2, 3, 5] (3 rakam) 2 < 3
Usta yazılımcıların ehil ellerine bırakıyorum. Saygılarımla.

A=150528
B, T=[], len(str(A))
for i in range(2,A+1):
    count, C , M, N= 0 , [],[], []
    K=sum([1 for j in range(2,int(i**(1/2))) if i%j==0])
    if K==0: C.append(i)
    if len(C)!=0: B.append(C[0])
for i,n in enumerate(B):
    while A%n==0:
        A=A//n
        M.append(n)
    if M.count(n)==1: 
        N.append(str(n))
    elif M.count(n)>=2: 
        N.append(str(n)+str(M.count(n)))
print(N)
print(len(str(''.join(N))))
if len(str(''.join(N)))==T: print('Equadigital')
elif len(str(''.join(N)))<T: print('Frugal')
else: print('Wastful')




def is_economical ( n ) :
    prm , pow = [ ] , [ ]
    prm = prime_fact(n)
    pow = power(prm ,pow, n).copy()
    return "Equadigital"*(sum([len(str(i)) for i in pow+prm if i!=1])==len(str(n)))\
           or"Wasteful"*(sum([len(str(i)) for i in pow+prm if i!=1]) > len(str(n)))\
           or"Frugal"
def is_prime(n):
    return all([n%i for i in range(2,n)]) and n!=1
def prime_fact(n):
    return [i for i in range(2,n+1) if is_prime(i) and not n%i]
def power(prm,pow,num):
    count=0
    for i in prm :
        while (not num % i) :
            num /= i
            count += 1
        pow.append(count)
        count = 0
    return pow


import math
def asal_mi(sayi):
    if sayi >= 2:
        i=2
        while i <= math.sqrt(sayi):
            if sayi % i == 0:
                return False
            i += 1
        else:
            return True
    else:
        return False
def asal_list(sayi):
    #sayi=150528
    asal_listesi = [i for i in range(2,sayi+1) if asal_mi(i) and not sayi%i]
    ussuz_carpanlar = asal_listesi.copy()
    # [2, 3, 7]
    for asal in asal_listesi:
        us =1
        while sayi % asal**us == 0:
            us+=1
        else:
            asal_listesi[asal_listesi.index(asal)]= asal ** (us-1)
    #[1024, 3, 49]
    count= len("".join(map(str,ussuz_carpanlar)))
    # "237"
    for i,k in list(zip(ussuz_carpanlar,asal_listesi)):
        bas_say=int(math.log(k,i))
        if (bas_say)!=1:
            count+=len(str(bas_say))
    if int(count)==len(str(sayi)):
        return f"Equadigital {count}"
    elif int(count)<=len(str(sayi)):
        return f"Frugal {count}"
    else :
        return f"Wasteful {count}"

