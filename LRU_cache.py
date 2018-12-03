class Node(object):
 
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = Node((0,0)) 
        self.tail = Node((0,0))
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.lookup = {}


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        node = self.lookup.get(key)
        if node :
            self._remove(node)
            self._add(node)
            return node.data[1]
        else:
            return - 1

        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.lookup:
            self._remove(self.lookup[key])
        
        data = (key,value)
        new_node = Node(data)
        self._add(new_node)
        self.lookup[key] = new_node

        if len(self.lookup) > self.capacity :
            # we have to delete head , since head is implicity the least used element
            n = self.head.next
            del self.lookup[n.data[0]]
            self._remove(n)
            


    def _add(self,new_node):

         # check if head and tail = None
        p = self.tail.prev
        p.next = new_node 
        new_node.prev = p 
        new_node.next = self.tail
        self.tail.prev = new_node
        
    def _remove (self, node): 
        p = node.prev
        n = node.next 
        p.next = n 
        n.prev = p

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)