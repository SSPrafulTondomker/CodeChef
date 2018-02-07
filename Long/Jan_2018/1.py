for _ in range (input()) :
	n = input()
	l = map(int,raw_input().split())
	e, o = 0, 0
	for i in l :
		if i%2 == 0 :
			e += 1
		else :
			o += 1
	if e == n :
		print "1"
	elif o == n :
		if n%2 == 0 :
			print "1"
		else :
			print "2"
	elif o%2 != 0 :
		print "2"
	else :
		print "1"

