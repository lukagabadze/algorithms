from typing import List


class Solution(object):
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        answers = []
        for i in range(len(words)):
            if x in words[i]:
                answers.append(i)

        return answers


if __name__ == "__main__":
    solution = Solution()

    q = [
        (["leet", "code"], "e"),
        (["abc", "bcd", "aaaa", "cbc"], "a"),
        (["abc", "bcd", "aaaa", "cbc"], "z"),
    ]

    for words, x in q:
        print("words: ", words)
        print("x: ", x)
        print()
        answer = solution.findWordsContaining(words, x)
        print("answer: ", answer)
        print("=====================")
        print()
