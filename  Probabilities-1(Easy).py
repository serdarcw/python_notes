https://edabit.com/challenge/LMjficQtWW36a3by3

Probabilities (Part 1)
Given a list of numbers and a value n, write a function that returns the probability of choosing a number greater than or equal to n from the list. The probability should be expressed as a percentage, rounded to one decimal place.

Examples
probability([5, 1, 8, 9], 6) ➞ 50.0

probability([7, 4, 17, 14, 12, 3], 16) ➞ 16.7

probability([4, 6, 2, 9, 15, 18, 8, 2, 10, 8], 6) ➞ 70.0
Notes
Probability of event = (num of favourable outcomes) / (total num of possible outcomes)


def probability(lst, n):
	return round((len([k for k in lst if k>=n])/len(lst))*100, 1)


def probability(lst, n):
	outcomes = 0
	for number in lst:
		if number >= n:
			outcomes += 1
	return round((outcomes/len(lst))*100,1)


def probability(lst, n):
  c = 0
  for i in lst:
    if i >= n:
      c += 1
  return round((c/len(lst))*100,1)