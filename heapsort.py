def heapify(heap, n, i):
   largest = i
   left = 2 * i + 1
   right = 2 * i + 2

   if left < n and heap[i] < heap[left]:
      largest = left

   if right < n and heap[largest] < heap[right]:
      largest = right

   if largest != i:
      heap[i],heap[largest] = heap[largest],heap[i]
      heapify(heap, n, largest)

def heapSort(heap):
   n = len(heap)

   for i in range(n // 2 - 1, -1, -1):
      heapify(heap, n, i)

   for i in range(n - 1, 0, -1):
      heap[i], heap[0] = heap[0], heap[i]
      heapify(heap, i, 0)

heap = [4, 3, 1, 0, 2]
heapSort(heap)
n = len(heap)
print("Heap array: ")
print(heap)
print ("The Sorted array is: ")
print(heap)