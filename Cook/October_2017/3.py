for _ in range (input()) :
	s = raw_input().strip()
	n = len(s) 
	r = "abcdefghijklmnopqrstuvwxyz"
	c = 0
	if n <= 1 :
		print "0"
	else :

		for i in range (n) :
			for j in range (i+1,n) :
				if s[i] == s[j] and j == i+1 :
					c += 1
				elif s[i] == s[j] and j != i+1 :
					p = 0
					for k in r :
						if k in s[i+1:j] :
							p += 1
						if p >= 2 :
							break
					if p == 1 :
						c += 1
		print c

