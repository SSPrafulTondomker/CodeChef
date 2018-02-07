import math
n,k = map(int,raw_input().split())
x = map(int,raw_input().split())
y = map(int,raw_input().split())
r = 0.0
l = []
for i in range (n) :
	x1 = x[i]*x[i]
	y1 = y[i]*y[i]
	l.append(x1+y1)
l.sort()
print int(math.ceil(math.sqrt(l[k-1])))
	
