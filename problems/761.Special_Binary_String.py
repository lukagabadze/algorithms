"""
NOTE: arr[::-1] reversed the array
"""


class Solution(object):
  def makeLargestSpecial(self, s):

    answer = s
    for i in range(len(s)):
      c = s[i]
      
      left_side = s[:i + 1]
      right_side = s[i + 1:]
      
      left_subs = []
      one_count = 0
      zero_count = 0
      for j in range(len(left_side))[::-1]:
        if left_side[j] == '1':
          one_count += 1
        if left_side[j] == '0':
          zero_count += 1
        if one_count == zero_count and one_count != 0:
          left_subs.append(j)

      right_subs = []
      one_count = 0
      zero_count = 0
      for j in range(len(right_side)):
        if right_side[j] == '1':
          one_count += 1
        if right_side[j] == '0':
          zero_count += 1
        if one_count == zero_count and one_count != 0:
          right_subs.append(j)
      
      if left_subs and right_subs:
        for l in left_subs:
          for r in right_subs:
            left = s[l : i+1]
            right = s[i+1 : i+r+2]
            
            new_s = s[:l] + right + left + s[i+r+2:]
            
            new_s = "".join(new_s)
            answer = max(new_s, answer)

    return answer
  
  
    

if __name__ == "__main__":
  solution = Solution()

  # s = "11011000"
  s = "101101011000"
  
  print("s: ", s);
  print("\n")
  answer = solution.makeLargestSpecial(s)
  print("\n")
  print("answer: ", answer)