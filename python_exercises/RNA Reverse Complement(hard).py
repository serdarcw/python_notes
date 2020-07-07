https://edabit.com/challenge/M8jNckAgpC5ZFkhhG


RNA Reverse Complement
Create a function that finds the reverse complement of a ribonucleic acid (RNA) strand. The RNA will be represented as a string containing only the characters "A", "C", "G" and "U". Since RNA can only (canonically) allow pairings of A/U and G/C, the complement of an RNA would be as follows:

original -> complement
"AAA" -> "UUU"
"UUU" -> "AAA"
"GGG" -> "CCC"
"CCC" -> "GGG"
"GGAACC" -> "CCAAGG"
Your function should find the complement on the right AND also reverse the resulting string.

Examples
reverse_complement("GUGU") ➞ "ACAC"

reverse_complement("UCUCG") ➞ "CGAGA"

reverse_complement("CAGGU") ➞ "ACCUG"
Notes
You can assume all input seqeuences will be valid.


dna='GUAGGCAACA'
rna=''

print(''.join(['G'*(i=='C') or 'C'*(i=='G') or 'A'*(i=='U') or 'U'*(i=='A')  for i in dna][::-1]))



for i in dna:
    if i=='G':
        rna+='C'
    elif i=='U':
        rna+='A'
    elif i=='C':
        rna+='G'
    else:
        rna+='U'
print(rna[::-1])



def reverse_complement(input_sequence):
	return input_sequence.translate(str.maketrans('AUCG', 'UAGC'))[::-1]


    def reverse_complement(input_sequence):
	dic = {'A':'U', 'U':'A', 'C':'G','G':'C'}
	return ''.join([ dic[a] for a in input_sequence[::-1]] )

def reverse_complement(input_sequence):
	a = {"A": "U", "G": "C", "U": "A", "C": "G"}
	return "".join([i.replace(i, a[i]) for i in input_sequence])[::-1]