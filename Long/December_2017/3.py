l = []
l.append(0)
l.append(2)
def find(n) :
	p = 0
	for i in range (1,n+1) :
		s = i+n
		k,e,o = 0,0,0
		while s != 0 :
			k = s%10
			if k%2 == 0 :
				e += k
			else :
				o += k
			s = s/10
		if i != n :
			p += (abs (e-o))*2
		else :
			p += abs(e-o)
	

	l.append(l[n-1]+p)
		
def start() :
	for i in range (2,10001) :
		find(i)
		#print i

start()
for _ in range (input()) :
	n = input()
	print l[n]

