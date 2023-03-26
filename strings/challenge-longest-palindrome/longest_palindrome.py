def expand(str, begin, end):
  while begin >= 0 and end <= end and str[begin] == str[end]:
    begin -= 1
    end   += 1

  return str[(begin + 1):end]

def longest_palindrome(str):
  if len(str) <= 0:
    return str
  
  longest = str[0:1]
  
  for i in range(0, len(str) - 1):
    temp = expand(str, i, i)

    if len(temp) > len(longest):
      longest = temp

    temp = expand(str, i, i+1)

    if len(temp) > len(longest):
      longest = temp

  return longest