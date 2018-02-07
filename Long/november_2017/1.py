for _ in range (input()) :
	n,p = map(int,raw_input().split())
	l = map(int,raw_input().split())
	c = 0
	f = 0
	for i in l :
		if i >= p/2 :
			c += 1
		elif i <= p/10 :
			f += 1
	if c == 1 and f == 2 :
		print "yes"
	else :
		print "no"
		
