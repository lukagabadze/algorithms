class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        def char_to_num(c: str) -> int:
            return ord(c) - ord("a")

        freqs = [0] * 26

        for c in word:
            num = char_to_num(c)
            freqs[num] += 1

        arr = []
        for n in freqs:
            if n != 0:
                arr.append(n)

        def greedy(freq: int):
            rm = 0
            for x in arr:
                if x < freq:
                    rm += x
                elif x > freq + k:
                    rm += x - (freq + k)
            return rm

        answer = len(word)
        for freq in arr:
            answer = min(answer, greedy(freq))

        return answer


if __name__ == "__main__":
    solution = Solution()

    q = [
        ("aabcaba", 0),
        ("dabdcbdcdcd", 2),
        ("aaabaaa", 2),
    ]

    for word, k in q:
        print("word: ", word)
        print("k: ", k)
        print()
        answer = solution.minimumDeletions(word, k)
        print("answer: ", answer)
        print("=====================")
        print()
