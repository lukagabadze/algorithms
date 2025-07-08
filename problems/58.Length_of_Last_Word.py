class Solution(object):
    def lengthOfLastWord(self, s: str) -> int:
        return len([word for word in s.split(" ") if word != ""][-1])


if __name__ == "__main__":
    solution = Solution()

    q = [
        ("Hello World"),
        ("   fly me   to   the moon  "),
        ("luffy is still joyboy"),
    ]

    for s in q:
        print("s: ", s)
        print()
        answer = solution.lengthOfLastWord(s)
        print("answer: ", answer)
        print("=====================")
        print()
