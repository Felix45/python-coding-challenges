def fibonacci(position):
  ''' This function returns the nth number in a fibonacci sequence '''
  if position <= 2:
    return 1
  return fibonacci(position - 1) + fibonacci(position -2)

print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))