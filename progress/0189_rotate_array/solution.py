class Solution:
    # works well
    def rotate_naive(self, nums: list[int], k: int) -> None:
        nums_copy = [0] * len(nums)

        for i in range(len(nums)):
            nums_copy[(i + k) % len(nums)] = nums[i]

        for i in range(len(nums)):
            nums[i] = nums_copy[i]

    # this solution runs out of time -> probably takes too long to check if element already exists
    def rotate_long(self, nums: list[int], k: int) -> None:
        if len(nums) == 1:
            return
        
        if k == 0 or k == len(nums):
            return
        
        if k > len(nums):
            k = k % len(nums)

        visited = []

        while len(visited) < len(nums):
            for i in range(k):
                p1 = i
                b1 = nums[p1]

                while p1 not in visited:
                    visited.append(p1)

                    p2 = (p1 + k) % len(nums)

                    b2 = nums[p2]
                    nums[p2] = b1
                    b1 = b2

                    p1 = p2

    # with this solution we have issues that not all cycles are ok and we dont' want to loop too long when not needed
    def rotate_cycles(self, nums: list[int], k: int) -> None:
        l = len(nums)
        if l == 1:
            return
        
        if k == 0 or k == l:
            return
        
        k = k % l

        # we will have duplicates on empty runs unfortunately 
        for i in range(k):
            self.cycle(nums, k, i)

        # if l % k == 0:
        #     # it may happen that this cycle was already covered that way having visited array would be helpful
        #     # it could be simple bitmap if we visited / shifted or not yet
        #     for i in range(k):
        #         self.cycle(nums, k, i)
        # else:
        #     self.cycle(nums, k, 0)

    def cycle(self, nums: list[int], k: int, start: int) -> None:
        l = len(nums)
        p = (start + k) % l
        b1 = nums[start]
        b2 = nums[p]

        while p != start:
            nums[p] = b1
            b1 = b2
            p = (p + k) % l
            b2 = nums[p]

        nums[p] = b1

    def rotate(self, nums: list[int], k: int) -> None:
        l = len(nums)
        if l == 1:
            return
        
        if k == 0 or k == l:
            return
        
        visited = [0] * l
        
        k = k % l
        for start in range(k):
            if visited[start]: 
                continue

            p = (start + k) % l
            b1 = nums[start]
            b2 = nums[p]

            while p != start:
                visited[p] = 1
                nums[p] = b1
                b1 = b2
                p = (p + k) % l
                b2 = nums[p]

            nums[p] = b1
            visited[p] = 1

    def rotate_fast(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n

        start = 0
        count = 0

        while count < n:
            current = start
            prev = nums[start]

            while True:
                next_idx = (current + k) % n
                nums[next_idx] = prev
                prev = nums[next_idx]

                current = next_idx
                count += 1

                if start == current:
                    break

            start += 1


    def rotate_reverse(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1


def main():
    s = Solution()

    # nums = [1,2,3,4,5,6,7]
    # k = 3
    # print(k)
    # print(nums)
    # s.rotate(nums, k)
    # print(nums)

    # nums = [-1,-100,3,99]
    # k = 2
    # print(k)
    # print(nums)
    # s.rotate(nums, k)
    # print(nums)

    nums = [1,2,3,4,5,6]
    k = 4
    print(k)
    print(nums)
    s.rotate(nums, k)
    print(nums)


if __name__ == "__main__":
    main()

        