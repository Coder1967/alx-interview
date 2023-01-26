#!/usr/bin/python3
def pascal_triangle(n):
	triangle = []
	last = []
	
	if n <= 0:
		return []
	triangle.append([1])
	if n == 1:
		return triangle
	
	last = triangle
		
	for i in range(n-1):
		j = 1
		sub = [1]
		while j < (len(last)+i)-1:
			try:
				sub.append(last[j-1] + last[j])
			except IndexError:
				break
			j += 1
		sub.append(1)
		triangle.append(sub)
		last = sub[:]
	return triangle
