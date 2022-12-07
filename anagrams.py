from collections import Counter

def are_anagrams_two(str_one, str_two):
  ''' Check if two strings are anagrams '''

  str_one = str_one.strip().lower()
  str_two = str_two.strip().lower()

  if(len(str_one) != len(str_two)):
    return False

  for letter in str_one:
    if letter not in str_two:
      return False
    
  return True


print(are_anagrams_two('Listen', 'Silent'))
