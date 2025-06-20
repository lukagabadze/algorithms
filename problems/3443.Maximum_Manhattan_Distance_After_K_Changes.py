class Solution(object):
    def maxDistance(self, s: str, k: int) -> int:
        string = s
        n, e, s, w = 0, 0, 0, 0
        answer = 0
        for c in string:
            if c == "N":
                n += 1
            if c == "E":
                e += 1
            if c == "S":
                s += 1
            if c == "W":
                w += 1

            # 1
            answer = max(answer, (n - s) + (w - e) + 2 * min(s + e, k))

            # 2
            answer = max(answer, (n - s) + (e - w) + 2 * min(s + w, k))

            # 3
            answer = max(answer, (s - n) + (e - w) + 2 * min(n + w, k))

            # 4
            answer = max(answer, (s - n) + (w - e) + 2 * min(n + e, k))

        return answer


if __name__ == "__main__":
    solution = Solution()

    q = [
        ("NWSE", 1),
        ("NSWWEW", 3),
        ("EWWE", 0),
    ]

    for s, k in q:
        print("s: ", s)
        print("k: ", k)
        print()
        answer = solution.maxDistance(s, k)
        print("answer: ", answer)
        print("=====================")
        print()
