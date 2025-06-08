from heapq import heappush, heappop


class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)

        heap = []
        removed_inds = set()
        for i in range(n):
            if s[i] != "*":
                heappush(heap, (s[i], -i))
            else:
                c, c_i = heappop(heap)
                removed_inds.add(-c_i)

        answer = ""
        for i in range(n):
            if s[i] != "*" and i not in removed_inds:
                answer += s[i]

        return answer


if __name__ == "__main__":
    solution = Solution()

    q = [
        ("aaba*"),
        ("abc"),
        ("abdac*d*cc*"),
    ]

    for s in q:
        print("s: ", s)
        print()
        answer = solution.clearStars(s)
        print("answer: ", answer)
        print("=====================")
        print()
