from collections import defaultdict

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # final solution takes is quite a beauty, as a concept we take xor operation
        # if we take XOR of zero and some bit, it will return that bit -> a xor 0 = a
        # if we take XOR of two same bits, it will return 0 -> a xor a = 0
        # hence if we xor each number with each other we should have only single one remaining 
        # a xor a xor b = 0 xor b = b
        # so we can XOR all bits together to find the unique number.
        res = 0
        for i in nums:
            res = res ^ i
        return res

# class Solution:
#     def singleNumber(self, nums: list[int]) -> int:
#         # a third solution is little wacky first we take all unique elements from our list multiply them by 2 and later we substract values from the original list
#         # concept 2*(a+b+c) − (a+a+b+b+c)=c
#         return 2 * sum(set(nums)) - sum(nums)

# class Solution:
#     def singleNumber(self, nums: list[int]) -> int:
#         # second solution very similar to a first one is to have an extra list where we append / remove elements which need to be checked
#         # at the end we just have one element in the list according to constraints
#         no_duplicate_list = []
#         for i in nums:
#             if i not in no_duplicate_list:
#                 no_duplicate_list.append(i)
#             else:
#                 no_duplicate_list.remove(i)
#         return no_duplicate_list.pop()


# class Solution:
#     def singleNumber(self, nums: list[int]) -> int:
#         # first solution takes a hash table where we add values and at the end we check which key had value 1
#         # instead of using default dict we could use regular hash map and check if the key exists
#         hash_table = defaultdict(int)

#         for i in nums:
#             hash_table[i] += 1
        
#         for i in hash_table:
#             if hash_table[i] == 1:
#                 return i
        

def main():
    input = [4, 1, 2, 2, 1]

    s = Solution()
    res = s.singleNumber(input)
    print(res)

if __name__ == "__main__":
    main()

        