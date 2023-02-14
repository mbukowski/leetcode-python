# 78. Subsets
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

## Example 1:
    Input: nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

## Example 2:
    Input: nums = [0]
    Output: [[],[0]]

## Constraints:
* 1 <= nums.length <= 10
* -10 <= nums[i] <= 10
* All the numbers of nums are unique.

## Summary
3 different approaches: 
- cascading
- lexicography with bitmask
- backtracking

### Intuition
All values in the array are unique, which should simplify a lot as we can go with a bitmask. 
We could also play with recursion but there is no need for that.

### Approach
Map mask to relevant subsets, ie. for [1, 2, 3] mask 010 which is value 2 will give us subset [2], mask 101 will give subset [1, 3] and so on

### Complexity
- Time complexity: exponential $O(2^n)$
depending on the size of the input list

- Space complexity: linear $O(n)$
basically we need to allocate one dimensional list

### Solution
https://leetcode.com/problems/subsets/solutions/464411/subsets/