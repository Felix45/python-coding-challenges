def all_construct(target_word, word_bank):
  '''
    Returns an array containing all the ways that the `target` can be constructed
    by concatenating elements of the `word_bank` array
  '''

  if target_word == '': return [[]]

  result = []

  for word in word_bank:
    if target_word.startswith(word):
      suffix = target_word[len(word):]
      suffix_ways = all_construct(suffix, word_bank)
      target_ways = []
      for suffix_way in suffix_ways:
        if isinstance(suffix_way, list):
          suffix_way.insert(0, word)
          target_ways.append(suffix_way[:])
        
      result += target_ways
    
  return result
