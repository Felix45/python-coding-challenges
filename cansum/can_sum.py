def can_sum(target_sum, arr, memo={}):
  ''' Returns boolean (true) if the elements of an array can sum up to target sum '''
  if target_sum in memo:
    return memo[target_sum]

  if target_sum == 0:
    return True

  if target_sum < 0:
    return False

  for number in arr:
    new_target_sum = target_sum - number
    if can_sum(new_target_sum, arr, memo) == True:
      memo[target_sum] = True
      return True

  memo[target_sum] = False  
  return False   