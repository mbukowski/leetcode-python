class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        i = 0

        while i < len(nums):
            if nums[k] != nums[i]:
                k += 1
                nums[k] = nums[i]

            i += 1

        # for i in range(len(nums)):
        #     if nums[k] != nums[i]:
        #         k += 1
        #         nums[k] = nums[i]

        return k + 1

def main():
    s = Solution()

    nums = [1,1,2]
    r = s.removeDuplicates(nums)
    print(r)
    print(nums)

    nums = [0,0,1,1,1,2,2,3,3,4]
    r = s.removeDuplicates(nums)
    print(r)
    print(nums)

if __name__ == "__main__":
    main()

        