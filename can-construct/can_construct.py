def can_construct(target_string, word_bank):
  '''
    Returns a boolean indicating whether or not the `target` 
    can be constructed by concatenating elements of the `word_bank` array.
  '''

  if target_string == '':
    return True

  for word in word_bank:
    if target_string[0:len(word)] == word:
      new_target_str = target_string[len(word):]
      if can_construct(new_target_str, word_bank) == True:
        return True

  return False