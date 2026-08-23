class LRUCache:
    class Node:
        def __init__(self, n, m, left=None, right=None):
            self.n = n
            self.m = m
            self.left = left
            self.right = right


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.right = self.tail
        self.tail.left = self.head
        
    def remove(self, node):
        # print(node.n, node.m)
        pre = node.left
        nxt = node.right
        pre.right = nxt
        nxt.left = pre

    def insert(self, node):
        pre = self.tail.left
       
        pre.right = node
        node.right = self.tail
        self.tail.left = node
        node.left = pre

    def get(self, key: int) -> int:
        # self.printList()
        if key not in self.d:
            return -1

        temp = self.d[key]
        self.remove(temp)
        self.insert(temp)
        return temp.m
        
        

    def put(self, key: int, value: int) -> None:
        if key not in self.d and len(self.d) + 1 > self.capacity:
            lru_node = self.head.right
            self.remove(lru_node)
            del self.d[lru_node.n]

            temp = self.Node(key, value)
            self.d[key] = temp
            self.insert(temp)
        else:
            if key not in self.d:
                self.d[key] = self.Node(key, value)
            temp = self.d[key]
            temp.m = value

            if temp.right and temp.left:
                self.remove(temp)
            self.insert(temp)

        

    def printList(self):
        head = self.head
        # for i in self.d:
        #     print (self.d[i].left.n, " -> ", self.d[i].n, " -> ", self.d[i].right and self.d[i].right.n)

        print("======")

        s = ""
        while head:
            s = s + str(head.m) + " -> "
            head = head.right

        print(s)
            


