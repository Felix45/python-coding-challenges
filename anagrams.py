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

def get_letters_count(str):
  ''' Returns the total count of letters in a string '''
  letters_count = {}
  
  for letter in str:
    if letter in letters_count:
      letters_count[letter] += 1
    else:
      letters_count[letter] = 1
  
  return letters_count

def are_anagrams_three(str_one, str_two):
  ''' Checks if two strings are anagrams by checking the count of letters in each string '''
  if len(str_one) != len(str_two):
    return False

  letters_in_str_one = get_letters_count(str_one.lower())
  letters_in_str_two = get_letters_count(str_two.lower())

  for letter in letters_in_str_one:
    if letters_in_str_one[letter] != letters_in_str_two[letter]:
      return False

  return True

print(are_anagrams('Listen', 'Silent'))
print(are_anagrams_two('ttew', 'tetw'))
print(are_anagrams_three('Restful', 'Fluster'))

