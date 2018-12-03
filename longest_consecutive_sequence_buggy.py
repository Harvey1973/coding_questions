class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        '''
        Idea : Use Union find and hashtable 
        First pass : store element in the list in the hashtable with keys being their value
        Build an array of the same length and give each a different id 
        For each element in the list :
            check if (a[i] - 1 )  and (a[i]+1) are in the dict 
            if there is , and they have different id than a[i]
            dict[a[i]] ++ 

        '''
        if(nums == []):
            return 0

        lookup = {}
        id = []
        parent_id = {}

        n = len(nums)
        for e in range (n):
            if nums[e] in lookup :
                lookup[nums[e]].append(e)
            else:
                lookup[nums[e]] = [e]
        print(lookup)

        for e in range(n):
            id.append(e)
        print(id)

        for i in range(n) :
            print(nums[i])
            print(id)

            
            left = nums[i] - 1 
            right = nums[i] + 1
            


            if left in lookup:
                
                    
                target_index = lookup.get(left)[0]
                i_index =  lookup.get(nums[i])[0]

                
                if (id[target_index] != id[i_index]):
                    #id[target_index] = id[i_index]
                    id[i_index] = id[target_index]
                    if (left - 1) in lookup:
                        target_index = lookup.get(left - 1)[0]
                        id[target_index] = id[i_index]
                    
            if right in lookup:

                target_index = lookup.get(right)[0]
                i_index =  lookup.get(nums[i])[0]
                
                #print(target_index)
                if (id[target_index] != id[i_index]):
                    id[target_index] = id[i_index]
                    if (right + 1) in lookup:
                        target_index = lookup.get(right + 1)[0]
                        id[target_index] = id[i_index]
                
                    
                    #id[i_index] = id[target_index]
        print(id)
        most_common = max(set(id), key = id.count) 

        print(most_common)
        res = id.count(most_common)
        print(res)

        return res

                


                

obj = Solution()
nums = [100,4,100,1,3,2]
nums2 = [1,2,3,4,1,2,3,4,5]
nums3 = [1,3,5,2,4]
nums4 = [0,3,7,2,5,8,4,6,0,1]
obj.longestConsecutive(nums4)