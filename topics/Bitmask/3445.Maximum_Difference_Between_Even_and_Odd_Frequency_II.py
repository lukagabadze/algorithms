"""
NOTE: HUUUGEE FUCKING THANKS TO THE GOAT kaitouchinh for the amazing explanation!!!
(https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/solutions/6831146/easy-to-understand-explanation-for-editorial-solution)

I would have been cooked without this.
"""


class Solution(object):
    def maxDifference(self, s: str, k: int) -> int:
        INF = float("inf")

        n = len(s)
        answer = float("-inf")

        for a in map(str, range(5)):
            for b in map(str, range(5)):
                if a == b:
                    continue

                # Counters for the 'right' pointer
                cnt_a, cnt_b = 0, 0

                # Counters for the 'left' pointer
                prev_a, prev_b = 0, 0

                # best[status] - stores minimum prev_a - prev_b for all "a" and "b" parities
                # NOTE: Keep in mind, we want to MAXIMIZE cnt_a - cnt_b and MINIMIZE prev_a - prev_b.
                # That's why we keep MINIMUM prev_a - prev_b counts here
                best = [INF] * 4

                left = -1
                for right in range(n):
                    cnt_a += 1 if s[right] == a else 0
                    cnt_b += 1 if s[right] == b else 0

                    while right - left >= k and cnt_b - prev_b >= 2:
                        # Parity state for the prefix ending at 'left'
                        left_status = self.get_status(prev_a, prev_b)

                        # Update the best array
                        best[left_status] = min(best[left_status], prev_a - prev_b)

                        left += 1
                        prev_a += 1 if s[left] == a else 0
                        prev_b += 1 if s[left] == b else 0

                    # Calculating the potential answer for the current 'right' pointer.

                    # 1. Get the parity state for the prefix ending at the 'right' pointer.
                    right_status = self.get_status(cnt_a, cnt_b)

                    # 2. Determine the desired left_status for this to hit the target.
                    # Remember that 10 is the target_state, so 10 = state_j XOR state_(i-1),
                    # therefore, state_(i-1) = state_j XOR 10
                    required_status = right_status ^ 0b10

                    if best[required_status] != INF:
                        answer = max(answer, (cnt_a - cnt_b) - best[required_status])

                        # NOTE: Remeber: freq[a] in s[i...j] = count(a, j) - count(a, i-1)
                        #                freq[b] in s[i...j] = count(b, j) - count(b, i - 1)
                        #
                        # The answer is freq(a) - freq(b) = (count(a, j) - count(b, i-1)) - (count(b, j) - count(b, i-1))
                        #
                        # Therefore: answer = count(a, j) - count(b, j) - (count(a, i-1) - count(b, i-1))
                        #
                        # Here: (cnt_a - cnt_b) is (count(a, j) - count(b, j))
                        # and best[required_status] is (count(a, i-1) - count(b, i-1)).

        return answer

    def get_status(self, cnt_a: int, cnt_b: int) -> int:
        """
        Helper function that returns a 2-bit parity state.
        Bit 1 is cnt_a and Bit 2 is cnt_b.
        Example: 10 means cnt_a is odd (1) and cnt_b is even (0).
        11 means cnt_a is odd (1) and cnt_b is odd (1)
        """

        # num & 1 returns 1 if num is odd and 0 if num is even.
        # Since we want to have a 2-bit array, we need to shift cnt_a to the left (...cnt_a...) << 1
        return ((cnt_a & 1) << 1) | (cnt_b & 1)


if __name__ == "__main__":
    solution = Solution()

    q = [("12233", 4), ("1122211", 3), ("110", 3), ("22141", 4)]

    for s, k in q:
        print("s: ", s)
        print("k: ", k)
        print()
        answer = solution.maxDifference(s, k)
        print("answer: ", answer)
        print("=====================")
        print()
