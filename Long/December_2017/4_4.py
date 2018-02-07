from collections import Counter

for _ in range (input()) :
	n = input()
	l = map(int, raw_input().split())
	a, b, c, d, s, x, pu = [], [], [], [], [], [], []

	for i in range (100001) :
		a.append(0)
		x.append(0)

	for i in range (n) :
		b.append(l[i])
		pu.append(l[i])

	c = Counter(b)
	l1, l2 = 0, 0

	for i in l :

		if c[i] == 2 and x[i] == 0:
			d.append(i)
			x[i] = 1
			l1 += 1
		elif c[i] == 1:
			s.append(i)
			l2 += 1

	if n >= 0 :

		d = d[l1-1:] + d[:l1-1]
		s = s[l2-1:] + s[:l2-1]
		j, k = 0, 0
	
		for i in range (n) :
			if c[l[i]] == 2 :
				if a[l[i]] == 0 :
					#print l[i],d[j]
					a[l[i]] = d[j]
					j += 1
			else :
				a[l[i]] = s[k]
				k += 1
		for i in range (n) :
			l[i] = a[l[i]]
		if l2 == 1 :
			for i in range (n) :
				if c[l[i]] == 1 :
					if i-1 >= 0 :
						l[i-1],l[i] = l[i],l[i-1]
					elif i+1 < n :
						l[i+1],l[i] = l[i],l[i+1]
					break
		elif l1 == 1 and l2 != 0:
			t = 0
			
			for i in range (n) :
				if c[l[i]] == 1 :
					d.append(i)
					t += 1
					if t == 2 :
						break
			t = 1
	
			for i in range (n) :
				if c[l[i]] == 2 :
					l[i] = l[d[t]]
					t += 1
			l[d[1]] = d[0]
			l[d[2]] = d[0]

					
		k = ""
		
		for i in l :
			k += str(i)+" "

	
		for i in range (n) :
			if l[i] == pu[i] :
				n -= 1
		print n
		print k
	


	

	
	
