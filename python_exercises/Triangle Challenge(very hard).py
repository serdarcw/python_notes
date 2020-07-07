https://edabit.com/challenge/dSrisJKHB78aj2d7L

Triangle Challenge
Given the perimeter and the area of a triangle, devise a function that returns the length of the sides of all triangles that fit those specifications. The length of the sides must be integers. Sort results in ascending order.

triangle(perimeter, area) ➞ [[s1, s2, s3]]
Examples
triangle(12, 6) ➞ [[3, 4, 5]]

triangle(45, 97.42786) ➞ [[15, 15, 15]]

triangle(70, 210) ➞ [[17, 25, 28], [20, 21, 29]]

triangle(3, 0.43301) ➞ [[1, 1, 1]]




perimeter=45
area=97.42786
B=[]
for i in range(1,perimeter-1):
    for j in range(1,perimeter-1):
        if type(((perimeter/2)*((perimeter/2)-i)*((perimeter/2)-j)*((perimeter/2)-(perimeter-i-j)))**(1/2))!=complex and round(((perimeter/2)*((perimeter/2)-i)*((perimeter/2)-j)*((perimeter/2)-(perimeter-i-j)))**(1/2), 5)==area and :
            if sorted([i,j,perimeter-i-j]) not in B and perimeter-i-j>0:
                B.append(sorted([i,j,perimeter-i-j]))
print(B)

def triangle(p,a):
    r=[]
    s=p/2
    for x in range(1,p//2+1):
        for y in range(int(s-x+1),p//2+1):
                z=p-x-y
                if round((s*(s-x)*(s-y)*(s-z))**.5,5)==a:
                    new=sorted((x,y,z))
                    if new not in r:
                        r.append(new)
    return sorted(r)



def triangle(p, area):
    const, sol, r = round(2*area**2/p, 3), [], range(1, round(p/2+0.1))
    sol = [tuple(sorted((a, b, p-a-b))) for a in r for b in r
           if (p/2-a)*(p/2-b)*(a+b-p/2)==const]
    return sorted([list(i) for i in set(sol)])




def triangle(per,area):
	ans = []
	semi = per/2
	for i in range(1, 1+per//2):
		for j in range(1, per+2 - 2*i):
			if abs((semi*(semi-i)*(semi-j)*(i+j-semi))**.5-area)<0.001:
					if sorted([i,j,per-i-j]) not in ans:
						ans.append(sorted([i,j,per-i-j]))
	return sorted(ans)

    
