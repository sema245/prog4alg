class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [0] * k
        self.head, self.sz, self.k = 0, 0, k

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.q[(self.head + self.sz) % self.k] = value
        self.sz += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.head = (self.head + 1) % self.k
        self.sz -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.q[self.head]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.q[(self.head + self.sz - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.sz == 0

    def isFull(self) -> bool:
        return self.sz == self.k