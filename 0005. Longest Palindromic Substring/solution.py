class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        n = len(s)

        def single_check(a, b) -> str:
            p = ''
            while a >= 0 and b < n:
                if s[a] == s[b]:
                    p = s[a:b+1]
                    a -= 1
                    b += 1
                else:
                    break

            return p


        # starting with single char
        for i in range(n):
            p = single_check(i, i)

            if len(p) > len(res):
                res = p

        # starting with double chars
        for i in range(len(s) - 1):
            p = single_check(i, i + 1)

            if len(p) > len(res):
                res = p

        return res

def main():
    input = 'babad'
    # input = 'bbccd'

    s = Solution()
    res = s.longestPalindrome(input)
    print(res)

if __name__ == "__main__":
    main()
