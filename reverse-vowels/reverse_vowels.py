def reverse_vowels(st):
  ''' Return str with all vowels in the string reversed '''

  st = list(st)
  vowels = 'aeiou'

  leftSlider = 0
  rightSlider = len(st) - 1

  while leftSlider < rightSlider:
    if st[leftSlider].lower() in vowels and st[rightSlider].lower() in vowels:
      st[leftSlider], st[rightSlider] = st[rightSlider], st[leftSlider]
      leftSlider += 1
      rightSlider -= 1
    else:
      if st[leftSlider] not in vowels:
        leftSlider += 1
    
      if st[rightSlider] not in vowels:
        rightSlider -= 1
  print(st)
  return ''.join(map(str,st))
