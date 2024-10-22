class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        prefix = strs[0]
        
        for s in strs:
            prefix = self.common_prefix(prefix, s)

        return prefix


    def common_prefix(self, s1, s2):
        prefix = ""

        for i in range(min(len(s1), len(s2))):
            if s1[i] == s2[i]:
                prefix += s1[i]
            else:
                break

        return prefix


def main():
    s = Solution()

    strs = ["flower","flow","flight"]
    r = s.longestCommonPrefix(strs)
    print(r)

    strs = ["dog","racecar","car"]
    r = s.longestCommonPrefix(strs)
    print(r)

if __name__ == "__main__":
    main()

        