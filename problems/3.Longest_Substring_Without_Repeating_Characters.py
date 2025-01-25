"""
This technique is called "sliding window"
pretty fucking cool
  
Interesting fact:
I had a count variable to count the possible answer and wrote "ans = max(ans, count)"
but chatgpt told me it was unnecessary since the count could be counted any time using "i - char_map.get(char)"
also pretty fucking cool
"""

class Solution(object):
  def lengthOfLongestSubstring(self, s):
    char_map = {}
    ans = 0
    start_ind = 0
    for i, char in enumerate(list(s)):
      if char in char_map and char_map[char] >= start_ind:
        start_ind = char_map.get(char) + 1

      ans = max(ans, i - start_ind)
      char_map[char] = i

    return ans

if __name__ == "__main__":
  solution = Solution()
  
  # s = "abcabcbb"
  # s = "dvdf"
  s = "tmmzuxt"
  
  print("s: ", s)
  
  print()
  answer = solution.lengthOfLongestSubstring(s)
  print()
  
  print("answer: ", answer)