def getPermutations(str):
  if len(str) == 0:
    return [str]
  
  output = []

  for i in range(0, len(str)):
    currentLetter = str[i]
    remainingLetter = str[0:i] + str[i+1:]

    perms = getPermutations(remainingLetter)

    for letter in perms:
      output.append(currentLetter+letter)

  return output
  

def permutation_sequence(number, k):
    ''' Get the kth permutation of permutation string '''

    fact = []
    while number > 0:
      fact.append(str(number))
      number -= 1

    permutations = getPermutations("".join(fact[::-1]))
    print(permutations)

    return permutations[k-1]


print(permutation_sequence(4,9))