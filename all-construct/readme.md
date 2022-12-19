## All Construct Coding challenge
> Write a function `all_construct` that takes in a target string and an array of strings as arguments. The function
should return a 2D array containing all the ways that the `target` can be constructed by concatenating elements of the `word_bank` array.
Each element of the 2d array should represent one combination that constructs the `target`.

## Constraints
- You may use an element of the `word_bank` array as many times as needed.

## Examples
```Python
  all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'ef', 'abcd', 'c']) => [
    ['ab', 'cd', 'ef'],
    ['ab', 'c', 'def'],
    ['abc', 'def'],
    ['abcd', 'ef']
  ]
  all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']) => [
    ['purp', 'le'],
    ['p', 'ur', 'p', 'le']
  ]
  all_construct('hello', ['cat', 'dog', 'mouse']) => []

```
