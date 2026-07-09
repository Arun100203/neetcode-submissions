class LinkedList:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
class MyHashMap:

    def __init__(self):
        pre = LinkedList(-1, -1)
        curr = LinkedList(-1, -1)
        head = pre
        for i in range(10000):
            pre.next = curr
            pre = curr
            curr = LinkedList(-1, -1)
        self.head = head

    def put(self, key: int, value: int) -> None:
        head = self.head
        if head.key == -1:
            head.key = key
            head.value = value
            return

        while head.key != -1:
            if head.key == key:
                break
            head = head.next

        head.key = key
        head.value = value

    def get(self, key: int) -> int:
        head = self.head
        while head and head.key != key:
            head = head.next

        if not head:
            return -1
        return head.value

    def remove(self, key: int) -> None:
        head = self.head
        while head and head.key != key:
            head = head.next

        if not head:
            return 
        
        head.key = -1
        head.value = -1

    # def print(self) -> None:
    #     head = self.head
    #     for i in range(10):
    #         print(head.key, head.value)
    #         head = head.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)