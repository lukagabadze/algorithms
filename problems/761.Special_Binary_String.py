"""
NOTE: arr[::-1] reverses the array

NOTE: Could not solve it on my own.
Thank you to the GOAT lee ("https://leetcode.com/problems/special-binary-string/solutions/113211/java-c-python-easy-and-concise-recursion/")
and thanks to another GOAT for explaining it further ("https://leetcode.com/problems/special-binary-string/solutions/113211/java-c-python-easy-and-concise-recursion/comments/281761")
"""


class Solution(object):
  def makeLargestSpecial(self, s):
    i = 0
    count = 0
    special_maximized_subs = []
    for (j, c) in enumerate(s):
      count = count + 1 if c == '1' else count - 1
      if count == 0:
        special_maximized_subs.append('1' + self.makeLargestSpecial(s[i+1:j])  + '0')
        i = j + 1

    return "".join(reversed(sorted(special_maximized_subs)))
  
  
    

if __name__ == "__main__":
  solution = Solution()

  # s = "11011000"
  s = "101101011000"
  
  print("s: ", s);
  print("\n")
  answer = solution.makeLargestSpecial(s)
  print("\n")
  print("answer: ", answer)