## Valid Anagram Coding challenge
> Given two strings `s` and `t`, return `true` if `t` _is an anagram of `s`, and `false` otherwise_.
An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Constraints
- 1 <= s.length, t.length <= 5 * 104
- `s` and `t` consist of lowercase English letters.

## Example 1
```Python
  Input: s = "anagram", t = "nagaram"
  Output: true
```
Explanation: "anagram" and "nagram" have equal letter frequencies.

## Example 2
```Python
  Input: s = "rat", t = "car"
  Output: false
```
Explanation: "rat" and "car" have different letter frequencies.

