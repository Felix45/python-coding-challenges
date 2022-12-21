def reverse_string(str):
  ''' Reverse string str by modifying input array in-place 0(1) extra memomory '''
  slowSlider = 0
  fastSlider = len(str) - 1

  while slowSlider < fastSlider:
    str[slowSlider], str[fastSlider] = str[fastSlider], str[slowSlider]
    slowSlider += 1
    fastSlider -= 1

  return str
