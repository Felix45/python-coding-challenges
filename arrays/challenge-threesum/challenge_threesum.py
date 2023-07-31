def three_sum(A):
  ''' Return triplets that sum to zero '''
  A.sort()
  triplets   = []
  duplicates = set()

  for num in range(len(A) - 2):
    left = num + 1
    right = len(A) - 1

    while left < right:
      summation = A[num] + A[left] + A[right]
      
      if summation == 0:
        num_str = str(A[num]) + ' ' + str(A[left]) + ' ' + str(A[right])
        if num_str not in duplicates:
          triplets.append([A[num], A[left], A[right]])
        duplicates.add(num_str)
        left  += 1
        right -= 1
      elif summation < 0:
        left += 1
      else:
        right -= 1

  return triplets
