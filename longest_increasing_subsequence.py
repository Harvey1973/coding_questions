class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1-d dp 
        n = len(nums)
        if n == 0:
            return 0
        else:   
            dp = [0]*(n)
            dp[0] = 1 

        for i in range (1,n):
            candidates = []

            for e in range (i):
                if (nums[i] > nums [e]):
                    candidates.append(dp[e])
            if candidates == []:
                dp[i] = 1
            else:
                dp[i] = 1 + max(candidates)
        print(max(dp))
        return max(dp)

obj = Solution()
a = [10,9,2,5,3,7,101,18]
obj.lengthOfLIS(a)    