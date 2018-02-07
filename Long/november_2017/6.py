for _ in xrange(input()):
	n = input()
	p, l = [], []
	for i in xrange(n) :
		r = raw_input().split()
		p.append(int(r[0]))
		l.append(r[1:])

	f, s, k, c, t = 0, 0, 0, 0, 0
	while c < n:
		s = 0
		print l
		for i in xrange(n-1):
			f = abs (int(l[i][p[i]-1])- int(l[i+1][p[i+1]-1]))
			f *= (i+1)
			s += f

		if k < s :
			k = s

		r = l[c]
		print r[p[c]-1]
		r = list(r[p[c]-1]) + (r[:p[c]-1])
		l[c] = r
		t += 1
		if t == p[c] :
			c += 1
			t = 0
	print k


