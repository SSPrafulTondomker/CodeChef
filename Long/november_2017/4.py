for _ in range (input()) :
	n = input()
	l = []
	for i in range (n) :
		r = map(int,raw_input().split())
		p = r[1:]
		p.sort()
		p = p[::-1]
		r = r[0:1]+p
		l.append(r)
		
	Sum = 0
	for i in range (n-1) :
		r = l[i]
		p = l[i+1]
		lf = r[r[0]]
		rf = p[1]
		Sum += abs (lf-rf)*(i+1)
	print Sum

	

	
	




	
