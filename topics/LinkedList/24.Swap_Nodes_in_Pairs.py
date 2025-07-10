"""
NOTE: Thanks to whoji for the clean solution!
(https://leetcode.com/problems/swap-nodes-in-pairs/solutions/11030/my-accepted-java-code-used-recursion)
"""

from utils import ListNode, array_to_linked_list, print_linked_list
from typing import Optional


class Solution(object):
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        n = head.next
        head.next = self.swapPairs(head.next.next)
        n.next = head

        return n


if __name__ == "__main__":
    solution = Solution()

    q = [
        [],
        [1],
        [1, 2, 3],
        [1, 2, 3, 4],
        [1, 2, 3, 4, 5],
    ]

    for list in q:
        print("list: ", list)
        print()
        answer = solution.swapPairs(array_to_linked_list(list))
        print("answer: ", end=" ")
        print_linked_list(answer)
        print("=====================")
        print()
