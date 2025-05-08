class Solution(object):
    def isValid(self, s: str) -> bool:
        i = 0
        while i < len(s):
            j = 1
            while i + j < len(s) and i - j + 1 >= 0 and s[i + j] in [")", "]", "}"]:
                if (
                    (s[i + j] == ")" and s[i - j + 1] != "(")
                    or (s[i + j] == "]" and s[i - j + 1] != "[")
                    or (s[i + j] == "}" and s[i - j + 1] != "{")
                ):
                    return False

                j += 1

            i += j

        return (
            s.count("(") == s.count(")")
            and s.count("[") == s.count("]")
            and s.count("{") == s.count("}")
        )


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
    ]

    for s in q:
        print("s: ", s)
        print()
        answer = solution.isValid(s)
        print("answer: ", answer)
        print("=====================")
        print()
