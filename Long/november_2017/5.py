for _ in range (input()) :
	s = raw_input().strip()
	x,y = map(int, raw_input().split())
	r = ""
	ln = len(s)
	a = s.count('a')
	b = s.count('b')
	sz = 0
	if a == b :
		print 'ab'*a
	elif a == 0 :
		r = 'b'*y
		ln -= y
		b -= y
		while ln > 0 :
			if b >= y :
				r += '*'+'b'*y 
				ln -= y
				b -= y
			else :
				r += '*'+'b'*b
				ln -= b
				b -= b
		print r
	elif b == 0 :
		r = 'a'*x
		ln -= x
		a -= x
		while ln > 0 :
			if a >= x :
				r += '*'+'a'*x 
				ln -= x
				a -= x
			else :
				r += '*'+'a'*a
				ln -= a
				a -= a
		print r
	else :
		r = ''
		while a != 0 or b != 0 :
			#print ln,a,b
			if b == 0 :
				if a >= x :
					if r[len(r)-1] != 'a' :
						r += 'a'*x 
						sz += x 
						ln -= x
						a -= x
					else :
						r += '*' + 'a'*x
						sz += x + 1
						ln -= x
						a -= x
				else :
					if r[len(r)-1] != 'a' :
						r += 'a'*a
						a -= a
						ln -= a
						sz += a
					else :
						r += '*' + 'a'*a
						a -= a
						ln -= a
						sz += a + 1
			elif a == 0 :
				if b >= y :
					if r[len(r)-1] != 'b' :
						r += 'b'*y 
						sz += y
						ln -= y
						b -= y
					else :
						r += '*' + 'b'*y
						sz += y + 1
						ln -= y
						b -= y
				else :
					if r[len(r)-1] != 'b' :
						r += 'b'*b
						b -= b
						ln -= b
						sz += b
					else :
						r += '*'+ 'b'*b
						b -= b
						ln -= b
						sz += b + 1
			elif a == b :
				if r[len(r)-1] == 'a' :
					r += 'ba'*a
					ln -= a
					a -= a
					b -= b
					sz += a
				else :
					r += 'ab'*b
					ln -= b
					a -= a
					b -= b
					sz += b
 
			elif a > b and a != 0 and b != 0 :
				if len(r) == 0 :
					if a >= x and a-b >= x:
						r += 'a'*x 
						sz += x
						ln -= x
						a -= x
					elif a-b < x :
						r += 'a'*(a-b)
						ln -= (a-b)
						a -= (a-b)
					else :
						r += 'a'*a
						sz += a
						ln -= a
						a -= a
				else :
					if r[len(r) - 1] == 'a' :
						if b >= 1 :
							r += 'b'
							sz += 1
							ln -= 1
							b -= 1
						else :
							r += '*'
							sz += 1
					else :
						if a >= x and a-b >= x:
							r += 'a'*x
							sz += x
							ln -= x
							a -= x
						elif a-b < x :
							r += 'a'*(a-b)
							ln -= (a-b)
							a -= (a-b)
						else :
							r += 'a'*a
							sz += a
							ln -= a
							a -= a
 
 
			else :
				if len(r) == 0 :
					if b >= y and b-a >= y:
						r += 'b'*y 
						sz += y
						ln -= y
						b -= y
					elif b-a < y :
						r += 'b'*(b-a)
						ln -= (b-a)
						b -= (b-a)
					else :
						r += 'b'*b
						sz += b
						ln -= b
						b -= b
				else :
					if r[len(r) - 1] == 'b' :
						if a >= 1 :
							r += 'a'
							sz += 1
							ln -= 1
							a -= 1
						else :
							r += '*'
							sz += 1
					else :
						if b >= y and b-a >= y:
							r += 'b'*y
							sz += y
							ln -= y
							b -= y
						elif b-a < y :
							r += 'b'*(b-a)
							ln -= (b-a)
							b -= (b-a)
						else :
							r += 'b'*b
							sz += b
							ln -= b
							b -= b
		
		print r		
 
 
 
 
