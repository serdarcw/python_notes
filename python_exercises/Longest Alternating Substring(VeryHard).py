https://edabit.com/challenge/RB6iWFrCd6rXWH3vi

Longest Alternating Substring
Given a string of digits, return the longest substring with alternating odd/even or even/odd digits. If two or more substrings have the same length, return the substring that occurs first.

Examples
longest_substring("225424272163254474441338664823") ➞ "272163254"
# substrings = 254, 272163254, 474, 41, 38, 23

longest_substring("594127169973391692147228678476") ➞ "16921472"
# substrings = 94127, 169, 16921472, 678, 476

longest_substring("721449827599186159274227324466") ➞ "7214"
# substrings = 7214, 498, 27, 18, 61, 9274, 27, 32
# 7214 and 9274 have same length, but 7214 occurs first.
Notes
The minimum alternating substring size is 2.


A=754388489999793138912431545258
C=str(A)+str(A)[-1]
K, lengh=[], []
for i in range(len(C)-1):
    if int(C[i])%2!=int(C[i+1])%2: K.append(C[i])
    else:
        K.append(C[i])
        print(K)
        if len(K)>len(lengh): lengh=K
        K=[]
print(int(''.join(lengh)))



def longest_substring ( n ):
    txt=''
    for i in range(len(n)-1):
        if int(n[i])%2==int(n[i+1])%2:
            txt=txt[:-1]+n[i]+" "+n[i+1]
        else: txt=txt[:-1]+n[i]+n[i+1]
    return sorted(txt.split(),key=len,reverse=True)[0]
print(longest_substring ( "844929328912985315632725682153" ))  # 56327256


def longest_substring(digits):
    res = digits[0]
    for i in digits[1:]:
        if int(i)%2 != int(res[-1])%2:
            res += i
        else:
            res += ' ' + i
    return max(res.split(), key=len)
