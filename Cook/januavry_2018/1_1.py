def mini (x, n, k, s) :
	t = x*n
	i = 1
	while i <= s :
		#print i,t
		if t < k :
			return 0
		if i%7 != 0 :
			x -= 1
		else :
			x = x
		t -= k
		i += 1
	
	if x > 0 :
		return 0
	if x <= 0 and t >= 0:
		return 1
	else :
		return -1

def bs(p, l, r ,n, k, s) :
	while l <= r :
		tr = mini(l, n, k, s)
		if tr == 1:
			return l
		l += 1
	return -1

for _ in range (input()) :
	n, k, s = map(int, raw_input().split())
	p = []
	for i in range (s+1) :
		p.append(i)
	print bs(p, 1, s, n, k, s)
	
