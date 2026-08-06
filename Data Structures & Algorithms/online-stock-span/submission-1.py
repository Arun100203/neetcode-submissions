class StockSpanner:

    def __init__(self):
        self.dp = []
        self.li = []

    def next(self, price: int) -> int:
        if len(self.li)==0:
            self.li.append(price)
            self.dp.append(1)
            return 1

        if self.li[-1] > price:
            self.li.append(price)
            self.dp.append(1)
            return 1

        i = len(self.li)-1
        while i >= 0:
            if self.li[i] > price:
                self.li.append(price)
                self.dp.append(len(self.dp)-i)
                return self.dp[-1]
            else: 
                i = i - self.dp[i]

        if i <= 0:
            self.li.append(price)
            self.dp.append(len(self.li))
            return self.dp[-1]
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)