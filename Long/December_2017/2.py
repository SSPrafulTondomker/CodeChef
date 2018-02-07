l = []
while True:
	try:
		k = raw_input()
		if (len(k) < 10) :
			break
		l.append(k)
	except EOFError:
		break
	if k == '' :
		break
	if len(k) < 10 :
		break

for p in l :
	k = p.strip()
	shot = 5
	A, B = 0, 0
	#for i in range (10) :
	#	if shot <= abs (A-B) :
	#		break
	#	if i%2 == 0 :
	#		if int(k[i]) == 1 :
	#			A += 1
	#	else :
	#		if int (k[i]) == 1 :
	#			B += 1
	#			shot -= 1
	if A > B :
		print "TEAM-A",i+1
	elif B > A :
		print "TEAM-B",i+1
	else :
		i = 10
		while i < 20 :

			if i%2 == 0 :
				if int(k[i]) == 1:
					A += 1
			i += 1
			if i%2 != 0 :
				if int(k[i]) == 1:
					B += 1
			if A > B or B < A :
				break
			i += 1


		if A > B :
			print "TEAM-A",i+1
		elif B < A:
			print "TEAM-B",i+1
		else :
			print "TIE"

