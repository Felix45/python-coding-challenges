def how_sum(target_sum, numbers, memo = {}):
  ''' Returns an array of elements that add upto the target sum '''

  if target_sum in memo:
    return memo[target_sum]

  if target_sum == 0:
    return []
  if target_sum < 0:
    return None

  for number in numbers:
    remainder_sum = target_sum - number
    remainder_result = how_sum(remainder_sum, numbers, memo)
    if remainder_result != None:
      memo[target_sum] = remainder_result + [number]
      return memo[target_sum]

  memo[target_sum] = None
  return None
