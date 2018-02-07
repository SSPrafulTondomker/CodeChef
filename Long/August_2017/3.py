s = map(int,raw_input().strip())
n = input()
l = map(int,raw_input().strip())
sl = []
ll = []
kt = 0
ll = [0,0,0,0,0,0,0,0,0,0]
for i in s :
	if i in l :
		sl.append(1)
	else :
		sl.append(0)
	kt += 1
c,f = 0,0
for i in range (kt) :
#	print sl[i]
	if sl[i] == 1 :
		ll[sl[i]] = 1;
#		print "j"
		for y in range (i,kt) :
			print ll,y,kt,l,sl[y]
			if sl[y] == 1 :
				ll[y] = 1
			if ll.count(1) == n :
				c += kt-y
				for j in range (11) :
					ll[i] = 0;
				break
	else :
		ll[sl[i]] = 1;
		for y in range (i,kt) :
			if sl[y] == 1 :
				ll[y] = 1
			if ll.count(1) == n :
				c += kt-y
				for j in range (11) :
					ll[i] = 0
				break
		c *= 2
		
print c

