def XOR(l,x,y) :
	t = 0
	for i in range (x,y+1) :
		t ^= l[i]
	return t
def MINI(l,x,y) :
	tr = 100000000
	for i in range (x,y+1) :
		if tr > l[i] :
			tr = l[i]
	return tr

n, k = map(int, raw_input().split()) 
l = map(int, raw_input().split())
f = []
s = n*(n+1)/2
x, y, z = 0, 0, 1
for i in range (s) :
	f.append(XOR(l,x,y)*MINI(l,x,y))
	#print x,y,MINI(l,x,y),XOR(l,x,y)
	y += 1
	if y == n :
		y = z
		x = z
		z += 1
f.sort()
print f[k-1]
