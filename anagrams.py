from collections import Counter

def are_anagrams_two(str_one, str_two):
  ''' Check if two strings are anagrams '''

  str_one = sorted(str_one.strip().lower())
  str_two = sorted(str_two.strip().lower())

  if len(str_one) != len(str_two):
    return False

  return str_one == str_two

def are_anagrams(str_one, str_two):
  ''' Check if two strings are anagrams '''
  
  return Counter(str_one.strip().lower()) == Counter(str_two.strip().lower())


print(are_anagrams_two('tetw', 'ttew'))
