# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


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


def test_has_cycle():
    solution = Solution()

    assert solution.hasCycle(None) is False
    assert solution.hasCycle(create_list([1, 2, 3])) is False

    cycle = ListNode(1)
    cycle.next = cycle
    assert solution.hasCycle(cycle) is True


if __name__ == "__main__":
    test_has_cycle()
    print("All hasCycle tests passed.")