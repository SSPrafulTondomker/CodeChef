import collections
p, y, w, r = [], [], [], []
for i in range (100001) :
	p.append(0)
	y.append(0)
	w.append(0)
	r.append(0)
for _ in range (input()) :
	n = input()
	l = map(int, raw_input().split())
	
	d, s = [], []
	a, b = 0, 0
	
	for i in range (100001) :
		r[i] = 0
	for i in l :
		r[i] += 1
	u = []

	for i in l :
		u.append(i)
	u = set(u)
	#print u
	for i in u :
		if r[i] == 2 :
			d.append(i)
			y[i] = 2
			a += 1
		else:
			s.append(i)
			y[i] = 1
			b += 1
	if a == 0 :
		if n != 1 :
			print n
		else :
			print n-1

		s = s[b-1:] + s[:b-1]
		k = ""
		for i in s :
			k += str(i) + " "
		print k

	elif b == 0 :

		p[d[0]] = d[a-1]
		j = 0
		for i in range(1,a) :
			p[d[i]] = d[j]
			j += 1

		for i in range (n) :
			l[i] = p[l[i]]
		if b == 1 :
			print n - 1
		else :
			print n
		k = ""
		for i in l :
			k += str(i)+" "
		print k
	else :
		if a != 1 :
			p[d[0]] = d[a-1]
			j = 0
		
			s = s[a-1:]+s[:a-1]

			for i in range (1,a) :
				p[d[i]] = d[j]
				j += 1
			j = 0
			for i in range (n) :
				if y[l[i]] == 2:
					l[i] = p[l[i]]
				else :
					l[i] = s[j]
					j += 1
			print n
			k = ""
			for i in l :
				k += str(i) + " "
			print k
		else :
			if a == 1 and b == 1 :
				print "2"
				f = 0
				for i in range (n) :
					if y[l[i]] == 2 and f == 0:
						l[i] = s[0]
						f = 1
					else :
						l[i] = d[0]
				k = ""
				for i in l :
					k += str(i) + " "
				print k

			else :
				j = 0
				for i in range (n) :
					if y[l[i]] == 2 :
						l[i] = s[j]
						j += 1
						w[i] = 1
			
				k = 0
				k2 = 0
				#print l,j
				for i in range (n) :
					if j < b and w[i] == 0:
						l[i] = s[j]
						j += 1
					elif w[i] == 0:
						l[i] = d[k]
						k2 += 1
						if k2 == 2 :
							k += 1
							k2 = 0
					
				g = ""
				for i in l :
					g += str(i)+" "
				print n
				print g
				
			 




