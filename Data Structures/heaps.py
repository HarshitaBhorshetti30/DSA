# ------------------------------------------------------------- Min Heap -----------------------------------------------------------------------------

class MinHeap:
    def __init__(self):
        self.h = []

    def insertElement(self,elem):
        self.h.append(elem)
        self.heapify_up()

    def heapify_up(self):
        idx = len(self.h) - 1
        while idx > 0:
            p = abs(idx-2) // 2
            if p >= 0 and self.h[p] > self.h[idx]:
                self.swap(idx,p)
            idx = p
    
    def swap(self,x,y):
        temp = self.h[x]
        self.h[x] = self.h[y]
        self.h[y] = temp

    def getMin(self):
        return self.h[0]

    def deleteMin(self):
        self.swap(0,len(self.h)-1)
        print(self.h)
        min_ = self.h.pop()
        self.heapify_down()
        print(self.h)
        return min_

    def heapify_down(self):
        idx, n = 0, len(self.h)
        l = (idx*2) + 1
        while l < n:
            smaller = l
            r = (idx*2) + 2
            if r < n and self.h[r] < self.h[l]:
                smaller = r
            if self.h[idx] > self.h[smaller]:
                self.swap(idx, smaller)
            else: break
            idx = smaller
            l = (idx*2) + 1

# heap = MinHeap()
# heap.insertElement(3)
# heap.insertElement(5)
# heap.insertElement(2)
# heap.insertElement(12)
# heap.insertElement(8)
# heap.insertElement(1)
# heap.insertElement(4)   
# print(heap.h)
# print(heap.getMin())
# print('D : ', heap.deleteMin())
# print('D : ', heap.deleteMin())
# print('D : ',heap.deleteMin())


# --------------------------------------------------- Max Heap ---------------------------------------------------------------------

class MaxHeap:
    def __init__(self):
        self.h = []

    def insertElement(self, elem):
        self.h.append(elem)
        self.heapify_up()

    def heapify_up(self):
        idx = len(self.h) - 1
        while idx > 0 :
            p = abs(idx-2) // 2
            if p >= 0 and self.h[p] < self.h[idx]:
                self.swap(p,idx)
            idx = p

    def swap(self,x,y):
        temp = self.h[x]
        self.h[x] = self.h[y]
        self.h[y] = temp

    def deleteMax(self):
        n = len(self.h)
        self.swap(0,n-1)
        max_ = self.h.pop()
        self.heapify_down()
        return max_

    def heapify_down(self):
        idx, n = 0, len(self.h)
        l = (idx * 2) + 1
        while l < n:
            bigger = l
            r = (idx * 2) + 1
            if r < n and self.h[r] > self.h[l]:
                bigger = r
            if self.h[idx] > self.h[bigger]: break
            self.swap(idx, bigger)
            idx = bigger
            l = (idx * 2) + 1
                

heap = MaxHeap()
heap.insertElement(3)
heap.insertElement(5)
heap.insertElement(2)
heap.insertElement(12)
heap.insertElement(8)
heap.insertElement(1)
heap.insertElement(4)   
print(heap.h)
print('D : ', heap.deleteMax())
print('D : ', heap.deleteMax())
print('D : ',heap.deleteMax())
