def search(arr, low, high):
     
    # Base case
    if low > high:
        return None
    if low == high:
        return arr[low]
 
    # Find the middle point
    mid = (low + high)/2;
 
    # If mid is even
    if mid%2 == 0:
         
        # If the element next to mid is same as mid,
        # then output element lies on right side,
        # else on left side
        if arr[mid] == arr[mid+1]:
            return search(arr, mid+2, high)
        else:
            return search(arr, low, mid)
 
    else:
        # else if mid is odd
 
        if arr[mid] == arr[mid-1]:
            return search(arr, mid+1, high)
        else:
            # (mid-1) because target element can only exist at even place
            return search(arr, low, mid-1)
 
 
# Test array
arr = [ 1, 1, 2, 2, 1, 1, 2, 2, 13, 1, 1, 40, 40 ]
 
result = search(arr, 0, len(arr)-1 )
 
if result is not None:
    print "The required element is %d " % result
else:
    print "Invalid array"
