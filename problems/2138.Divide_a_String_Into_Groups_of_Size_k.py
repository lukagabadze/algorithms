from typing import List


class Solution(object):
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        answer = []

        for i in range(0, n, k):
            if i + k > n:
                answer.append(s[i:] + fill * (k - (n - i)))
            else:
                answer.append(s[i : i + k])

        return answer


if __name__ == "__main__":
    solution = Solution()

    q = [
        ("abcdefghi", 3, "x"),
        ("abcdefghij", 3, "x"),
        ("a", 1, "x"),
        ("a", 3, "x"),
    ]

    for s, k, fill in q:
        print("s: ", s)
        print("k: ", k)
        print("fill: ", fill)
        print()
        answer = solution.divideString(s, k, fill)
        print("answer: ", answer)
        print("=====================")
        print()
