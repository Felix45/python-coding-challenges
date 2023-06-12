def kth_largest_number(A,k):
    ''' Returns K large elements in decreasing order '''
    A.sort()
    A = A[::-1]

    return A[0:k]