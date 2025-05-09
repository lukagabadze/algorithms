"""
TIME: 10ms (Beats 4.38%)
NOTE: Not fast, but super clean, just running a while loop until the string empties or does not change:
        s = s.replace("()", "")
        s = s.replace("[]", "")
        s = s.replace("{}", "")
"""


class Solution(object):
    def isValid(self, s: str) -> bool:
        while s:
            prev = s

            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")

            if prev == s:
                return False

        return True


if __name__ == "__main__":
    solution = Solution()

    q = [
        ("()"),
        ("()[]{}"),
        ("(]"),
        ("([])"),
        ("([(({{[]}}))])([[()]])"),
        ("([(({{[]}}))])([}[()]])"),
        (""),
        ("]"),
        (")(){}"),
        ("]["),
    ]

    for s in q:
        print("s: ", s)
        print()
        answer = solution.isValid(s)
        print("answer: ", answer)
        print("=====================")
        print()
