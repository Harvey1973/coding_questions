class Solution(object):
    def twoSum(self,nums, target):
        sort_nums = sorted(nums)
        for i in range (len(nums)):
            elem = target - sort_nums[i]
            result = self.binary_search(elem, sort_nums[(i+1):])
            if ( result !=None ):
                first_index = nums.index(sort_nums[i])
                if (sort_nums[i] == result): 
                    second_index = nums[(first_index+1):].index(result) + first_index + 1
                else :
                    second_index = nums.index(result)
                return sorted([first_index,second_index])
    def binary_search(self,target,array):
        if len(array) == 1 :
            if (array[0] == target):

                return array[0]
            else:
                return None
        mid = int (len(array)/2)
        if array[mid] == target :
            return array[mid] 
        if target < array[mid]:
            return (self.binary_search(target,  array[0:(mid)]))
        else: 
            return (self.binary_search (target,  array[mid:]))
obj = Solution()        
nums = [2,7,11,15]
print(obj.twoSum(nums,9))