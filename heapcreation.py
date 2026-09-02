import heapq

heap = []

# Insert elements
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)
heapq.heappush(heap, 3)

print(heap)

print("Minimum:", heap[0])

print("Removed:", heapq.heappop(heap))

print("Heap after removal:", heap)

