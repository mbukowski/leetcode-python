class Solution:
    def convert_list(self, s: str, numRows: int) -> str:
        direction = 1
        current = 0
        result = [ '' for i in range(numRows) ]

        for i in range(len(s)):
            result[current] += s[i]

            if current == numRows - 1:
                direction = -1
                current = max(current + direction, 0)
            elif current == 0:
                direction = 1
                current = min(current + direction, numRows - 1)
            else:
                current = current + direction
            
        return ''.join(result)
    
    def convert(self, s: str, numRows: int) -> str:
        result = ''

        if numRows == 1: return s

        for start in range(numRows):
            i = start
            
            while i < len(s):
                if start == 0 or start == numRows - 1:
                    result += s[i]
                    i += 2 * (numRows - 1)
                    if i >= len(s): break
                else:
                    result += s[i]
                    i += 2 * (numRows - 1 - start)
                    if i >= len(s): break

                    result += s[i]
                    i += 2 * start
                    if i >= len(s): break
            
        return result

def main():
    solution = Solution()

    # s = "PAYPALISHIRING"
    # numRows = 3
    # r = solution.convert(s, numRows)
    # print(r)

    # s = "PAYPALISHIRING"
    # numRows = 4
    # r = solution.convert(s, numRows)
    # print(r)

    s = "A"
    numRows = 2
    r = solution.convert(s, numRows)
    print(r)

if __name__ == "__main__":
    main()

        