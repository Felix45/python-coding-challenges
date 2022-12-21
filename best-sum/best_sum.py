def best_sum(target_sum, numbers, memo = {}):
  ''' Returns the shortest array of elements that add upto the target sum '''
  if target_sum in memo:
    return memo[target_sum]

  if target_sum == 0:
    return []

  if target_sum < 0:
    return None

  shortestCombination = None

  for number in numbers:
    remainder = target_sum - number
    remainder_result = best_sum(remainder, numbers, memo)
    if remainder_result != None:
      newCombination = remainder_result + [number]
      if shortestCombination == None or len(newCombination) < len(shortestCombination):
        shortestCombination = newCombination
        memo[target_sum] = shortestCombination

  memo[target_sum] = shortestCombination
  return shortestCombination
