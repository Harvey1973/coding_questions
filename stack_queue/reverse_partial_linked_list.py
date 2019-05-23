# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        curr = head 
        prev = None 
        count = 0 
        
        while (curr != None):
            count = count + 1
            if count >= m :
                break 
            else :
                prev = curr
                curr = curr.next 
                
        con = prev 
        tail = curr 
        print(count)
        print(curr.val)
        print(prev.val)
        
        while (curr != None and count <=n):
            # indicate the starting position of reversal 
            count = count + 1
            temp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = temp
            
        # after the while loop curr will point to the first link object outside of 
        # reversal window 
        # Prev will point to the head of the reversed portion
        print("after reversal")
        print(curr.val)
        if con :
            con.next = prev
        else:
            head = prev
        tail.next = curr
        return head 
        
                
            
        