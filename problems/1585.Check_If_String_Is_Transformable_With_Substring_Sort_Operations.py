"""
NOTE: Huge thanks to GSAN for the explanation!
(https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations/solutions/843954/python-backward-forward-pass-with-stack)

NOTE: Previously, I was looking at a key in the target, I would check the left side AND right side.
Turns out, you can just check one side, left for example.
Because if there is an error, some key might not fail while checking left,
BUT, some other key 100% will.
TODO: I am not 100% sure tho.... check this.
"""


class Solution(object):
    def isTransformable(self, s: str, t: str) -> bool:
        places = [[] for _ in range(10)]

        for i in reversed(range(len(s))):
            key = int(s[i])
            places[key].append(i)

        for c in t:
            key = int(c)

            # Check if this digit exists in the source
            if not places[key]:
                return False

            # This key was previously at index i
            i = places[key][-1]
            for j in range(key):
                if places[j] and places[j][-1] < i:
                    return False

            places[key].pop()

        return True


if __name__ == "__main__":
    solution = Solution()

    q = [
        ("84532", "34852"),
        ("34521", "23415"),
        ("12345", "12435"),
        ("18", "28"),
        ("845327893142", "845327893142"),
    ]

    for s, t in q:
        print("s: ", s)
        print("t: ", t)
        print()
        answer = solution.isTransformable(s, t)
        print("answer: ", answer)
        print("=====================")
        print()
