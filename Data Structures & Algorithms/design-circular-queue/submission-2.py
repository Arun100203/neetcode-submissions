class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1] * k
        self.start = 0
        self.end = 0
        self.n = k
        

    def enQueue(self, value: int) -> bool:
        if self.queue[self.start%self.n] == -1:
            self.queue[self.start%self.n] = value
            self.start += 1
            return True

        return False
        

    def deQueue(self) -> bool:
        if self.queue[self.end%self.n] != -1:
            self.queue[self.end%self.n] = -1
            self.end += 1
            return True

        return False


    def Front(self) -> int:
        if self.isEmpty():
            return -1
        # print(self.start, self.end, self.queue)
        return self.queue[(self.end)%self.n]


    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        # print(self.start, self.end, self.queue)
        return self.queue[(self.start-1)%self.n]
        

    def isEmpty(self) -> bool:
        return self.start == self.end 
        

    def isFull(self) -> bool:
        return self.start - self.end == self.n


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()