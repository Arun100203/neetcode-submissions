class LFUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.freq = defaultdict(LinkedList)

        self.cap = capacity
        self.min_fre = 1

    def counter(self, node):
        cnt = node.fre
        self.freq[cnt].pop(node)
        if cnt == self.min_fre and self.freq[cnt].length() == 0:
            self.min_fre += 1


        node.fre += 1
        self.freq[node.fre].pushRight(node)
        

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1

        node = self.hashmap[key]
        self.counter(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key not in self.hashmap:
            if len(self.hashmap) == self.cap:
                #remove first element in the highest(last) fre element.
                node = self.freq[self.min_fre].popLeft()
                self.hashmap.pop(node.key)

            temp = Node(key, value) 
            self.hashmap[key] = temp
            self.freq[1].pushRight(temp)
            self.min_fre = 1
        else:
            node = self.hashmap[key]
            node.value = value
            self.counter(node)


        

class Node:
    
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.fre = 1
        self.next = None
        self.pre = None

class LinkedList:
    def __init__(self):
        self.left = Node(-1, -1)
        self.right = Node(-1, -1)

        self.size = 0
        self.left.next = self.right
        self.right.pre = self.left

    def length(self):
        return self.size

    def pushRight(self, node):
        pre = self.right.pre
        pre.next = node
        node.pre = pre

        node.next = self.right
        self.right.pre = node
        
        self.size += 1

    def pop(self, node):
        pre, nxt = node.pre, node.next

        pre.next = nxt
        nxt.pre = pre

        node.pre = None
        node.next = None

        self.size -= 1

    def popLeft(self):
        if self.length() == 0:
            return None

        node = self.left.next
        self.pop(node)
        return node


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)