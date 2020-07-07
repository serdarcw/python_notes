Group Anagrams 
Given a list of strings, group anagrams together.
Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
All inputs will be in lowercase.
The order of your output does not matter.
================================================================================
Attention : Please send your solutions via private direct message to me :slightly_smiling_face: (edited) 

A=[“eat”, “tea”, “tan”, “ate”, “nat”, “bat”]
C=[]
B=[]
for i in A:
    for j in A:
        if set(i)==set(j):
            C.append(j)
    if not C in B:
        B.append(C)
    C=[]
print(B)

