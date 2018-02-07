from sets import Set
from collections import Counter

for _ in range (input ()) :
	n,k = map(int,raw_input().split())
	l = map(int,raw_input().split())
	r = []
	m = Set(l)
	for i in range (200001) :
		r.append(i)
	cnt = Counter (r)
	cmt = Counter (m)
	cmt.subtract(cnt)
	for i in r :
		if cmt[i] == -1 and k > 0:
			k -= 1
			cmt[i] = 0
		if k == 0 :
			break
	
	for j in range (i,200001) :
		if cmt[j] == -1 :
			print j
			break
	

