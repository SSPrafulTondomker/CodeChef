for _ in range (input()) :
	n = input()
	s = map(int,raw_input().split())
	f = 0
	for i in s :
		f = f|i
	print f
