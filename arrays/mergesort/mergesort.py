def mergesort(A,n):
    '''
      returns a sorted array
    '''
    print(A)
    if len(A) == 1:
      return A

    listA = A[0:n//2]
    listB = A[n//2:]

    return merge(mergesort(listA, len(listA)), mergesort(listB, len(listB)))

def merge(listA, listB):
    '''
      returns a merged sorted array containing elements from listA
      and listB 
    '''
    i = 0
    j = 0
    output = []

    while i < len(listA) and j < len(listB):
        if listA[i] < listB[j]:
          output.append(listA[i])
          i += 1
        else:
          output.append(listB[j])
          j += 1

    while i < len(listA):
        output.append(listA[i])
        i += 1

    while j < len(listB):
        output.append(listB[j])
        j += 1

    return output
