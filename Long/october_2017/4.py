n, q = map(int, raw_input().split())
p = []

for _ in range (300002) :
	p.append(0)

for _ in range (n) :
	x,y = map(int, raw_input().split())
	p[x] = y

for _ in range (q) :
	x1, y1, x2, y2 = map (int, raw_input().split())
	s = 0 
	for i in range (x1,x2+1) :
		if s < p[i] :
			s = p[i]
	if s > 0 :
		height1 = abs (s - y1) + 1
		distance = abs (x2 - x1)
		height2 = abs (s - y2) + 1
	else :
		height1 = 0
		distance = abs (x2-x1)  
		height2 = 0
	print height1+distance+height2

	

