class Solution(object):
    def removeElement(self, nums, val):
        p1 = 0
        p2 = len(nums) - 1

        while (p1 <= p2):
            if (nums[p1] != val):
                # k += 1
                p1 += 1
            elif (nums[p2] == val):
                p2 -= 1
            else:
                # should use a buffer to store value, but actually in this case it doesn't matter 
                # also we don't need a separate result parameter, it's enough to return p1 pointer
                nums[p1] = nums[p2]
                p1 += 1
                p2 -= 1

        return p1
    

def main():
    s = Solution()

    nums = [3,2,2,3]
    val = 3
    k = s.removeElement(nums, val)
    print(k)
    print(nums)

    nums = [0,1,2,2,3,0,4,2]
    val = 2
    k = s.removeElement(nums, val)
    print(k)
    print(nums)


if __name__ == "__main__":
    main()

        