def lcs(text1, text2):
  ''' returns the length of the longest common subsequence '''
  m = len(text1)
  n = len(text2)
  table = [[0 for j in range(0, n + 1)] for i in range(0, m+1)]

  for i in range(1, m+1):
    for j in range(1, n+1):
      if text1[i - 1] == text2[j - 1]:
        table[i][j] = table[i-1][j-1] + 1
      else:
        table[i][j] = max(table[i-1][j], table[i][j-1])
  
  return table[m][n]
        

