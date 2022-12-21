from collections import Counter

def are_anagrams(str_one, str_two):
  ''' Check if two strings are anagrams '''
  
  return Counter(str_one.strip().lower()) == Counter(str_two.strip().lower())


def are_anagrams_two(str_one, str_two):
  ''' Check if two strings are anagrams '''

  str_one = sorted(str_one.strip().lower())
  str_two = sorted(str_two.strip().lower())

  if len(str_one) != len(str_two):
    return False

  return str_one == str_two

def are_anagrams_three(str_one, str_two):
  ''' Checks if two strings are anagrams by counting the frequecny of individual letters '''
  if len(str_one) != len(str_two):
    return False
  
  str_one = str_one.lower()
  str_two = str_two.lower()

  for letter in str_one:
    if str_one.count(letter) != str_two.count(letter):
      return False

  return True

print(are_anagrams('Listen', 'Silent'))
print(are_anagrams_two('ttew', 'tetw'))
print(are_anagrams_three('ResTfuL', 'FLUSter'))

