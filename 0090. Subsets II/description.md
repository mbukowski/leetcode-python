# 90. Subsets II

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

## Example 1:
    Input: nums = [1,2,2]
    Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

## Example 2:
    Input: nums = [0]
    Output: [[],[0]]
 
## Constraints:
* 1 <= nums.length <= 10
* -10 <= nums[i] <= 10

## Notes
- maximum no. of sets $2^n$ which means we always have exponential complexity
- for small input set it's acceptable
- solution: https://leetcode.com/problems/subsets-ii/solutions/1304408/subsets-ii/
- maybe we could have a better time if we don't use recurrsion but it's very good for small sets like this one esp. we don't have to enter that deep,
- my non-recurrsive solution is not that good, we should keep some additional information - check this out again

## Summary
### Solution
https://leetcode.com/problems/subsets-ii/solutions/1304408/subsets-ii