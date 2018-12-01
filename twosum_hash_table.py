class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        # put everything in a hashtable 
        for i in range (len(nums)):
            map[str(i)] = nums[i]
        # create inverse mapping
        inv_map = {v: k for k, v in map.items()}
        for i in range(len(nums)):
            elem = target - nums[i]
            if elem in map.values():
                index = int(inv_map[elem])
                return (i,index)
obj = Solution()        
nums = [0,7,11,0,1,0]
print(obj.twoSum(nums,0))
                
                