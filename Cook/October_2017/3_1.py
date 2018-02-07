import math
for _ in range (input()) :
	s = raw_input().strip()
	r = ""
	n = len(s)
	l = []
	c = 0
	for i in range (n+1) :
		l.append(-1)

	for i in range (n-1) :
		if s[i] != s[i+1] :
			c += 1
			l[i] = c
			c = 0
		if s[i] == s[i+1] :
			c += 1
		if s[i] == s[i+1] and i+1 == n-1 :
			l[i+1] = c + 1
		
	c = 0
	for i in range (n) :
		if l[i] >= 2:
			if i != n-1 and abs(l[i]-i-1) != 0 :
				c += 1

			for j in range(2,l[i]+1) :
				c += int(math.ceil((l[i]*(1.0)/j*(1.0))*(1.0)))
				
			
	print c



