from utils import ListNode, array_to_linked_list, print_linked_list
from typing import Optional


class Solution(object):
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1 and not list2:
            return None

        head = ListNode()
        node = head

        while list1 and list2:
            node.next = ListNode()

            value = None
            if list1.val <= list2.val:
                value = list1.val
                list1 = list1.next
            else:
                value = list2.val
                list2 = list2.next

            node.val = value
            node = node.next

        # Append the rest
        if list1:
            node.val = list1.val
            node.next = list1.next

        # Append the rest
        if list2:
            node.val = list2.val
            node.next = list2.next

        return head


if __name__ == "__main__":
    solution = Solution()

    q = [([1, 2, 4], [1, 3, 4]), ([], []), ([1, 9], [10, 11])]

    for list1, list2 in q:
        print("list1: ", list1)
        print("list2: ", list2)
        print()
        answer = solution.mergeTwoLists(
            array_to_linked_list(list1), array_to_linked_list(list2)
        )
        print("answer: ", end=" ")
        print_linked_list(answer)
        print("=====================")
        print()
