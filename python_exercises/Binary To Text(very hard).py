https://edabit.com/challenge/AGgQTPNy6G5cxz4KK

Binary To Text
Create a function that takes a binary string and returns the text. The eight bits on the binary string represent 1 character on the ASCII table. For further info, check out the resource tab.

Examples
binary_to_text("01101110011011110110010001100101") ➞ "node"

binary_to_text('0111001001100101011000010110001101110100') ➞ "react"

binary_to_text("011100000111100101110100011010000110111101101110") ➞ "python"
Notes
Inputs are all valid strings.




A="01101110011011110110010001100101"
#B=[A[8*i:8+8*i] for i in range(0,len(A)//8)]
''.join(list(map(lambda x: chr(int(x[0])*128+int(x[1])*64+int(x[2])*32+int(x[3])*16+int(x[4])*8+int(x[5])*4+int(x[6])*2+int(x[7])*1), [A[8*i:8+8*i] for i in range(0,len(A)//8)])))
print(sonuç)


def binary_to_text(n):
	return ''.join(chr(int(n[i:i+8], 2)) for i in range(0, len(n), 8))

def binary_to_text(n):
    return ''.join(chr(int(n[i: i + 8], 2)) for i in range(0, len(n), 8))


def binary_to_text(n):
	return ''.join(chr(sum(2**(7-i) for i,b in enumerate(n[s:s+8]) if b=='1'))
							for s in range(0,len(n),8))

def binary_to_text(n):
    res=""
    for index in range(0,len(n),8):
        number=""
        for jindex in range(index,index+8):
            number+=n[jindex]
        res+=chr(int(number,2))
    return res
