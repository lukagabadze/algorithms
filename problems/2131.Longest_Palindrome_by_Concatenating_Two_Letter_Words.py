from typing import List


"""
TIME: 131ms (Beats 38.09%)
NOTE: I don't like using a dictionary here (words_map) since it's slow, arrays are faster.
And also, I would rather go over words_map.keys() instead of words array for a faster result,
but I keep getting an error saying the dictionary size changed during iteration. I'll fix it.

TIME: 248ms (Beats 8.78%)
NOTE: I changed the words_map dictionary to a matrix which 100% should have made the performance better, but it's much much slower.
I also added unique_words set which would hold all unique words and go over them in our final for loop instead of going over every word.
This as well should have made an improvement, but it made it slower. WTF?!
"""


class Solution(object):
    def longestPalindrome(self, words: List[str]) -> int:
        words = [[ord(word[0]) - ord("a"), ord(word[1]) - ord("a")] for word in words]

        words_map = [[0 for _ in range(26)] for _ in range(26)]
        answer = 0
        unique_words = set()
        for x, y in words:
            words_map[x][y] += 1
            unique_words.add((x, y))

        # Find a center with just one word ("cc" for example)
        for x, y in unique_words:
            if x == y and words_map[x][y] % 2 == 1:
                answer += 2
                break

        visited = [[False for _ in range(26)] for _ in range(26)]
        for x, y in unique_words:
            if visited[x][y] or visited[y][x]:
                continue

            # If we don't have reverse counter-part, continue
            if words_map[x][y] < 1 or words_map[y][x] < 1:
                continue

            # If reverse counter-part is the same word, like "gg" and we have multiple
            if x == y:
                answer += words_map[x][y] // 2 * 4
                visited[x][y] = True
                continue

            answer += min(words_map[x][y], words_map[y][x]) * 4
            visited[x][y] = True

        return answer


if __name__ == "__main__":
    solution = Solution()

    q = [
        (["lc", "cl", "gg"]),
        (["ab", "ty", "yt", "lc", "cl", "ab"]),
        (["cc", "ll", "xx"]),
        (["qw", "er", "ty"]),
        (
            [
                "dd",
                "aa",
                "bb",
                "dd",
                "aa",
                "dd",
                "bb",
                "dd",
                "aa",
                "cc",
                "bb",
                "cc",
                "dd",
                "cc",
            ]
        ),
    ]

    for words in q:
        print("words: ", words)
        print()
        answer = solution.longestPalindrome(words)
        print("answer: ", answer)
        print("=====================")
        print()
