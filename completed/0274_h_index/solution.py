class Solution:
    def hIndex(self, citations: list[int]) -> int:
        score = [0]*1001
        max_citation = 0

        for i in range(len(citations)):
            if citations[i] > max_citation:
                max_citation = citations[i]

            score[citations[i]] += 1

        if max_citation == 0:
            return 0

        total = 0
        current = max_citation
        while current > 0:
            if score[current] > 0:
                total += score[current]

            if total >= current:
                return current
            
            current -= 1
        
        return 0
        

def main():
    solution = Solution()

    # citations = [3,0,6,1,5]
    # r = solution.hIndex(citations)
    # print(r)

    # citations = [1,3,1]
    # r = solution.hIndex(citations)
    # print(r)

    citations = [10]
    r = solution.hIndex(citations)
    print(r)


if __name__ == "__main__":
    main()

        