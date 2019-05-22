class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n = len(s)
        #print(n)
        if n !=0 and n!= 1:
            #print("1111")
            self.helper(0,n-1,s)
        print(s)
    def helper(self,start_index,end_index,s):
        mid = len(s) // 2
        if start_index < (mid) :
            s[start_index],s[end_index] = s[end_index] ,s[start_index] 
            self.helper(start_index+1,end_index-1,s)
obj = Solution()

s = ["H","E","A","B"]
obj.reverseString(s)