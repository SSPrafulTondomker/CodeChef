def reach(l) :


for _ in range (input().split()) :
	n, m = map(int, raw_input().split()) 
	r, l, z, s = [], [], [], []
	for i in range (m) :
		z.append(0)
	for i in range (n) :
		r = map(int, raw_input().split())
		l.append(r)
		s.append(z)
	reach(l, s)
