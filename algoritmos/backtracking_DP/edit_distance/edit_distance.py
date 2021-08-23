
def editDistance(str1, str2,m,n):

    if m == 0:
        return n



    if n == 0:
        return m

    # If last characters of two strings are same, nothing
    # much to do. Ignore last characters and get count for
    # remaining strings.


    if str1[ m - 1 ] == str2[ n - 1 ]:
        return editDistance(str1, str2, m- 1, n - 1)

    # If last characters are not same, consider all three
    # operations on last character of first string, recursively
    # compute minimum cost for all three operations and take
    # minimum of three values.


    return 1 + min(editDistance(str1, str2, m, n - 1),  # Insert
                   editDistance(str1, str2, m - 1, n),  # Remove
                   editDistance(str1, str2, m - 1, n - 1)  # Replace
                   )







if __name__ == '__main__':

    str1 = "patito"
    str2 = "pablito"


print(editDistance(str1,str2,len(str1),len(str2)))
