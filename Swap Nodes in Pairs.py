class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            # সংযোগ বদল
            first.next = second.next
            second.next = first
            prev.next = second

            # পরের জোড়ার জন্য এগিয়ে যাওয়া
            prev = first

        return dummy.next