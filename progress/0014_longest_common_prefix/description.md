# 14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

## Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

## Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

## Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

## Solution
- iterate through each word and change char_at by 1 thus we quite fast should find where is a common prefix - O(n^2) complexity
- another idea is to get common prefix between each, one after another, init prefix to val from first element, get common part, move to another -> do we have to iterate through characters? we will figure it out in a moment, we could just mock it with some extra function
- are these lists sorted? can they contain duplicates, can we convert them to some other representation?
- shall we sort first? extra time, I don't think we need it - would definitely speed up finding common, but if unsorted then maybe even faster?
- if we sort them first we could start with shortest word - common prefix cant' be longer that shortest word -> again not sure on sorting
- I could have added handling special cases as a solution, that way should work quite nice, like edge cases

https://leetcode.com/problems/longest-common-prefix/editorial/?envType=study-plan-v2&envId=top-interview-150