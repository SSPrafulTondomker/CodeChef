
for _ in range (input()) :
	n = input()
	s = ""
	p = 4294967296
	k = p
	c = 0
	l = 100000
	for i in range(1,n+1) :
		if i <= 42949 :
			s += str(l) + " "
		else :
			s += str(1) + " "

	print s
