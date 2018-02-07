n, q = map(int, raw_input().split())
l = map(int, raw_input().split())
for _ in range (q) :
	t, j, a = map(int, raw_input().split())
	if t == 1 :
		l[j-1] = a
	else :
		i = j
		c = 0
		s = 0
		for k in range (i) :
			s ^= l[k]
			if s == a :
				c += 1
	
	
		print c
