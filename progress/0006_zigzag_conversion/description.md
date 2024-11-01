# 6. Zigzag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 
## Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

## Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

## Example 3:
Input: s = "A", numRows = 1
Output: "A"

## Constraints:
1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000

## Analysis
- need to create two dimensional array or list of hashes where a key is a point in this system, and value a letter, with that we don't have to expand list with empty chars, which we could and combining would be much faster -> we can do it probably with lambda as we operate on the stream 
- actually we don't need even to store points but chars
- for this case we keep a list of strings which are initialised as empty strings, but we keep that to simplify our processing, probably should keep in array and construct string from that but we don't have to be that specific
- edge case which I didn't think is when we have just 1 row, we can handle that directly or find an algorithm 
- a good solution is to find a pattern by which strings chars and strings are created, then for sure we can write a nice solution for this, just to notice how we need to jump
- solution with rules suprisingly took more time than mapping to arrays

## Solution
https://leetcode.com/problems/zigzag-conversion/editorial