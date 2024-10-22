# 42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

## Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

## Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

## Constraints:
n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5

## Solution
- assumptions, we have a valid array, only 1 bar
- kinda similar to highline problem 
- shall I go from top or bottom?
- water must be guarded by 2 bars
- we could slice from top to bottom and then sum up 
- for each level we could make a bitmap and fill check how much water fills in between cells
- we could do slicing from the bottom as well, after first iteration we know what is a max
- can we do it in smaller O(n^2)? 
- what if we divide a problem to sub-problems and count them? that could actually work -> that would solve a problem with local peaks 
- but wait, we never have such situation it's always water falling down, the only thing which may change is a starting pointer and ending pointer, because if it's empty on this position it will not capture any water
- so total water on each level is: empty cells - starting and ending pointers, if pointers meet each other then we finish algorithm, 
- can we sum up occupied cells on each level somehow faster? maybe if we make another structure? that could be a 2 dimensional array 0/1 - but would that speed it up by a lot? probably not
- any special structures which come to my mind? empty, starting from high level for water trapping, sorted? nothing that would come to my head and wouldn't be against that solution
  1) one big tower in the middle, which doesn't bring anything, but that would already by counted with condition, and we can't move to the the end cause we could have a crown situation we really want to keep track of the left- and rightmost possible cases
- how to test it? what do you mean how to test it? pour water and test
- water = height * width - occupied - empty on each level -> need to count how many empty we have on each level
- 1 iteration map -> max height + total
- later iteration just count how many empty on each level 
- we could speed if p1 is equal to p2 -> just calculate from here all remaining empty as that would be a simple peak

https://leetcode.com/problems/trapping-rain-water/editorial/?envType=study-plan-v2&envId=top-interview-150