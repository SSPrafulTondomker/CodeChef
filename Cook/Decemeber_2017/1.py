for _ in range (input()) :
	n = input()
	r, t = "", ""
	c, p = 0, 0
	for i in range (n) :
		s = raw_input().strip()
		if r == "" :
			r = s
		if r == s :
			c += 1
		else :
			t = s
			p += 1
	if c > p :
		print r
	elif c < p :
		print t
	else :
		print "Draw"
	
