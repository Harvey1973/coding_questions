class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # The idea of this problem is use the analogy to bucket 
        # use the left most index and right , most index as the barrier ,
        # a segment can hold water if and only if the bars in between are 
        # less than the minimum height

        #initialization 
        l = 0
        r = len(height) -1 
        water = 0
        min_height = 0
        while ( l < r ):

            # advanceing left panel 
            while (l < r ) and height[l] <= min_height:
                water += (min_height - height[l])
                l = l + 1
            while (l < r) and height[r] <= min_height:
                water += (min_height - height[r])
                r = r - 1
            min_height = min (height[l], height[r])

        return water 


obj = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
obj.trap(height)