from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def get_min(list1, list2):
            if not list1:
                value = list2.val
                list2 = list2.next
            elif not list2:
                value = list1.val
                list1 = list1.next
            elif list1.val <= list2.val:
                value = list1.val
                list1 = list1.next
            else:
                value = list2.val
                list2 = list2.next

            return value

        root = ListNode(get_min(list1, list2))
        node = root

        while list1 or list2:
            new_node = ListNode(get_min(list1, list2))
            node.next = new_node
            node = new_node

        return root
