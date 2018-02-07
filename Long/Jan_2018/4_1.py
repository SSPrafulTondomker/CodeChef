def getsum(BITTree,i):
    s = 100000000 
    i = i+1
    while i > 0:
	    if s > BITTree[i] :
		    s = BITTree[i]
            i -= i & (-i)

    return s
 
def updatebit(BITTree , n , i ,v):
    i += 1
    while i <= n:
	    if BITTree[i] > v :
		    BITTree[i] = v
            i += i & (-i)
 
def construct(arr, n):
    BITTree = [1000000]*(n+1)
    for i in range(n):
        updatebit(BITTree, n, i, arr[i])
    return BITTree
 
if __name__ == '__main__': 
	freq = map(int, raw_input().split())
	BITTree = construct(freq,len(freq))
	print( getsum(BITTree,input()))
	print(getsum(BITTree,input()))
