# 2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

## Example 1:

    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.

## Example 2:

    Input: l1 = [0], l2 = [0]
    Output: [0]

## Example 3:

    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]
 
## Constraints:

* The number of nodes in each linked list is in the range [1, 100].
* 0 <= Node.val <= 9
* It is guaranteed that the list represents a number that does not have leading zeros.

## Summary

### Intuition

- we start from the begin and we move forward
- we should be aware that lists may have different length

### Approach

Take first elements from the both lists and add them together. If sum is greater than 10 save that reminder and add modulo value to the last position.
If next element in first list is not null add it to the total summ. Do the same with the second list. Repeat the whole process as long as sum value is greater than 0.

### Complexity
- Time complexity: linear $O(n)$ - we just iterate through the each list once

- Space complexity: linear $O(n)$ - we create new linked list, but if we reuse existing one we could make it without declaring extra space

### Solution

https://leetcode.com/problems/add-two-numbers/solutions/127833/add-two-numbers/
