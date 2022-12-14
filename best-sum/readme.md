## BestSum Coding challenge
> Write a function `best_sum` that takes in a target sum and an array of numbers as arguments. The function
should return an array containing the shortest combination of elements that add up to exactly the target sum. If there is no combination that adds up to the target sum,
then return None.

## Constraints
- You may use an element of the array as many times as needed.
- You may assume that all input numbers are nonnegative
- If there are multiple shortest combinations possible, you may return any single combination

## Examples
```
  best_sum(7, [5, 3, 4, 7]) => [7]
  best_sum(7, [2, 4]) => None
  best_sum(300, [7, 14]) => None
  best_sum(100, [1, 2, 5, 25], {})  => [25, 25, 25, 25]
```
