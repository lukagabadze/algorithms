from typing import List, defaultdict


"""
TIME: 131ms (Beats 38.09%)
NOTE: I don't like using a dictionary here (words_map) since it's slow, arrays are faster.
And also, I would rather go over words_map.keys() instead of words array for a faster result,
but I keep getting an error saying the dictionary size changed during iteration. I'll fix it.
"""


class Solution(object):
    def longestPalindrome(self, words: List[str]) -> int:
        words_map = defaultdict(int)
        answer = 0
        for word in words:
            words_map[word] += 1

        # Find a center with just one word ("cc" for example)
        for word in words:
            if word[0] == word[1] and words_map[word] % 2 == 1:
                answer += 2
                break

        visited = set()
        for word in words:
            if word in visited or word[::-1] in visited:
                continue

            # If we don't have reverse counter-part, continue
            if words_map[word] < 1 or words_map[word[::-1]] < 1:
                continue

            # If reverse counter-part is the same word, like "gg" and we have multiple
            if word[0] == word[1]:
                answer += words_map[word] // 2 * 4
                visited.add(word)
                continue

            answer += min(words_map[word], words_map[word[::-1]]) * 4
            visited.add(word)

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
