class Solution(object):
    def merge(self, nums1, m, nums2, n):
        p = m + n - 1
        p1 = m - 1
        p2 = n - 1

        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1   

        # my original solution, above little nicer solution
        # while (p >= 0):
        #     if (p1 >= 0) and (p2 >= 0):
        #         if (nums1[p1] >= nums2[p2]):
        #             nums1[p] = nums1[p1]
        #             p1 -= 1
        #         else:
        #             nums1[p] = nums2[p2]
        #             p2 -= 1

        #     elif (p1 < 0):
        #         nums1[p] = nums2[p2]
        #         p2 -= 1
               
        #     else:
        #         nums1[p] = nums1[p1]
        #         p1 -= 1

        #     p -= 1
       

    

def main():
    s = Solution()

    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    s.merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    s.merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    s.merge(nums1, m, nums2, n)
    print(nums1)

if __name__ == "__main__":
    main()

        