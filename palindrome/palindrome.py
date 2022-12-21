import re

def is_palindrome(str_to_check):
  '''
    @param str_to_check
    @return boolean
  '''
  str_to_check = re.sub('[^a-zA-Z0-9]', '', str_to_check.lower())
  start = 0
  str_len = len(str_to_check) - 1

  while start < str_len:
    if str_to_check[start] != str_to_check[str_len]:
      return False
    start += 1
    str_len -= 1
  
  return True

def is_palindrome_two(str_to_check):
  '''
    @param str_to_check
    @return boolean
  '''
  str_to_check = re.sub('[^a-zA-Z0-9]', '', str_to_check.lower())
  return str_to_check == str_to_check[::-1]
