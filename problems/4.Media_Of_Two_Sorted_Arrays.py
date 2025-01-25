class Solution(object):
  def findMedianSortedArrays(self, nums1, nums2):
    nums = sorted(nums1 + nums2)
    length = len(nums)

    if length % 2 == 0:
      return (nums[length // 2 - 1] + nums[length // 2]) / 2.0

    if length % 2 == 1:
      return nums[length // 2]

if __name__ == "__main__":
  solution = Solution()

  # l1 = [1, 3]
  # l2 = [2]

  l1 = [1, 2]
  l2 = [3, 4]
  
  print("l1: ", l1)
  print("l2: ", l2)

  print()
  answer = solution.findMedianSortedArrays(l1, l2)
  print()

  print("answer: ", answer)