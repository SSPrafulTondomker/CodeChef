for _ in range (input()) :
	s = map(int,raw_input().split())
	r = raw_input().strip()
	l = "abcdefghijklmnopqrstuvwxyz"
	sum = 0
	for i in range(26) :
		if l[i] not in r :
			sum += s[i]
	print sum
