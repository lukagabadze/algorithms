"""
TIME: 10ms (Beats 4.38%)
NOTE: Not fast, but super clean, just running a while loop until the string empties or does not change:
        s = s.replace("()", "")
        s = s.replace("[]", "")
        s = s.replace("{}", "")


TIME: 0ms (Beats 100%)
NOTE: Using stacks is much faster and more reliable.
"""


class Solution(object):
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if not stack:
                    return False

                a = stack.pop()
                if (
                    (c == ")" and a != "(")
                    or (c == "]" and a != "[")
                    or (c == "}" and a != "{")
                ):
                    return False

        return True if not stack else False


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
        ("["),
    ]

    for s in q:
        print("s: ", s)
        print()
        answer = solution.isValid(s)
        print("answer: ", answer)
        print("=====================")
        print()
