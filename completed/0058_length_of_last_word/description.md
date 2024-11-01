# 58. Length of Last Word
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

## Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

## Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

## Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

## Constraints:
1 <= s.length <= 10^4
s consists of only English letters and spaces ' '.
There will be at least one word in s.

## Analysis
- this looks like an easy problem, I wonder if handling special case is needed
- simple solution would be having two indexes: 1st for 1st char and 2nd for last char and we iterate through this string
- time complexity O(n)
- we could also use regular expression, it would look something like this .*?(\w+)\s*$ -> we would still have to check if it's greedy or non greedy regexp
- I added a bool to indicate if we are in the word already, I wonder if we can do it without it, maybe if we init both with negative value?
- regexp solution is slower than final but consumes a tiny bit less memory
- thing which I didn't think about was to start from the end as we are looking just for a last word -> keep in mind reverting words, starting from the end has this benefit that could speed up the whole process
- also we could use str.split() function but that's quite obvious

## Solution
https://leetcode.com/problems/length-of-last-word/editorial


