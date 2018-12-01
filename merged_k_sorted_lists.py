class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # array to store the values of all linked lists 
        array = []
        for l in lists:
            curr = l
            while curr:
                array.append(curr.val)
                curr = curr.next
        
        array = self.heap_sort(array)
        #print(array)
        head_node = ListNode(0)
        curr = head_node
        n = len(array)
        for i in range(n-1, -1, -1):
            curr.next =  ListNode(array[i])
            curr = curr.next

        return head_node.next
    
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
            self.max_heapify(arr,i)
        return arr

    def heap_sort(self,array):
        sorted_res = []
        max_heaps = self.build_heap(array)
        while (len(max_heaps) > 0):
            max_heaps[0], max_heaps[-1] = max_heaps[-1] , max_heaps[0]
            sorted_res.append(max_heaps[-1])
            del max_heaps[-1]
            self.max_heapify(max_heaps,0)
            
        return (sorted_res)

arr = [1,4,5,1,3,4,2,6]
obj = Solution()
print(obj.heap_sort(arr))