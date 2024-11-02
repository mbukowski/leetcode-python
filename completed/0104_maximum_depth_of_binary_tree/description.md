# 104. Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

## Example 2:
Input: root = [1,null,2]
Output: 2 

## Constraints:
The number of nodes in the tree is in the range [0, 10^4].
-100 <= Node.val <= 100

## Analysis
- this looks like a simple recursion problem, size of the tree is a max from the left, right + 1
- can we do it without recursion -> just have a list of visited nodes, but we need to remember their height, somewhere we need to return it
- we could have a height in a separate variable
- also we could go level by level increasing height, yes that's how I would approach it, thus we have 2 problems, 1st is recursion and 2nd regular
- implemented both solutions, I wonder if iterative solution could be simplified
- time complexity in both cases O(n) each node has to be visited once
- DFS and BFS algorithms
- iterative solution was a clean implementation of appending tuples of pairs level and node, with that we didn't have to have an extra structure holding whole level and we had a nice alg. to calc max depth
- when it comes to tail recursion it's little more complex topic not that well understood by me

## Solution
https://leetcode.com/problems/maximum-depth-of-binary-tree/editorial/