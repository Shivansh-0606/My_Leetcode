#Using OrderedDict internally uses Hashmap and DLL.

from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.cache.move_to_end(key)
        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)


#Using Hashmap and Doubly Linked List.

class Node:
    def __init__(self,key:int = 0,val:int = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove_from_cache(self,node:Node)-> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def move_to_front(self,node:Node)-> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]

        self.remove_from_cache(node)
        self.move_to_front(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove_from_cache(node)
            self.move_to_front(node)
        
        else:
            new_node = Node(key,value)
            self.cache[key] = new_node
            self.move_to_front(new_node)

            if len(self.cache) > self.capacity:
                lru_node = self.tail.prev
                self.remove_from_cache(lru_node)
                del self.cache[lru_node.key]



        

            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
