# 134. Gas Station
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

## Example 1:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

## Example 2:
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
 
## Constraints:
n == gas.length == cost.length
1 <= n <= 10^5
0 <= gas[i], cost[i] <= 10^4

## Solution:
1. simple cases, just 1 gas station -> still travel around circle
2. check if there is enough gas in all gas stations comparing to cost -> don't need to find a specific solution
   is it enough condition?, ie. is there a configuration that even though values evens out, that it wouldn't work
   1) with whole gas -> and then only consume, will work 
   2) gas stations with petrol and in between cost -> from 1 to 2 higher than cost, then it works out even though that from 2 to 1 on negative
   3) 3 gas stations, 1 -> 2 negative, 2 -> 3 negative, 3 -> 1 positive
3. simple solution would be O(n^2)
4. there can be gas stations and and cost with 0 as a price
5. goal to complete it in O(n(log(n))) -> that would mean we need to divide to sub-problems
6. shall we start with highest value of gas? maybe yes but we need at least to go once through the list 
7. according to my 2nd point it's enough to make one travel -> we should make a map starting with 1 and then check 
   gas balance and remember point where balance is positive, I think we should keep a point where was the highest point and do a trip from starting point to that peak one more time, we check a point where we have highest amount of starting gas, then complexity would be even O(n) :)

https://leetcode.com/problems/gas-station/editorial/?envType=study-plan-v2&envId=top-interview-150
