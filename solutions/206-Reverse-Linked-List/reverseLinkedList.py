from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        # initial recursive solution
        # # base case - you've reached the end of the list
        # if head.next == None:
        #     return head

        # newHead = self.reverseList(head.next)
        # head.next = None
        # # traverse to the end of the list
        # current = newHead
        # while current.next:
        #     current = current.next
        # current.next = head
        # return newHead

        # iterative solution
        previous = None
        current = head
        while current:
            nextNode = current.next
            current.next = previous
            previous = current
            current = nextNode
        return previous


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

# Link the nodes together
node1.next = node2  # node1 -> node2
node2.next = node3

bruh = Solution()
newHead = bruh.reverseList(node1)
