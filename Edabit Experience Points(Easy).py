
https://edabit.com/challenge/yvwdxFcxkT5hiTgfr

Edabit Experience Points
As you complete questions on Edabit, you gain experience points depending on the difficulty of the question. The points for each difficulty are as follows:

Difficulty	Experience Points
Very Easy	5XP
Easy	10XP
Medium	20XP
Hard	40XP
Very Hard	80XP
Given a dictionary of how many questions a person has completed of each difficulty, return how many experience points they'll have.

Examples
get_xp({
  "Very Easy" : 89,
  "Easy" : 77,
  "Medium" : 30,
  "Hard" : 4,
  "Very Hard" : 1
}) ➞ "2055XP"


get_xp({
  "Very Easy" : 254,
  "Easy" : 32,
  "Medium" : 65,
  "Hard" : 51,
  "Very Hard" : 34
}) ➞ "7650XP"


get_xp({
  "Very Easy" : 11,
  "Easy" : 0,
  "Medium" : 2,
  "Hard" : 0,
  "Very Hard" : 27
}) ➞ "2255XP"
Notes
Return values as a string and make sure to add "XP" to the end.





d={
  "Very Easy" : 89,
  "Easy" : 77,
  "Medium" : 30,
  "Hard" : 4,
  "Very Hard" : 1
}
point={
  "Very Easy" : 5,
  "Easy" : 10,
  "Medium" : 20,
  "Hard" : 40,
  "Very Hard" : 80
}
A=["Very Easy","Easy","Medium","Hard","Very Hard"]
sum=0
for i in A:
    sum+=d[i]*point[i]
print(sum)




def get_xp(d):
	return str(d["Very Easy"]*5 + d["Easy"]*10 + d["Medium"]*20 + d["Hard"]*40 + d["Very Hard"]*80) + "XP"



def get_xp(d):
  points = [
    d.get('Very Easy') * 5,
    d.get('Easy') * 10,
    d.get('Medium') * 20,
    d.get('Hard') * 40,
    d.get('Very Hard') * 80
  ]
  return '{}XP'.format(sum(points))



