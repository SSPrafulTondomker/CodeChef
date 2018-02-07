for _ in range (input()) :
	k, d0, d1 = map(int, raw_input().split())
	k -= 2
	s = 0
	s = d0 + d1
	u = [2, 4, 6, 8]
	f = 0
	c = 0
	while k > 0 :
		c = 0
		r = s%10
		s += r
		if r in u :
			c += 1
		k -= 1
		if k <= 0 :
			break
		r = s%10 
		s += r
		if r in u :
			c += 1
		k -= 1
		if k <= 0 :
			break
		r = s%10
		s += r
		if r in u :
			c += 1
		k -= 1
		if k <= 0:
			break
		r = s%10
		s += r
		if r in u :
			c += 1
		k -= 1
		if c == 4 :
			f = 1
			break
	
	if f == 0 :
		if s%3 == 0:
			print "YES"
		else :
			print "NO"

	else :
		p = k%4
		t = k/4
		if p == 0 :
			s += 2*t + 4*t + 8*t + 6*t
		else :
			if p == 3 :
				t += 1
				s += 2*t + 4*t + 8*t + 6*(t-1)
			elif p == 2 :
				s += 2*(t+1) + 4*(t+1) + 8*t + 6*t
			else :
				s += 2*(t+1) + 4*t + 8*t + 6*t
			if s%3 == 0 :
				print "YES"
			else :
				print "NO"
