import heapq

def topKFrequent(nums, k):
    freq = {}

    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    heap = []
    for num in freq:
        heapq.heappush(heap, (freq[num], num))
        if len(heap) > k:
            heapq.heappop(heap)

    result = []
    while heap:
        count, num = heapq.heappop(heap)
        result.append(num)

    return result

nums = [1, 1, 1, 2, 2, 3]
k = 2

print(topKFrequent(nums, k))