class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = defaultdict(int)
        heap = []
        for i in range(k):
            heap.append(-1 * nums[i])
            freq[nums[i]] +=1
        heapq.heapify(heap)
        res.append(-1 * heap[0])
        l = 0
        for r in range(k, len(nums)):
            freq[nums[l]] -= 1
            freq[nums[r]] +=1
            heapq.heappush(heap, -1 * nums[r])
            while freq[-1 * heap[0]] == 0:
                heapq.heappop(heap)
            res.append(-1 * heap[0])
            l+=1
        return res

