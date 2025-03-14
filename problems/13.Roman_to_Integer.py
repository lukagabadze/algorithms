class Solution(object):
    def romanToInt(self, s: int) -> int:
        symbol_value = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        answer = 0
        for i in range(len(s)):
            if i != len(s) - 1:
                if symbol_value[s[i]] < symbol_value[s[i + 1]]:
                    answer -= symbol_value[s[i]]
                    continue

            answer += symbol_value[s[i]]

        return answer


if __name__ == "__main__":
    solution = Solution()

    q = ["III", "LVIII", "MCMXCIV"]

    for s in q:
        print("s: ", s)
        answer = solution.romanToInt(s)
        print("answer: ", answer)
        print()
