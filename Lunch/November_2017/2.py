for _ in range (input()) :
	n = input()
	l = map(int,raw_input().split())
	c = 0
	i = 0
	while i < n :
		j = i+1
		while j < n :
			if l[i]|l[j] <= max (l[i],l[j]) :
				c += 1
			j += 1
		i += 1
	print c
