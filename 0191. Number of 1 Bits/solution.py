class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        # third approach with bitwise and for 'n' and 'n-1'
        # if we have zeros at the end they get reverted to ones and we can speed up our algorithm 
        # front part stays the same and we substract least relevant part
        # n:   1 1 0 0 1 0 0
        # n-1: 1 1 0 0 0 1 1
        while n > 0:
            res += 1
            n = n & (n - 1)

        return res

# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         res = 0

#         # second approach can be a bitwise shift - for sure available in java
#         while n > 0:
#             res = res + (n & 1)
#             n = n >> 1

#         return res

# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         res = 0

#         # we iterate checking the rest from div 2 and summing them up 
#         while n > 0:
#             if n % 2 == 1: 
#                 res += 1
#             n = n // 2

#         return res

def main():
    s = Solution()
    v = s.hammingWeight(7)
    print(v)

if __name__ == "__main__":
    main()

        