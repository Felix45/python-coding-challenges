def letter_combination(digits):
  ''' Returns all the possible letter combinations of [digits] '''
  if len(digits) == 0:
    return []
  
  letters = {
    '0': '',
    '1': '',
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
  }
  
  output = []
  queue  = ['']

  while len(queue) > 0:
    str = queue[0]
    del   queue[0]

    if len(str) == len(digits):
      output.append(str)
    else:
      current = letters[digits[len(str)]]
      for charc in current:
        queue.append(str+charc)
    
  return output
