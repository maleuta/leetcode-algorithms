#Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next

            node = node.next


        node.next = list1 or list2

        return dummy.next


def create_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def print_list(head):
    values = []

    while head:
        values.append(head.val)
        head = head.next

    print(values)


list1 = create_list([1, 2, 4])
list2 = create_list([1, 3, 5])

result = Solution().mergeTwoLists(list1, list2)
print_list(result)