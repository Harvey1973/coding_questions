class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        Idea : Using hash map 
        map[n] denotes the length of sequence that has number n as a boundary point (start point , end point or connecting point)
        '''
        maps = {}
        res = 0
        for e in nums :
            sums = 0
            if e not in maps :
                #print(maps.get(e-1))
                if maps.get(e - 1) != None:
                    left = maps.get(e - 1)
                else :
                    left = 0

                if maps.get(e + 1) != None:
                    right = maps.get(e + 1)
                else :
                    right = 0


                sums = left + right + 1
                res = max(res,sums)
                maps[e] = sums
                

                maps[e - left] = sums
                maps[e + right] = sums
                print(maps)
            else :
                continue
        return res
obj = Solution()
nums = [100,4,100,1,3,2]
nums2 = [1,2,3,4,1,2,3,4,5]
nums3 = [1,3,5,2,4]
nums4 = [0,3,7,2,5,8,4,6,0,1]
nums5 = [1,2,3,4,5]
print(obj.longestConsecutive(nums))

