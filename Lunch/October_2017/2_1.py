for _ in range (input()) :
	n,k = map(int,raw_input().split())
	r = pow(2,n)
	i = 1
	while i != 0 :
		if k > r+1 :
			g = r+1
			i = 0
		n -= 1
		r = pow(2,n)
	print g,k
	g = n-g
	e = pow(2,g)*k
	print e

