class FreqStack:

    def __init__(self):
        self.d = {}
        self.max_value = 0
        self.gd = {}

    def push(self, val: int) -> None:
        fre = self.d.get(val, 0) + 1
        self.max_value = max(fre, self.max_value)
        self.d[val] = fre

        if fre not in self.gd:
            self.gd[fre] = []
        self.gd[fre].append(val)
        

    def pop(self) -> int:
        val = self.gd[self.max_value].pop()
        self.d[val] -=1 

        if not self.gd[self.max_value]:
            self.max_value -= 1

        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()