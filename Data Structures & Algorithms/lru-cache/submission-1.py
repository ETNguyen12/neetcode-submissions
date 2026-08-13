class ListNode:

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.nxt = None
        self.prv = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.nxt = self.tail
        self.tail.prv = self.head

    def update(self, node: ListNode) -> None:
        self.remove(node)
        self.add(node)
    
    def add(self, node: ListNode) -> None:
        last_node = self.tail.prv
        last_node.nxt = node
        node.prv = last_node
        node.nxt = self.tail
        self.tail.prv = node

    def remove(self, node: ListNode) -> None:
        prev_node = node.prv
        next_node = node.nxt
        prev_node.nxt = next_node
        next_node.prv = prev_node

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if node is None:
            return -1

        self.update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.update(node)
            return
        
        node = ListNode(key, value)
        self.cache[key] = node
        self.add(node)
        if len(self.cache) > self.cap:
            least_recently_used_node = self.head.nxt
            self.remove(least_recently_used_node)
            del self.cache[least_recently_used_node.key]

        
