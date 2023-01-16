def search_insert_index(nums, target):
  '''
    return the index if the target is found.
    If not, return the index where it would be if it were inserted in order.
  '''
  low = 0
  high = len(nums) - 1
  mid = (low + high) // 2

  while low < high:
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        high = mid - 1
    elif nums[mid] < target:
        low = mid + 1
    mid = (low + high) // 2

  if mid < 0:
    return 0

  if nums[mid] < target:
    return mid + 1

  return mid