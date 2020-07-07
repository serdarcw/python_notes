https://edabit.com/challenge/FSRLWWcvPRRdnuDpv

Jake's Meal Time
Jake is a very habitual person. He eats breakfast at 7:00 a.m. each morning, lunch at 12:00 p.m. and dinner at 7:00 p.m. in the evening.

Create a function that takes in the current time as a string and determines the duration of time before Jake's next meal. Represent this as a list with the first and second elements representing hours and minutes, respectively.

Examples
time_to_eat("2:00 p.m.") ➞ [5, 0]
// 5 hours until the next meal, dinner

time_to_eat("5:50 a.m.") ➞ [1, 10]
// 1 hour and 10 minutes until the next meal, breakfast





time='11:58 p.m.'
C=0
if len(time)==9:
    C=60*(int(time[0])+12*(time[-4]=='p'))+eval(time[2:4])
else:
    C=60*(eval(time[0:2])+12*(time[-4]=='p'))+eval(time[3:5])
print(C)
breakfast, lunch, dinner = 420, 720, 1140
if C==720:
    return [7,0] 
if C < breakfast:
    print([(breakfast-C)//60, (breakfast-C)-60*((breakfast-C)//60)])
elif breakfast < C <lunch:
    print([(lunch-C)//60, (lunch-C)-60*((lunch-C)//60)])
elif lunch < C < dinner:
    print([(dinner-C)//60, (dinner-C)-60*((dinner-C)//60)])
elif C> dinner:
    print([7+(1440-C)//60, (1440-C)-((1440-C)//60)*60])



def time_to_eat(ct):
    h, p = int(ct[:ct.find(':')]), ct[ct.find('.')-1]=='p'
    m = int(ct[ct.find(':')+1:ct.find(' ')])
    h = 7-h-int(m>0) if p else 12-h-int(m>0) if 7<=h<12 else 7-h-int(m>0)
    m = 60 - m if m > 0 else m
    return [h if h>=0 else 12+h, m]


def time_to_eat(ct):
	#from datetime import datetime
	#an = datetime.datetime.now()
	saat_dk,vak = [i for i in ct.split()]
	saat,dk = [int(i) for i in saat_dk.split(":")]
	lst = []
	if vak == "p.m.":
		saat = saat + 12
	if 7 <= saat < 12:
		kal_sa = 11 - saat
		kal_dk = 60 - dk
	elif 12 <= saat < 19:
		kal_sa = 18 - saat
		kal_dk = 60 - dk
	elif 19 <= saat < 24:
		kal_sa = 23 - saat + 7
		kal_dk = 60 - dk
	elif 0 <= saat < 7:
		kal_sa = 6 - saat
		kal_dk = 60 - dk
	if kal_dk >=60 :
		kal_dk = kal_dk - 60
		kal_sa = kal_sa + 1
	lst.append(kal_sa)
	lst.append(kal_dk)
	return lst