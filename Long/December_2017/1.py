for _ in range (input()) :
	n,m = map(int,raw_input().split())
	l = []
	g, r = 0, 0 
	q, w = "", ""
	for i in range (n) :
		l.append(raw_input().strip())
	for i in range (501) :
		q += "RG"
		w += "GR"

	# if R
	for i in range (n) :
		for j in range (m) :
			if i%2 == 0 :
				if l[i][j] != q[j] :
					if q[j] == "G" :
						g += 5
					else :
						g += 3
				if l[i][j] != w[j] :
					if w[j] == "G" :
						r += 5
					else :
						r += 3
			else :
				if l[i][j] != w[j] :
					if w[j] == "G" :
						g += 5
					else :
						g += 3
				if l[i][j] != q[j] :
					if q[j] == "G" :
						r += 5
					else :
						r += 3

	if g >= r :
		print r
	else :
		print g



