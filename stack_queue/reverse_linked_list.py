# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    '''
    Iterative method for reversing a linked list 
    example 1-> 2->3 -> null  
    output: 3-> 2->1 -> null
    '''
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        while (curr!= None):
            # save the current next link object  
            temp_next = curr.next 
            # make the current next pointer points to the previous one 
            curr.next = prev
            # update the prev to the current
            prev = curr 
            # update the new curr pointer 
            curr = temp_next

        return prev

            
        