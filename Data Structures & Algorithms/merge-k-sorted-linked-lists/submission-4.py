# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        heap = []
        counter = 0
        for i in lists:
            if i:
                heapq.heappush(heap, (i.val, counter, i))
                counter+=1
        dummy = ListNode()
        cur = dummy
        while heap:
            val, counter, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap, (node.next.val, counter,node.next))
                counter+=1
        return dummy.next

        