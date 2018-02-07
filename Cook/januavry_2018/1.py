
import math
 
for _ in range (input()) :
	n, k, s = map(int, raw_input().split()) 
	if n < k :
		print "-1"
	else :
		p = 1
		df = n
		c = 1
		f = 0
		i = 1
		while i<=s :
			n -= k
			#print n, i
			if n < k and p%7 != 0 and i!=s:
				n += df
				c += 1
			elif (p+1)%7 == 0 and n-k < k:
				n += df
				c += 1
			elif p%7 == 0 and n < k :
				f = 1
				break
			p += 1
			
			i += 1
		if f == 1 :
			print "-1"
		else :
			print c
		
