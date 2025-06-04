class Solution(object):
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)
        answer_len = n - numFriends + 1

        if answer_len <= 0:
            return ""

        if numFriends == 1:
            return word

        if answer_len == 1:
            return max(word)

        answer = ""
        for i in range(n + answer_len):
            left_edge = max(0, i - answer_len)
            right_edge = min(i, n)
            answer = max(answer, word[left_edge:right_edge])

        return answer


if __name__ == "__main__":
    solution = Solution()

    q = [
        ("dbca", 2),
        ("bbbb", 4),
        ("a", 1),
        ("a", 2),
        ("abeovmdipaiv", 4),
        ("aann", 2),
        ("gh", 1),
    ]

    for word, numFriends in q:
        print("word: ", word)
        print("numFriends: ", numFriends)
        print()
        answer = solution.answerString(word, numFriends)
        print("answer: ", answer)
        print("=====================")
        print()
