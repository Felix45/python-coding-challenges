def median(median = 0, median_two = 0):
  '''
    return average median
  '''
  return (median + median_two) / 2

def linear_median_sorted(listA, listB):
    '''
      return the median of the two sorted arrays using
      two pointers approach
    '''
    i, j = 0, 0
    
    output = []

    while i < len(listA) and j < len(listB):
      if listA[i] <= listB[j]:
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

    length = len(output)
    if(length % 2 == 0):
      return median(output[length // 2], output[length // 2 - 1])
    
    return median(output[length // 2])




