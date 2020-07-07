
Calculated Bonus
#Bonus

A financial institution provides professional services to banks and claims charges 
from the customers based on the number of man-days provided. Internally, it has set 
a scheme to motivate and reward staff to meet and exceed targeted billable utilization 
and revenues by paying a bonus for each day claimed from customers in excess of a threshold 
target. This quarterly scheme is calculated with a threshold target of 32 days per quarter, 
and the incentive payment for each billable day in excess of such threshold target is shown as follows:

| 0 to 32 days | Zero | | 33 to 40 days | SGD$325 per Billable Day | 
| 41 to 48 days | SGD$550 per Billable Day | | > 48 days | SGD$600 per Billable Day |

Please note that incentive payment is calculated progressively. As an example, 
if an employee reached total billable days of 45 in a quarter, his/her incentive payment
 is computed as follows:

32*0 + 8*325 + 5*550 = 5350

Write a function bonus to read the billable days of an employee and return 
the bonus he/she has obtained in that quarter.

bonus(15) ➞ 0
bonus(37) ➞ 1625
bonus(50) ➞ 8200





n = 50
if n>48:
    top =7000+(n%48)*600
elif n>41:
    top =2600+(n%32)*550
elif n>32:
    top =(n%32)*325
print(top)


def bonus(days):
	return 325*max(0,days-32) + 225*max(0,days-40) + 50*max(0,days-48)


def bonus(days):
    if days <= 32:
        return 0
    days -= 32
    bonus = 325 * min(days, 8)
    days -= 8
    if days <= 0:
        return bonus
    bonus += 550 * min(days, 8)
    days -= 8
    if days <= 0:
        return bonus
    bonus += 600 * days
    return bonus


def bonus(days):
	if days > 48:
		return 600 * (days - 48) + 550 * 8 + 325 * 8
	if days > 40:
		return 550 * (days - 40) + 325 * 8
	if days > 32:
		return 325 * (days - 32)
	return 0



def bonus(days):
    total = 0
    for i in range(1, days+1):
        if 32 < i <= 40:
            total += 325
        if 40 < i <= 48:
            total += 550
        if i > 48:
            total += 600
    return total



def bonus(days):
	b = 0
	for i in range(days+1):
		if 33<=i<=40:
			b+=325
		elif 41<=i<=48:
			b+=550
		elif 49<=i:
			b+=600
	return b






def bonus(days):
	pay = ((32,0),(8,325),(8,550),(float('inf'),600))
	r = 0
	for d,x in pay:
		if days<=d:
			r += x*days
			break
		else:
			r += x*d
			days -= d
	return r
