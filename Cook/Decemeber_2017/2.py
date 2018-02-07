import collections

for _ in range (input()) :
	n = input()
	l = map(int, raw_input().split())
	c = collections.Counter(l)
	#c.update(l)
	for i in c :
		print i,c[i]

	
	
