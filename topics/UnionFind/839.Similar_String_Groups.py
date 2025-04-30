from typing import List


"""
TIME: 139ms (Beats 74.86%)
MEMORY: 18.14MB (Beats 69.14%)
NOTE: This legit took me less than 10 minutes.
I am telling you, I am just goated 🐐.
"""


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        parent = list(range(n))
        rank = [0] * n

        def find(node: int):
            if parent[node] != node:
                parent[node] = find(parent[node])
                return parent[node]
            return node

        def union(a: int, b: int):
            a_root = find(a)
            b_root = find(b)

            if a_root == b_root:
                return

            if rank[a_root] > rank[b_root]:
                parent[b_root] = a_root
            elif rank[a_root] < rank[b_root]:
                parent[a_root] = b_root
            else:
                parent[b_root] = a_root
                rank[a_root] += 1

        def are_similar(word1: str, word2: str) -> bool:
            n1 = len(word1)
            n2 = len(word2)

            if n1 != n2:
                return False

            diff_count = 0
            for i in range(n1):
                if word1[i] != word2[i]:
                    diff_count += 1

                if diff_count > 2:
                    return False

            return True

        for i in range(n):
            for j in range(i + 1, n):
                i_root = find(i)
                j_root = find(j)

                if i_root == j_root:
                    continue

                if are_similar(strs[i], strs[j]):
                    union(i_root, j_root)

        return len(set([find(i) for i in parent]))


if __name__ == "__main__":
    solution = Solution()

    q = [(["tars", "rats", "arts", "star"]), (["omv", "ovm"])]

    for strs in q:
        print("strs: ", strs)
        print()
        answer = solution.numSimilarGroups(strs)
        print("answer: ", answer)
        print("=====================")
        print()
