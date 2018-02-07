n, m, q = map(int, raw_input().split())
wq, cost, cnt, e, h, c = [], [], [], [], [], 0
for _ in range (m) :
	p = (map(int,raw_input().split()))
	cost.append(p[:2])
	cnt.append(p[2:])
s = 10000000
f = 0
for _ in range (n+1) :
	wq.append(0)
for _ in range (q) :
	a, b = map(int, raw_input().split())
	if a > b :
		a, b = b, a
	if s > a :
		s = a
	if f < b :
		f = b
for i in cnt :
	c += 1
	e.append(c+1)
	for j in i :
		wq[j] = 1
		#print wq.count(1),i
	if wq.count(1) == abs(b-a ) + 1 :
		break
	

re = len(e)
print re
if re%2 == 0 :
	for i in range (re-1) :
		print e[i],e[i+1]
else :
	for i in range (re-2) :
		print e[i],e[i+1]
	print e[re-1]

