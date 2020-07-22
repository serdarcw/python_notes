
Bir kelimeyi okutturup, her harfini alfabedeki bir sonraki harfle değiştiren fonksiyon yazabilir misiniz?  İnterview sorudu idi.
Örnek;
input : bursa output: cvstb

A='abcdefghijklmnopqrstuvyz'
A+='a'
word='bursaz'
print(''.join([A[A.index(n)+1] for i,n in enumerate(word)]))



A='abcdefghijklmnopqrstuvyz'
A+='a'
word='bursaz'
print(''.join(map(lambda x : A[A.index(x)+1], word)))
