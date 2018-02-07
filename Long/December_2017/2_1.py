def call(f, sc, j) :
	if f > sc :
		print "TEAM-A", j
	else :
		print "TEAM-B", j
def pA(j) :
	print "TEAM-B",j
def pB(j) :
	print "TEAM-A",j
def pT() :
	print "TIE"
def me () :
	a = 10
	for i in range (10) :

		if a+1 < 20 and s[a] == "1" and s[a+1] == "0" :
			pB(a+2)
			break
		if a+1 < 20 and s[a] == "0" and s[a+1] == "1" :
			pA(a+2)
			break
		if a+1 >= 20 :
			pT()
			break
		a += 2

while True:
	try:
		s = raw_input()
		if s == "" or len(s) == 0:
			break
	except EOFError:
		break

	if len(s)> 19 :
		s = s.strip()
		f, sc, a, b = 0, 0, 5, 5
		j = 0
		for i in range (5) :

			if s[j] == "1" :
				f += 1
			a -= 1
			j += 1
			if f+a < sc or sc+b < f:
				call(f,sc,j)
				break
			if s[j] == "1" :
				sc += 1
			b -= 1
			j += 1
			if f+a < sc or sc+b < f:
				call(f,sc,j)
				break
			

		if f == sc :
			me()


			

