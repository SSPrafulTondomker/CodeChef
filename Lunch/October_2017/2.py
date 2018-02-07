for _ in range (input()) :
	n,k = map(int,raw_input().split())
	p = k
	r = pow(2,n)
	l = []
	for i in range(0,r) :
		l.append(i)
	i = n
	l1,l2 = [],[]
	g,f = [],[]
	while i > 0 :
	 	w = pow(2,i)
	 	j = 0
		while j < r and j >= 0:
			for k in range (j,w+j) :
				if k%2 == 0 and k < r:
					l1.append(l[k])
				elif k < r:
					l2.append(l[k])
			f += l1 + l2
			l1 = []
			l2 = []
			j += w
		l = f
		f = []
		i -= 1
	print l.index(p),l
	
