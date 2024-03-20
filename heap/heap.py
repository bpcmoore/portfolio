import random

class MaxHeap:
    def __init__(self):
        self.heap = ['x'] # x is a place holder so the index is equal to the place in the heap

    def insert(self, value: int):
        self.heap.append(value)
        ind = len(self.heap) - 1
        while ind > 1:
            if value > self.heap[int(ind/2)]:
                self.heap[ind] = self.heap[int(ind/2)]
                self.heap[int(ind/2)] = value
                ind = int(ind/2)
            else:
                break
    
    def pop(self):
        size = len(self.heap) - 1
        if size == 0: return "empty heap"
        if size == 1: return self.heap.pop(1)
        value = self.heap[1]
        self.heap[1] = self.heap.pop(-1)
        size -= 1
        ind = 1
        while size >= ind * 2:
            cur = self.heap[ind]
            if size >= ind * 2 + 1:
                if cur > self.heap[ind * 2] and cur > self.heap[ind * 2 + 1]: break
                elif self.heap[ind * 2] < self.heap[ind * 2 + 1]:
                    self.heap[ind] = self.heap[ind * 2 + 1]
                    self.heap[ind * 2 + 1] = cur
                    ind = ind * 2 + 1
                    continue
            if cur > self.heap[ind * 2]: break
            self.heap[ind] = self.heap[ind * 2]
            self.heap[ind * 2] = cur
            ind = ind * 2
        return value

if __name__ == "__main__":
    heap = MaxHeap()
    for i in range(50):
        heap.insert(random.randint(-100,100))
    print(heap.heap)
    for i in range(len(heap.heap)):
        print(heap.pop())
        
