# Another solution with backtrack
# This solution is much cleaner and explains in a good way how backtracking works
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        def backtrack(start, curr_list):
            res.append(curr_list.copy())
            
            for j in range(start, n):
                curr_list.append(nums[j])
                backtrack(j+1, curr_list)
                curr_list.pop()
        
        n = len(nums)

        backtrack(0, [])


# Backtracking 
# backtracking is quite simple when we understand it, it does require a piece of common variables
# Time complexity O(Nx2^N)
# Space complexity O(N) as we have just to reserve some space for curr
# class Solution:
#     def subsets(self, nums: list[int]) -> list[list[int]]:
#         res = []
        
#         def backtrack(first = 0, curr = []):
#             # if the combination is done
#             if len(curr) == k:  
#                 res.append(curr.copy())
#                 return

#             for i in range(first, n):
#                 # add nums[i] into the current combination
#                 curr.append(nums[i])
#                 # use next integers to complete the combination
#                 backtrack(i + 1, curr)
#                 # backtrack
#                 curr.pop()
        
#         n = len(nums)
#         for k in range(n + 1):
#             backtrack()

#         return res


# Cascading 
# We start with empty list and we iterate through each element and we add to already existing 
# Time complexity O(Nx2^N)
# Space complexity O(Nx2^N)
# class Solution:
#     def subsets(self, nums: list[int]) -> list[list[int]]:
#         res = [[]]
#         n = len(nums)
        
#         for num in nums:
#             new_sets = []
#             for curr_set in res:
#                 new_sets.append(curr_set + [num])

#             res += new_sets
        
#         return res

# # Another approach to bitmask solution, only why do we start slicing from 3rd element
# class Solution:
#     def subsets(self, nums: list[int]) -> list[list[int]]:
#         n = len(nums)
#         res = []
        
#         for i in range(2**n, 2**(n + 1)):
#             # generate bitmask, from 0..00 to 1..11 bitmask is a string 
#             # we start from element index 3 as bitmask look something like this '0b1000' etc. 
#             bitmask = bin(i)[3:]
            
#             # append subset corresponding to that bitmask
#             # creates list on the fly
#             res.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        
#         return res

# # Lexicographic with binary bitmask
# class Solution:
#     def subsets(self, nums: list[int]) -> list[list[int]]:
#         res = []

#         for mask in range(2 ** len(nums)):
#             m_set = []

#             i = 0
#             while mask > 0:
#                 if mask & 1 == 1:
#                     m_set += [nums[i]]
#                 mask = mask >> 1
#                 i += 1

#             res.append(m_set)

#         return res

def main():
    input = [1, 2, 3]

    s = Solution()
    res = s.subsets(input)
    print(res)

if __name__ == "__main__":
    main()
