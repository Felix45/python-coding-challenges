def can_sum(target_sum, arr):
  ''' Returns boolean (true) if the elements of an array can sum up to target sum '''
  
  if target_sum == 0:
    return True

  if target_sum < 0:
    return False

  for number in arr:
    new_target_sum = target_sum - number
    if(can_sum(new_target_sum, arr) == True):
      return True

  return False   