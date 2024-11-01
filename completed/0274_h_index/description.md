# 274. H-Index
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

## Example 1:
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

## Example 2:
Input: citations = [1,3,1]
Output: 1

## Constraints:
n == citations.length
1 <= n <= 5000
0 <= citations[i] <= 1000

## Analysis
- if array is empty return 0
- naive solution would O(n^2) as we check array for each level higher starting with 0
- sorting array upfront would be helpful, we could then just iterate once, time complexity O(nlogn)
- can we do it recursively? probably yes
- what if we start with additional array? from 0 to 1000? we can just once iterate and increase each bucket and then go down summing it up, we could also keep a maximum value that we know from which index we start
- after that we could probably improve that recursively or dynamic programming
- storing max_citations can speed up in case we have plenty of low values
- additionally if we would use a sorted map we could use that structure instead of array -> no empty fields
- I don't see a way to implement it properly without additional structure