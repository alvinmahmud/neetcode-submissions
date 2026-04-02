class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev, self.next = None, None

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

        self.head, self.tail = self.Node(0, 0), self.Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def delete(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.tail.prev
        nxt = self.tail
        prev.next = node
        node.next = nxt
        node.prev = prev
        nxt.prev = node
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.delete(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        self.cache[key] = self.Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.head.next
            self.delete(lru)
            del self.cache[lru.key]
