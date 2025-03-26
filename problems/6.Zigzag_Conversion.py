class Solution(object):
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        n = len(s)
        step = (numRows - 1) * 2

        answer = ""
        for i in range(numRows):
            for j in range(i, n, step):
                answer += s[j]

                if 0 < i and i < numRows - 1:
                    offset = (numRows - (i + 1)) * 2
                    if j + offset < n:
                        answer += s[j + offset]

        return answer


if __name__ == "__main__":
    solution = Solution()

    q = [
        ("PAYPALISHIRING", 3),
        ("PAYPALISHIRING", 4),
        ("A", 1),
    ]

    for s, numRows in q:
        print("s: ", s)
        print("numRows: ", numRows)
        print()
        answer = solution.convert(s, numRows)
        print("answer: ", answer)
        print("=====================")
        print()
