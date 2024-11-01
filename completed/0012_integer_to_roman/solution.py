class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M', '']

        result = ""
        degree = 0

        while num > 0:
            rem = num % 10
            num = num // 10

            while rem > 0:
                if rem == 9:
                    result = roman[2 * degree] + roman[2 * (degree + 1)] + result
                    rem -= 9
                elif rem == 4:
                    result = roman[2 * degree] + roman[2 * degree + 1] + result
                    rem -= 4
                elif rem == 5:
                    result = roman[2 * degree + 1] + result
                    rem -= 5
                elif rem != 5:
                    result = roman[2 * degree] + result
                    rem -= 1

            degree += 1

        return result

def main():
    solution = Solution()

    num = 3749
    r = solution.intToRoman(num)
    print(r)

    num = 58
    r = solution.intToRoman(num)
    print(r)

    num = 1994
    r = solution.intToRoman(num)
    print(r)


if __name__ == "__main__":
    main()

        