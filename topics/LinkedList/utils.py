class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def array_to_linked_list(arr) -> ListNode:
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def print_linked_list(head: ListNode):
    if not head:
        return

    while head:
        print(head.val, end=" -> " if head.next is not None else "")
        head = head.next

    print()
