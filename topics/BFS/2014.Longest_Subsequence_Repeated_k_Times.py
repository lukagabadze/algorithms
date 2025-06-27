"""
NOTE: Thanks to the official LeetCode editorial for the solution!
(https://leetcode.com/problems/longest-subsequence-repeated-k-times/solutions/6882480/longest-subsequence-repeated-k-times)

NOTE: I keep getting close to solving these questions using my intuition but there is just not enough time to do this daily.

NOTE: Generating next valid candidates using BFS is very cool.
"""

from collections import Counter, deque


class Solution(object):
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        # Take the characters which appear at least k times in the string
        # (you can also call this characters "hot" characters)
        candidates = sorted([c for c, w in Counter(s).items() if w >= k], reverse=True)

        answer = ""
        queue = deque(candidates)
        while queue:
            cand = queue.popleft()

            if len(cand) > len(answer):
                answer = cand

            # Generate next candidates
            for char in candidates:
                nxt = cand + char
                it = iter(s)

                # Since we are using the iterator here "iter(s)",
                # that means the order of this substring will also be checked.
                if all(ch in it for ch in nxt * k):
                    queue.append(nxt)

        return answer


if __name__ == "__main__":
    solution = Solution()

    q = [
        ("letsleetcode", 2),
        ("bb", 2),
        ("ab", 2),
    ]

    for s, k in q:
        print("s: ", s)
        print("k: ", k)
        print()
        answer = solution.longestSubsequenceRepeatedK(s, k)
        print("answer: ", answer)
        print("=====================")
        print()
