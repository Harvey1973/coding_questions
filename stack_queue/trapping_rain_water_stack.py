class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        total_water = 0
        n = len(height)

        for i in range(n):
            # the first condition indicates non-empty stack and the second condition implies 
            # there is a right upper bound 
            # thus the condition inside the while loop being true implies there are water trapped 
            while ( len(stack) != 0 and height[ stack[-1] ] < height[i] ):
                top = stack.pop()
                lowerheight = height[top]
                # important , since we popped an item before , if the stack is empty then there wont be any water trapped 
                # since for water to be trapped , there MUST be a bottom existed.
                if len(stack) == 0 :
                    break
                leftUpperIndex = stack[-1]

                # calculate the width of current trapped water
                trapped_water_width = i - leftUpperIndex - 1
                if (height[leftUpperIndex] < height[i] ):
                    trapped_water_height = height[leftUpperIndex] - lowerheight
                else:
                    trapped_water_height = height[i] - lowerheight
                total_water += trapped_water_height*trapped_water_width
            
            # if stack is empty, simply push the index onto the stack 
            stack.append(i)    
        return total_water