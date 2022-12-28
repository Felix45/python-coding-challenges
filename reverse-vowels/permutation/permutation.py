def getPermutations(str):
  if len(str) == 0:
    return [str]
  
  output = []
  for index in range(len(str)):
    currentLetter = str[index]
    remainingLetter = str[0:index] + str[index+1:]

    permutations = getPermutations(remainingLetter)
    
    for letter in permutations:
        output.append(currentLetter+letter)

  return output

print(getPermutations('aboo'))