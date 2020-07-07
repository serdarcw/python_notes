Given two strings,  and ,
that may or may not be of the same length,
determine the minimum number of character deletions required to make  and  anagrams.
Any characters can be deleted from either of the strings.


a = "Car"
b = "car"
pre_total = len(a)+len(b)
for i in a:
    if i in b :
        b = b.replace(i,'',1)
        a = a.replace(i,'',1)
 
post_total = len(a)+len(b)
print(f"a value is {a}")
print(f"b value is {b}")
if (post_total == pre_total):
    print("Those two words cant have an anagram")
else:
    print(len(a)+len(b))