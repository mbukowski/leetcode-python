class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums) == 1: return True

        jump = 0

        for i in range(len(nums)):
            if jump - 1 < nums[i]:
                jump = nums[i]

            if i + jump >= len(nums) - 1: return True

            jump -= 1
            if jump < 0: return False

        return True

def main():
    s = Solution()

    # nums = [2,3,1,1,4]
    # r = s.canJump(nums)
    # print(r)

    # nums = [3,2,1,0,4]
    # r = s.canJump(nums)
    # print(r)

    nums = [2, 0, 0]
    r = s.canJump(nums)
    print(r)


if __name__ == "__main__":
    main()

        