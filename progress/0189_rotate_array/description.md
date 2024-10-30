# 189. Rotate Array
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

## Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

## Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

## Constraints:
1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
0 <= k <= 10^5

## Analysis
- check for empty array -> according to preconditions
- edge cases is when we have just one element -> simply return it
- another edge case is when k is is 0 or length of the array -> don't need to shift anything and would be problematic as well
- tricky situation occurs when k is greater than array length -> we could simplify it by do initial modulo

- do we know anything about data which is placed in the array maybe the same values?
- size of array manageable in memory
- array doesn't have to be sorted 
- first solution which comes to my head -> init a new array and simple copy paste over -> that however requires an extra space
- second solution -> to use a store and we take each pair one after another, if we are lucky -> we don't have to switch to next param, 
- however if cycle occurs we need to move to next value and go on, how would we know that a cycle occurred -> we keep starting point
- we would have to remember if visited each of the first k params if yes we didn't have cycle
- third more complex, what if we take that part of memory and just splice it differently? we just point to another next element, that would be easily done if we have a different data structure
- what about a possible values it's doesn't matter what we have inside
- we need to store somewhere if we visited already a given field -> for small k it's simple for large k however it's different, what shall we do with large k? shall we just revert but in another order? doesn't matter I think 
- ok let's start with implementing simple solution and then we do in place
- current solution uses extra structure visited where we check if given value was already moved, problem is that it will be the same size as starting array, but that would be in place at least
- we could have recursive solution where we pass starting and target and value which we want to shift between both of the indexes, and as well visited array
- optimal solution would focus on checking if target table can divide without any reminders by 'k' if yes we have to visit every step from 0 to k, otherwise we are guaranteed to have each of the variables visited 
- can we use different data structure? binary tree or sth. else? 
- how do we test it? by taking original table and checking if shift happened correctly -> still need to store original somewhere else

- final version shifts array in place however we are using a helper structure for handling if position was or was not visited, without that I imagine it's also possible however would require more complex algorithm to figure out proper cycles, and still would be problematic without helper structure
- faster version simply copies one array to another
- rotate_fast is a good implementation, a correct approach used here is the number of changes which we used to track, thus we don't have to use any extra structure for that
- rotating an array by reversing gives us also a nice solution for this problem, quite nice


## Solution
https://leetcode.com/problems/rotate-array/editorial/?envType=study-plan-v2&envId=top-interview-150