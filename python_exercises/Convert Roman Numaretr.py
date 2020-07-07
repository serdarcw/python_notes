
https://edabit.com/challenge/uPAmqwiHmvwpwoBom

Roman Numeral Converter
Create a function that takes an Arabic number and converts it into a Roman number.
Examples
convert_to_roman(2) ➞ "II"
convert_to_roman(12) ➞ "XII"
convert_to_roman(16) ➞ "XVI"
Notes
All roman numerals should be returned as uppercase.
The largest number that can be represented in this notation is 3,999.
Yazım Kuralları
1) Bir rakamın sağ tarafına, kendisinden küçük bir rakam geldiği zaman toplanarak okunur.
Örnek: XVI (16)
2) Bir rakamın sol tarafına, kendisinden küçük bir rakam geldiği zaman çıkarılarak okunur.
Örnek: XCI (91)
3) Bir rakam, en fazla üç kez yan yana yazılabilir.
Örnek: CCCXXI (321)
4) Bir rakamın merkezi, en büyük olan simgedir. Onun soluna veya sağına kendisinden küçük rakamlar yazılabilir.
Örnek: CDLII (452)
5) En büyük sayı 3888’dir. (MMMDCCCLXXXVIII)

c1:def convert_to_roman(num):
	roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
	sayi = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
	romanvalue = ""
	for i, d in enumerate(sayi):
		while (num >= d):
			num -= d
			romanvalue += roman[i]
	return romanvalue




c2:def convert_to_roman(num):
    d = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
         (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
         (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    res = ''
    for value, numeral in d:
        res += numeral * (num//value)
        num %= value
    return res



c3:def convert_to_roman(num):
	decimal = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
	numeral = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
	res = ''
	for i in range(13):
		val = num//decimal[i]
		if val:
			res += numeral[i] * val
			num -= decimal[i] * val
	return res




c4:def convert_to_roman(n):
	rom = ['M','D','C','L','X','V','I']
	ara = [1000,500,100,50,10,5,1]
	r = ''
	for i in ara:
		if n//i:
			if n//i!=4:
				r+=(rom[ara.index(i)])*(n//i)
			elif rom[ara.index(i)-1] not in r:
				r+=rom[ara.index(i)]+rom[ara.index(i)-1]
			else:
				r=r[:-1]+rom[ara.index(i)]+rom[ara.index(i)-2]
			n%=i
	return r



num=2308

roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
sayi = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
romanvalue = ""
for rom,arb in enumerate(sayi):
    while num>=arb:
        num-= arb
        romanvalue+=roman[rom]
print(romanvalue)

