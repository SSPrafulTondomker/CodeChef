for _ in range (input()) :
	l = []
	n = 0
	for i in range (input()) :
		p = map (int,raw_input().split())
		n += 1
		l.append (p)
	e = 0
	i = 0
	s = 0
	while i < n :
	 	j = i+1
	 	r = s
		while j < n :
			y = l[i]
			k = l[j]
			q1,q2 = y[0],y[1]
			w1,w2 = k[0],k[1]
			s = abs (q1-w1) + abs (q2-w2)
			j += 1
		if r 
		i += 1
	print e


