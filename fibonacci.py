def fibonacci(position, memo = {}):
  ''' This function returns the nth number in a fibonacci sequence '''

  if position in memo:
    return memo[position]

  if position <= 2:
    return 1
  memo[position] = fibonacci(position - 1, memo) + fibonacci(position -2, memo)
  return memo[position]

print(fibonacci(40))
print(fibonacci(50))
print(fibonacci(60))