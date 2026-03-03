class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None
        
class LRU:
    def __init__(self,capacity):
        self.capacity=capacity
        self.cache={}
        
        self.head=Node(0,0)
        self.tail=Node(0,0)
        
        self.head.next=self.tail
        self.tail.prev=self.head
        
    def _add_to_front(self,node):
        node.next=self.head.next
        self.head.next.prev=node
        node.prev=self.head
        self.head.next=node
        
    def _remove(self,node):
        prev=node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev
        
    def get(self,key):
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self._remove(node)
        self._add_to_front(node)
        return node.value
    
    def put(self,key,value):
        if key in self.cache:
            node=self.cache[key]
            self._remove(node)
        node=Node(key,value)
        self.cache[key]=node
        self._add_to_front(node)
        if len(self.cache)>self.capacity:
            last=self.tail.prev
            self._remove(last)
            del self.cache[last.key]
    
    def display(self):
        curr=self.head.next
        while curr != self.tail:
            print(f"{curr.key} :{curr.value}",end=" ")
            curr=curr.next
        print("END")
lru=LRU(3)
lru.put(1,11)
lru.put(2,22)
lru.put(3,33)
lru.get(1)
lru.put(4,44)
lru.display()