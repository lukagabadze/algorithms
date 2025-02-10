class Solution:
  def openLock(self, deadends, target):
    # Edge case
    if "0000" in deadends or target in deadends:
      return -1

    queue = [('0000', 0)]
    visited = {'0000'}
    answer = -1

    while queue:
      (state, ans) = queue.pop(0)
      print('state: ', state)
      print('ans: ', ans)
      print()

      if state == target:
        answer = ans
        break

      arr = list(map(int, list(state)))

      d = [ -1, 1 ]

      def get_state(arr):
        state = ''
        for num in arr:
          if num < 0:
            state += '9'
          elif num > 9:
            state += '0'
          else:
            state += str(num)
        return state

      for i in d:
        for j in [0, 1, 2, 3]:
          arr_c = list(arr)
          arr_c[j] += i
          new_state = get_state(arr_c)
          if new_state not in deadends and new_state not in visited:
            queue.append((new_state, ans + 1))
            visited.add(new_state)

    return answer

if __name__ == "__main__":
  solution = Solution()
  
  deadends = ["0201","0101","0102","1212","2002"]
  target = "0202"


  print('deadends: ', deadends)
  print('target: ', target)
  print('\n')
  answer = solution.openLock(deadends, target)
  print('answer: ', answer)