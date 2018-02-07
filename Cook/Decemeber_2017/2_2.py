for _ in range (input()) :
	n = input()
	l = map(int, raw_input().split())
	c = 0
	for i in l :
		if i%4 != 0 :
			c += 1
	print c/2
