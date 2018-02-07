n = input()
l = map(int,raw_input().split())
i = n
while i != 0 :
	if l[i] != 0 :
		break
	i -= 1
if n == 0 or i == 0:
	if l[0] < 0 :
		print "-1 -1"
	elif l[0] == 0 :
		print "0 0"
	else :
		print "1 1",l[0]
if l[i] < 0 and n != 0:
	if i%2 == 0 :
		print "-1 -1"
	else :
		print "-1 1"
elif n != 0 :
	if i%2 == 0 :
		print "1 1"
	else :
		print "1 -1"

