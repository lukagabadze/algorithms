class Solution(object):
    def longestSubsequence(self, s: str, k: int) -> int:
        answer = 0

        ones = []
        for i, c in enumerate(reversed(list(s))):
            if c == "0":
                answer += 1

            if c == "1":
                ones.append(i)

        sm = 0
        for p in ones:
            sm += 2**p

            if sm > k:
                break

            answer += 1

        return answer


if __name__ == "__main__":
    solution = Solution()

    q = [
        ("1001010", 5),
        ("00101001", 1),
    ]

    for s, k in q:
        print("s: ", s)
        print("k: ", k)
        print()
        answer = solution.longestSubsequence(s, k)
        print("answer: ", answer)
        print("=====================")
        print()
