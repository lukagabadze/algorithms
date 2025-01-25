"""
First time with linked lists, hell yeah
"""

class ListNode:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next

class Solution(object):
  def addTwoNumbers(self, l1, l2):
    root_head = ListNode(0)
    tail = root_head
    carry = 0
    while l1 is not None or l2 is not None or carry:
      value = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry

      if value > 9:
        value = value % 10
        carry = 1
      else:
        carry = 0
      
      node = ListNode(value)
      tail.next = node
      tail = node
      
      l1 = l1.next if l1 else None
      l2 = l2.next if l2 else None

    return root_head.next
    

def array_to_linked_list(arr):
    root_head = ListNode(0)
    tail = root_head
    for value in arr:
      node = ListNode(value)
      tail.next = node
      tail = node

    return root_head.next

def print_linked_list(head: ListNode, name = ""):
  print(name, end="")
  node = head
  while node:
    print(node.val, end = " ")
    if node.next:
      print("->", end = " ")
    node = node.next

  print()

if __name__ == "__main__":
  solution = Solution()

  # l1 = array_to_linked_list([2, 4, 3])
  # l2 = array_to_linked_list([5, 6, 4])
  
  l1 = array_to_linked_list([9,9,9,9,9,9,9])
  l2 = array_to_linked_list([9,9,9,9])

  # l1 = array_to_linked_list([0, 0, 5])
  # l2 = array_to_linked_list([0, 0, 5])

  # l1 = array_to_linked_list([0])
  # l2 = array_to_linked_list([0])

  print_linked_list(l1, "l1: ")
  print_linked_list(l2, "l2: ")

  print()
  answer = solution.addTwoNumbers(l1, l2)
  print()

  print_linked_list(answer, "answer: ")