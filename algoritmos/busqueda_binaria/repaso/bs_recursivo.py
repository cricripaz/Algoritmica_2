
"""

l = left
r = right
x = elemento buscado

"""

def binarySearch(arr, l, r, x):

    if r >= l:
        mid = l + (r - l) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1






arr = range(10)


x = 9

res = binarySearch(arr ,0 ,len(arr)-1 , x)

if res != -1 :
    print(" Elemnto Si existe ")
else:
    print(" Elemento no existe ")

