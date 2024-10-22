class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        tank = 0
        start = 0
        total = 0

        k = len(gas)

        for i in range(k):
            total += gas[i] - cost[i]

            # travel from i -> i + 1
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = (i + 1) % k

        if total < 0:
            return -1

        # # do we need to travel from 0 to start to make sure??
        # for i in range(start):
        #     tank += gas[i] - cost[i]
        #     if (tank < 0):
        #         return -1
            
        return start


def main():
    s = Solution()

    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    r = s.canCompleteCircuit(gas, cost)
    print(r)

    gas = [2,3,4]
    cost = [3,4,3]
    r = s.canCompleteCircuit(gas, cost)
    print(r)


if __name__ == "__main__":
    main()

        