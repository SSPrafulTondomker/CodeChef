a,b = map (int,raw_input().split())
p = 0
def per(c) :
	if pow(c,0.5)*pow(c,0.5) == c :
		return 1
	else :
		return 0
for i in range (1,a) :
	for j in range (1,b) :
		c = (i*i) + j
		if per(c) == 1 :
			p += 1
			print i,j,pow(c,0.5)*pow(c,0.5)
print p
