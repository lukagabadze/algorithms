from typing import List, Dict


class TrieNode:
    def __init__(self):
        self.cnt: int = 0

        # Child nodes.
        # children["b"] will hold TrieNode class object of the child character "b".
        self.children: Dict[str, "TrieNode"] = {}


class Solution(object):
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        if len(strs) == 1:
            return strs[0]

        # Trie tree root
        root = TrieNode()

        def insert(string: str):
            node = root
            for i, c in enumerate(string):
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
                node.cnt += 1

        # Assembling the trie tree
        for string in strs:
            insert(string)

        max_count = max([n.cnt for n in root.children.values()] or [0])

        if max_count < len(strs):
            return ""

        answer = ""
        node = root
        while True:
            next_char = None
            for char in node.children:
                if node.children[char].cnt == max_count:
                    next_char = char
                    node = node.children[char]

            if not next_char:
                break

            answer += next_char

        return answer


if __name__ == "__main__":
    solution = Solution()

    q = [
        (["flower", "flow", "flight"]),
        (["dog", "racecar", "car"]),
        ([]),
        (["a"]),
        (["reflower", "flow", "flight"]),
    ]

    for strs in q:
        print("strs: ", strs)
        print()
        answer = solution.longestCommonPrefix(strs)
        print("answer: ", answer)
        print("=====================")
        print()
