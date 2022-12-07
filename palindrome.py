def is_palindrome(str_to_check):
  '''
    @param str_to_check
    @return boolean
  '''
  start = 0
  str_len = len(str_to_check) - 1

  while start < str_len:
    if str_to_check[start] != str_to_check[str_len]:
      return False
    start += 1
    str_len -= 1
  
  return True

