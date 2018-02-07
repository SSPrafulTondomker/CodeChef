for _ in range (input()) :
	l = []
	p = map(int,raw_input().split())
	l = p
	n = len(l)
	n -= 1
	s = 0
	l.sort()
	if l[n] == n :
		print l[n-1]
	else :
		print l[n]


