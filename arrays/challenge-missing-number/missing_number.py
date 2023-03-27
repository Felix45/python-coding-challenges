def missing_number(A):
  ''' returns the smallest positive integer that does not occur in A '''

  numbers = set(A)

  range_of_numbers = len(A) + 2

  for num in range(1, range_of_numbers):
    if num not in numbers:
      return num