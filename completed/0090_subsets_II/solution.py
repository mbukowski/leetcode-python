class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        # our solution will be recursive, we pop a first element from the list and we calculate a subsets for the rest of the list and we merge them
        # once the remaining list is empty we return from this single element an empty list and a list containing this element 
        # later we will merge this list with similar list from first element and remainder of the subsets but we check if such an element already exists not to add duplicates
        # before adding to merge set we need to sort our list
        subsets_p = self.subsets(nums.pop(0))
        
        if len(nums) == 0:
            return subsets_p
        else:
            subsets_q = self.subsetsWithDup(nums)
            merge_set = []
            for p in subsets_p:
                for q in subsets_q:
                    pq = p + q
                    pq.sort()
                    if pq not in merge_set:
                        merge_set.append(pq)

            return merge_set

    def subsets(self, num: int) -> list[list[int]]:
        return [[], [num]]

# class Solution:
#     def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
#         # this solution represents iterative approach, we will go through each element and keep adding them to our list
#         # sorting upfront will be a helpful for visibility and not to add two subsets which are the same, ie. [1, 2] and [2, 1]
        
#         # we start with an empty resolution
#         res = [[]]
        
#         nums.sort()
#         # total number of iteration
#         for i in range(len(nums)): 
#             res_copy = res.copy()

#             for j in range(i, len(nums)):
#                 # now we add each element to all existing lists
#                 q = [nums[j]]
#                 for p in res_copy:
#                     pq = p + q
#                     # print(f"{p} + {q} -> {pq}")
#                     if pq not in res:
#                         res.append(pq)
#                 print(f"{i} {j}")

#         return res


def main():
    input = [1, 2, 2]
    input = [4,4,4,1,4]

    s = Solution()
    res = s.subsetsWithDup(input)
    print(res)

if __name__ == "__main__":
    main()

        