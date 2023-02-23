# 5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

## Example 1:

    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.

## Example 2:

    Input: s = "cbbd"
    Output: "bb"

## Constraints:

* 1 <= s.length <= 1000
* s consist of only digits and English letters.

## Summary

### Intuition

- we can't go from the front and back at the same time, we may have different strings
- for sure we could do a brute force which checks if a string is a palindrome this would be $O(n^2)$ time complexity
- there is a difference between even and odd length palindrome
- each palindrome has a break point -> where we can go in both directions 

### Approach

We are checking each possible break point. Each point can either indicate a single character or a two characters. 
Then we go both sides from this point and check how far we can count our palindrome.

### Complexity

- Time complexity: exponential $O(2^n)$

- Space complexity: linear $O(n)$

### Solution

https://leetcode.com/problems/longest-palindromic-substring/solutions/127837/longest-palindromic-substring/
