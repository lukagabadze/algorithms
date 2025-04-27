from typing import List


"""
TIME: 3ms (Beats 60.85%)
MEMORY: 18.20MB (Beats 15.98%)
NOTE: This is without the path compression optimization.
"""


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        n = 26
        parent = list(range(n))
        rank = [0] * n

        def letter_to_int(a: str):
            return ord(a) - ord("a")

        def find(node: int):
            if parent[node] != node:
                return find(parent[node])
            return node

        def union(a: int, b: int):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return

            if rank[root_a] > rank[root_b]:
                parent[root_b] = root_a
            elif rank[root_a] < rank[root_b]:
                parent[root_a] = root_b
            else:
                parent[root_b] = root_a
                rank[root_a] += 1

        # Assemble the groups first
        for s in equations:
            if s[1] == "=":
                a = letter_to_int(s[0])
                b = letter_to_int(s[3])
                union(a, b)

        # Now check for exceptions
        for s in equations:
            if s[1] == "!":
                root_a = find(letter_to_int(s[0]))
                root_b = find(letter_to_int(s[3]))

                # Found an exception
                if root_a == root_b:
                    return False

        return True


if __name__ == "__main__":
    solution = Solution()

    q = [(["a==b", "b!=a"]), (["b==a", "a==b"]), (["a==b", "b==c", "c!=z", "z!=b"])]

    for equations in q:
        for row in equations:
            print(row)
        print()
        answer = solution.equationsPossible(equations)
        print("answer: ", answer)
        print("=====================")
        print()
