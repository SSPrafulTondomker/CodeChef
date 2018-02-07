l = [0, 2, 12, 36]
p = [0]
def find (n) :
	s = n
	e, o = 0,0 
	while s != 0 :
		k = s%10
		if k%2 == 0 :
			e += k
		else :
			o += k
		s /= 10
	k = abs(e-o)
	p.append(k)

def start() :
	for i in range (1,2000001) :
		find(i)
	for i in range (4,1000001) :
		me(i)

def me(n) :
	s = abs(l[n-1]-l[n-2])
	k = s + l[n-1] - p[n]*2 + p[(n-1)*2] + p[n+n-1]*2 + p[n*2]
	
	l.append(k)


start()
for _ in range (input()) :
	n = input()
	print l[n]
