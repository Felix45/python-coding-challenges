def sort_by_frequency(s):
  ''' Sorts a string s by the frequency of characters and returns the sorted string '''
  table = {}
  temp  = []
  result = ''

  for i in range(len(s)):
    if s[i] in table:
      table[s[i]] += s[i]
    else:
      table[s[i]] = s[i]

  for letter in table:
    temp.append([letter, table[letter]])

  temp.sort(reverse=True, key=lambda x: (len(x[1]) or x[0]))
  
  for j in range(len(temp)):
    result += temp[j][1]

  return result
