n = input()
l = map(int, raw_input().split())
m = input()
r = map(int, raw_input().split())
l.sort()
r.sort()
x = r[m-1]
x += 1
c = 0
for i in l :
	if i < x :
		c += x-i
print c
