



def binarySearchRecursive(arr, left, right, x):

    if (right >= left):

        mid = left + (right - left) // 2

        if (arr[mid] == x):
            return mid
        elif (arr[mid] > x):
            return binarySearchRecursive(arr, left, mid - 1, x)
        else:
            return binarySearchRecursive(arr, mid + 1, right, x)

    else:
        return -1





if __name__ == '__main__':

    '''
    x = elemento buscado 
    '''
    arr = [2,4,6,8,10,12,14,16,18,20,22,24,26]

    x = 13

    res = binarySearchRecursive(arr , 0 , len(arr) - 1 , x)

    print("Si existe" if res != -1 else "No Existe")


