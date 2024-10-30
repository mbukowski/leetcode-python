# 55. Jump Game
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

## Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

## Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

## Constraints:
1 <= nums.length <= 10^4
0 <= nums[i] <= 10^5

## Analysis
- bruteforce solution would take O(n^2) time, we could probably divide an conquer
- array is quite long, edge case is empty or one size
- this problem is a little bit similar to gas station, I think we could first check if we can reach end, I would go through the list, one by one if jump further is higher take that one, if not burn 1 jump, and once we end up below jump threshold we should be golden, we just need True or False
- with that solution complexity is O(n)

## Solution
https://leetcode.com/problems/jump-game/editorial/?envType=study-plan-v2&envId=top-interview-150
