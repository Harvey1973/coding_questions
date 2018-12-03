class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_streak = 0
        
        array = set(nums)

        for e in nums :
            current_streak = 0
            # if e - 1 not in array , then it means it is the start of a streal
            if e - 1 not in array :
                current_number = e 
                current_streak = current_streak + 1

                while current_number + 1 in array :
                    current_number = current_number + 1 
                    current_streak = current_streak + 1
            longest_streak = max (longest_streak, current_streak)
        return longest_streak


obj = Solution()
nums = [100,4,100,1,3,2]
nums2 = [1,2,3,4,1,2,3,4,5]
nums3 = [1,3,5,2,4]
nums4 = [0,3,7,2,5,8,4,6,0,1]

print(obj.longestConsecutive(nums4))