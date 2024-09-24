from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # original attempt. Almost works.

        # compareListHead = list1 if list1.val >= list2.val else list2
        # returnHead = list1 if list1.val < list2.val else list2
        # currentListHead = returnHead
        # while currentListHead.next != None:
        #     while currentListHead.next.val < compareListHead.val:
        #         currentListHead = currentListHead.next
        #     temp = currentListHead.next
        #     currentListHead.next = compareListHead
        #     currentListHead = compareListHead
        #     compareListHead = temp
        # currentListHead.next = compareListHead
        # return returnHead

        # after a hint
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next


# listnodea1 = ListNode(1)
# listnodea2 = ListNode(2)
listnodea3 = ListNode(5)
# listnodea1.next = listnodea2
# listnodea2.next = listnodea3

listnodeb1 = ListNode(1)
listnodeb2 = ListNode(2)
listnodeb3 = ListNode(4)
listnodeb1.next = listnodeb2
listnodeb2.next = listnodeb3

bruh = Solution()
bruh.mergeTwoLists(listnodea3, listnodeb1)
