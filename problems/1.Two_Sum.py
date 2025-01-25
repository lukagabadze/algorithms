class Solution(object):
  def twoSum(self, nums, target):
    target_map = { num: i for i, num in enumerate(nums) }
    print('target_map: ', target_map)
    result = next(([i, target_map.get(target - num)] for (i, num) in enumerate(nums) if target_map.get(target - num) is not None and i is not target_map.get(target - num)), None)
    return result
    

if __name__ == "__main__":
  solution = Solution()
  # nums = [2,7,11,15]
  # target = 9
  nums = [3,2,4]
  target = 6
  
  print("nums: ", nums);
  print("target: ", target);
  print("\n")
  answer = solution.twoSum(nums, target)
  print("\n")
  print("answer: ", answer)