"""

There are two ways to solve this in O(n^2):
1) Dynamic Programming - have a matrix where coordinates i, j are indexes of a palindrome,
and if s[i] === s[j] and dp[i + 1][j - 1] === True than congrats, you found a new palindrome
and you can set dp[i][j] = True

2) Expand from centers in each letter of the string, this is probably easier


BUT, you have a way to solve this in O(n) time using Manacher's Algorithm

lil funny thing: racecar is a palindrome
"""


class Solution(object):
    def longestPalindrome(self, s):
        s = "#" + "#".join(s) + "#"

        def expand(ind):
            size = 1
            while (
                ind - size >= 0
                and ind + size < len(s)
                and s[ind - size] == s[ind + size]
            ):
                size += 1

            return size * 2 - 1

        i = 1
        center_ind = 0
        answers = [1]
        final_ans = [1, 1]
        while i < len(s):
            size = 1

            known_size_ind = center_ind - (i - center_ind)
            known_size = answers[known_size_ind]

            # Out of center
            if center_ind + answers[center_ind] // 2 - 1 < i:
                size = expand(i)
                center_ind = i

            # Totally Inside
            elif i + known_size < center_ind + answers[center_ind] // 2:
                size = known_size
            # Prefix Goes Out
            elif (
                known_size_ind - known_size // 2 < center_ind - answers[center_ind] // 2
            ):
                size = 1
            else:
                size = expand(i)
                center_ind = i

            if size > final_ans[1] - final_ans[0] + 1:
                final_ans[0] = center_ind - size // 2
                final_ans[1] = center_ind + size // 2 + 1

            # Reached the end (not necessary, it shoud make it a little faster)
            if center_ind + size // 2 >= len(s):
                break

            answers.append(size)
            i += 1

        return s[final_ans[0] : final_ans[1]].replace("#", "")


if __name__ == "__main__":
    solution = Solution()

    # s = "abaxabaxabybaxabyb"
    s = "babadada"

    print("s: ", s)

    print()
    answer = solution.longestPalindrome(s)
    print()

    print("answer: ", answer)
