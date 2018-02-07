import collections

p, b = [], []
for i in range (100001) :
	p.append(0)
	b.append(0)

for _ in range (input()) :
	n = input()
	l = map(int,raw_input().split())
	v = []
	
	d, s = [], []

	count = collections.Counter(l)
	e, c = 0, 0

	for i,j in zip(count.keys(),count.values()) :
		p[i] = j
		if j == 2 :
			d.append(i)
			d.append(i)
			c += 1
		else :
			s.append(i)
			e += 1
	j = 0
	e = len(s) - 1
	c = len(d) - 1
	for i in range (n) :
		v.append(l[i])
		
	for i in range (n) :
		if l[i] in d :
			if e - 1 != 0 :
				k = l[i]
				l[i] = s[e]
				e -= 1
				l.replace(k,s[e],1)
				e -= 1
			elif e == 1 :
				g 
				

	print l

	




			

	


