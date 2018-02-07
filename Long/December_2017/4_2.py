for _ in range (input()) :
	n = input()
	l = map(int,raw_input().split())
	s = ""
	s = str(l[n-1])
	for i in range (n-1) :
		s += " "+str(l[i])
	if n != 1 :
		print n
	else :
		print n-1
	print s

