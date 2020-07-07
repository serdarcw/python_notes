https://edabit.com/challenge/xbjDMxzpFcsAWKp97

Concert Seats
Create a function that determines whether each seat can "see" the front-stage. A number can "see" the front-stage if it is strictly greater than the number before it.

Everyone can see the front-stage in the example below:

# FRONT STAGE
[[1, 2, 3, 2, 1, 1],
[2, 4, 4, 3, 2, 2],
[5, 5, 5, 5, 4, 4],
[6, 6, 7, 6, 5, 5]]

# Starting from the left, the 6 > 5 > 2 > 1, so all numbers can see.
# 6 > 5 > 4 > 2 - so all numbers can see, etc.
Not everyone can see the front-stage in the example below:

# FRONT STAGE
[[1, 2, 3, 2, 1, 1], 
[2, 4, 4, 3, 2, 2], 
[5, 5, 5, 10, 4, 4], 
[6, 6, 7, 6, 5, 5]]

# The 10 is directly in front of the 6 and blocking its view.
The function should return True if every number can see the front-stage, and False if even a single number cannot.

Examples
can_see_stage([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]) ➞ True

can_see_stage([
  [0, 0, 0],
  [1, 1, 1],
  [2, 2, 2]
]) ➞ True

can_see_stage([
  [2, 0, 0], 
  [1, 1, 1], 
  [2, 2, 2]
]) ➞ False

can_see_stage([
  [1, 0, 0],
  [1, 1, 1],
  [2, 2, 2]
]) ➞ False

# Number must be strictly smaller than 
# the number directly behind it.

seats=[[1, 2, 3, 2, 1, 1], 
[2, 4, 4, 3, 2, 2], 
[5, 5, 5, 10, 4, 4], 
[6, 6, 7, 6, 5, 5]]

count=0
for j in range(len(seats[0])):
	A=[]
	for i in range(len(seats)):
		A.append(seats[i][j])
	if A==sorted(A):
		count+=1
print(count==len(seats[0]))


def can_see_stage(seats):
	return all(sorted(set(row)) == list(row) for row in zip(*seats))


def can_see_stage(seats):
	for i in range(len(seats[0])):
		for j in range(1, len(seats)):
			if seats[j][i] <= seats[j-1][i]:
				return(False)
	return(True)



def can_see_stage(seats):
  return all(sorted(set(i[j] for i in seats)) == [i[j] for i in seats] for j in range(len(seats[0])))

def can_see_stage(seats):
    rows, columns = len(seats), len(seats[0])
​
for i in range(columns):
    first = True
    for j in range(rows):
        if first:
            last = seats[j][i]
            first = False
        elif seats[j][i] <= last:
            return False
        else:
            last = seats[j][i]
