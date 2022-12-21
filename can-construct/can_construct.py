def can_construct(target_string, word_bank, memo={}):
  '''
    Returns a boolean indicating whether or not the `target` 
    can be constructed by concatenating elements of the `word_bank` array.
  '''
  if target_string in memo: return memo[target_string]
  if target_string == '': return True

  for word in word_bank:
    if target_string.startswith(word):
      new_target_str = target_string[len(word):]
      if can_construct(new_target_str, word_bank) == True:
        memo[target_string] = True
        return True

  memo[target_string] = False
  return False