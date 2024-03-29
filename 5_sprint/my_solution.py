def sift_down(heap, idx):
    left = 2 * idx
    right = 2 * idx + 1
    if len(heap) < left:
        return idx
    if (right <= len(heap)) and (heap[left] < heap[right]):
        index_largest = right
    else:
        index_largest = left
    if heap[idx] < heap[index_largest]:
        heap[idx], heap[index_largest] = heap[index_largest], heap[idx]
        return sift_down(heap, index_largest)
    return idx