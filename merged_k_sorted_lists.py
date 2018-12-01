# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

# This solution uses heap without library functions
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # array to store the values of all linked lists 
        array = []

        for l in range (len(lists)):
            while (lists[l].next != None ):
                array.append(lists[l].val)
        #build heap 
        heaps = self.build_heap(array)
        head_node = ListNode(heaps[-1])
        for i in range(n-2, -1, -1):
            node = ListNode(heaps[i])
            head_node.next = node
            head_node = node
            
    
    def max_heapify(self,arr,i):
        n= len(arr)
        largest = i # Initialize largest as root 
        l = 2 * i + 1     # left = 2*i + 1 
        r = 2 * i + 2     # right = 2*i + 2 
        # See if left child of root exists and is 
        # greater than root 
        if l < n and arr[i] < arr[l]: 
            largest = l 
    
        # See if right child of root exists and is 
        # greater than root 
        if r < n and arr[largest] < arr[r]: 
            largest = r 
    
        # Change root, if needed 
        if (largest != i):
            arr[i],arr[largest] = arr[largest],arr[i]
            self.max_heapify(arr,largest)

        
    def build_heap(self,arr):
        length = len(arr)
        for i in reversed (range (0,int (length/2))):
            print(i)
            self.max_heapify(arr,i)
        return arr

obj = Solution()
array = [1,4,5,1,3,4,2,6]


print(obj.build_heap(array))









