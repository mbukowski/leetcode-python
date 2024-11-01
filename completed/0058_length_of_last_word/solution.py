import re

class Solution:
    def lengthOfLastWordBool(self, s: str) -> int:
        first = 0
        last = 0
        word = False

        for i in range(len(s)):
            if s[i] == ' ':
                word = False

            else:
                if word:
                    last = i
                else:
                    first = i
                    last = i

                word = True

        return last - first + 1
    
    def lengthOfLastWordRe(self, s: str) -> int:
        m = re.search(r'.*?(\w+)\s*$', s)
        last_word = m.group(1)

        return len(last_word)

    def lengthOfLastWord(self, s: str) -> int:
        first = -10
        last = -10

        for i in range(len(s)):
            if s[i] != ' ':
                if last + 1 < i:
                    first = i

                last = i

        return last - first + 1


def main():
    solution = Solution()

    s = "Hello World"
    r = solution.lengthOfLastWord(s)
    print(r)

    s = "   fly me   to   the moon  "
    r = solution.lengthOfLastWord(s)
    print(r)

    s = "luffy is still joyboy"
    r = solution.lengthOfLastWord(s)
    print(r)


if __name__ == "__main__":
    main()

        