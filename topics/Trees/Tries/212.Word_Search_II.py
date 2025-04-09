"""
NOTE: Brute force with word search 1 algorithm gives TLE

NOTE: I had an intuition that I had to use prefixes and suffixes of the strings to save time.
Now I looked into solutions and looks like people use Tries Data Structure to store word prefixes and suffixes.
My intuition is getting sharper every day, that's great!

NOTE: I had this problem in the DFS folder, but it requires Tries Data Structure,
which is new to me, so I am moving it to Tries directory.

NOTE: Funny thing: I tried having self.is_word equal to None if the node was not a word,
BUT, the code `if node.is_word` did not work in cases where the is_word index was 0.
So I had to go back to using -1 if the node was not a word.

NOTE: This code was written completely by myself.
BUT, I could not crack the solution on my own, for that, I peeked in the solutions of other people,
but could not fully understand how it worked, until I watched the first 4 minutes of this video, which explains the DFS + Tries solution really well!
Huge thanks to NeetCode for the GOATed video! (https://www.youtube.com/watch?v=asbcE9mZz_U)
"""

from typing import List, Dict


class TrieNode:
    def __init__(self):
        # Equals -1 if the node is not a word,
        # or an index to the actual word in the words array.
        self.is_word: int = -1

        # Child nodes.
        # children["b"] will hold TrieNode class object of the child character "b".
        self.children: Dict[str, "TrieNode"] = {}

    def __str__(self):
        return f"is_word: {self.is_word}; children: {[key for key in self.children]}"


"""
TIME: 4299ms (Beats 65.09%)
NOTE: Pretty good for an implementation I wrote myself.
There are probably some small optimizations to lower the time to 200ms-300ms range.
"""


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> bool:
        board = board
        m = len(board)
        n = len(board[0])

        # Root of the Trie tree
        root = TrieNode()

        # Insert method to assemble the Trie tree
        def insert(word: str, ind: int):
            node = root
            for i, c in enumerate(word):
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.is_word = ind

        # Assemble the Trie tree
        for i, word in enumerate(words):
            insert(word, i)

        answers = []

        # DFS (backtrack)
        def dfs(i: int, j: int, node: TrieNode):
            if node.is_word != -1:
                answers.append(words[node.is_word])
                node.is_word = -1

            points_of_interest = [
                (i + 1, j),
                (i - 1, j),
                (i, j + 1),
                (i, j - 1),
            ]
            for x, y in points_of_interest:
                if (x >= 0 and y >= 0 and x < m and y < n) and (
                    board[x][y] in node.children
                ):
                    temp = board[i][j]
                    board[i][j] = ""

                    dfs(x, y, node.children[board[x][y]])

                    board[i][j] = temp

        # Run DFS on every cell of the board
        for i in range(m):
            for j in range(n):
                if board[i][j] in root.children:
                    dfs(i, j, root.children[board[i][j]])

        # Return the answers
        return answers


if __name__ == "__main__":
    solution = Solution()

    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    words = ["oath", "pea", "eat", "rain"]

    # board = [["a", "b"], ["c", "d"]]
    # words = ["abcb"]

    # board = [["a"]]
    # words = ["a"]

    # board = [["a", "a"]]
    # words = ["aaa"]

    for i, row in enumerate(board):
        print(" ".join(row))
    print()
    print("words: ", words)
    print("\n")
    answer = solution.findWords(board, words)
    print("answer: ", answer)
