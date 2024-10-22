class Solution(object):
    def trap(self, height):
        _height = 0
        _width = len(height)
        occupied = 0
        empty = 0

        # water = h * w - occupied - empty

        # scan iteration        
        for i in range(len(height)):
            occupied += height[i]
            _height = max(_height, height[i])

        p1 = 0
        p2 = _width - 1

        for level in range(_height):
            while height[p1] - (level + 1) < 0:
                p1 += 1

            while height[p2] - (level + 1) < 0:
                p2 -= 1

            empty += p1
            empty += _width - 1 - p2

        # what if h * w is too high? max should be in range 10^5 * 10^5 -> 10^10
        water = _height * _width - occupied - empty

        return water
    
    '''
    similar to my solution but faster and takes care of the case where p1 and p2 are next to each other with one peak
    main difference is that it treats each cell independently and calculates for them
    that means we started by asking a question how to count water - in this case we count water for each cell 
    not like I suggested with equation, however solution is quite simple, need to check from different angles to that
    solution

    solution with stacks is little more complicated but works quite well imho
    '''
    def trap_longer(self, height):
        p1 = 0
        p2 = len(height) - 1

        water = 0
        level = 1

        while (p1 < p2):
            # alternatively we could navigate with range but I like this way better
            if height[p1] - level < 0:
                p1 += 1
            elif height[p2] - level < 0:
                p2 -= 1
            else:
                # we can already start from next cell after left pointer
                for i in range(p1 + 1, p2):
                    if height[i] - level < 0:
                        water += 1

                level += 1

        return water

    def trap_best(self, height):
        left, right = 0, len(height) - 1
        ans = 0
        left_max, right_max = 0, 0
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                ans += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                ans += right_max - height[right]
                right -= 1
        return ans

def main():
    s = Solution()

    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    r = s.trap(height)
    print(r)

    height = [4,2,0,3,2,5]
    r = s.trap(height)
    print(r)

if __name__ == "__main__":
    main()

        