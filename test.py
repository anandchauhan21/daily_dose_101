class MyCircularQueue:

    def __init__(self, k: int):
        self.head = 0
        self.tail = 0
        self.c = 0
        self.k = k
        self.arr = [None]*k

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.arr[self.tail] = value
        self.c +=1
        self.tail = (self.tail+1)%self.k
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.head = (self.head+1)%self.k
        self.c -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.arr[self.head]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.arr[self.tail]

    def isEmpty(self) -> bool:
        if self.c ==0: return True
        return False

    def isFull(self) -> bool:
        if self.c == self.k: return True
        return False

