from math import ceil, floor, log

MAX = 1000


def sieveOfEratosthenes(isPrime):
    isPrime[1] = False

    for p in range(2, MAX + 1):
        if p * p > MAX:
            break

        # If prime[p] is not changed, then
        # it is a prime
        if (isPrime[p] == True):

            # Update all multiples of p
            for i in range(2 * p, MAX + 1, p):
                isPrime[i] = False


def getMid(s, e):
    return s + (e - s) // 2


def queryPrimesUtil(st, ss, se, qs, qe, index):

    if (qs <= ss and qe >= se):
        return st[index]

    if (se < qs or ss > qe):
        return 0

    mid = getMid(ss, se)
    return queryPrimesUtil(st, ss, mid, qs, qe, 2 * index + 1) + \
           queryPrimesUtil(st, mid + 1, se, qs, qe, 2 * index + 2)


def updateValueUtil(st, ss, se, i, diff, si):

    if (i < ss or i > se):
        return

    st[si] = st[si] + diff
    if (se != ss):
        mid = getMid(ss, se)
        updateValueUtil(st, ss, mid, i, diff, 2 * si + 1)
        updateValueUtil(st, mid + 1, se, i, diff, 2 * si + 2)

def updateValue(arr, st, n, i, new_val, isPrime):

    if (i < 0 or i > n - 1):
        print("Invalid Input")
        return

    diff, oldValue = 0, 0

    oldValue = arr[i]

    arr[i] = new_val


    if (isPrime[oldValue] and isPrime[new_val]):
        return


    if ((not isPrime[oldValue]) and (not isPrime[new_val])):
        return


    if (isPrime[oldValue] and not isPrime[new_val]):
        diff = -1


    if (not isPrime[oldValue] and isPrime[new_val]):
        diff = 1


    updateValueUtil(st, 0, n - 1, i, diff, 0)



def queryPrimes(st, n, qs, qe):
    primesInRange = queryPrimesUtil(st, 0, n - 1, qs, qe, 0)

    print("Numeros primos en el rango ", qs, " to ", qe, " = ", primesInRange)


def constructSTUtil(arr, ss, se, st, si, isPrime):

    if (ss == se):

        if (isPrime[arr[ss]]):
            st[si] = 1
        else:
            st[si] = 0

        return st[si]


    mid = getMid(ss, se)
    st[si] = constructSTUtil(arr, ss, mid, st, si * 2 + 1, isPrime) + \
             constructSTUtil(arr, mid + 1, se, st, si * 2 + 2, isPrime)
    return st[si]

def constructST(arr, n, isPrime):

    x = ceil(log(n, 2))

    max_size = 2 * pow(2, x) - 1

    st = [0] * (max_size)


    constructSTUtil(arr, 0, n - 1, st, 0, isPrime)


    return st



if __name__ == '__main__':
    arr = [2,4,7,8,10,1]
    n = len(arr)


    isPrime = [True] * (MAX + 1)
    sieveOfEratosthenes(isPrime)


    st = constructST(arr, n, isPrime)


    a = 2
    b = 6
    queryPrimes(st, n, a, b)

