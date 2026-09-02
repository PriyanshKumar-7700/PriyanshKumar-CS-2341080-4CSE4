import heapq

def kthlargest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]

nums = [3, 2, 1, 5, 6, 8, 1]
k = 3
print(kthlargest(nums, k))