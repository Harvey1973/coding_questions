




# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, interval):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        
        '''using set 
        
        
        interval = []
        for e in intervals:
            interval.append([e.start,e.end])
        
        '''
        
        # first sort the intervals by their first value 
        interval.sort(key = lambda x : int(x[0]))
        print('!!')
        print(interval)
        interval_maps = {}
        result = []
        n = len(interval)
        array = [False]*n
        for e in range(n):
            print('outerloop')
            print(array[e])
            left = interval[e][0]
            right = interval[e][1]
            if array[e] == False:

                seta = set(range(left,right + 1))  
                print(seta)
                start = left
                end = right
                for i in range(e+1,n):
                    lefta = interval[i][0]
                    righta =  interval[i][1]
                    setb = set(range(lefta,righta + 1))
                    print(interval[i])
                    print(setb)
                    if (seta & setb != set()):
                        print(seta)
                        print(setb)
                        print(seta & setb)
                        merged_range = seta|setb
                        print('merged')
                        print(merged_range)
                        start = min(merged_range)
                        end = max(merged_range)
                        seta = set(range(start,end + 1))
                        array[e] = True
                        array[i] = True
                        print(array)
                interval_maps[str(start)] = end
            if array[e] == False:
                interval_maps[str(left)] = right
        for k,v in interval_maps.items():
            result.append([int(k),v])
        #print(result)

        #return interval_maps
        return result

a = [[1,3],[2,6],[8,10],[15,18]]
b = [[1,4],[4,5]]
c= [[1,3],[2,4],[7,10],[5,8]]
d = [[1,3],[4,5]]
e = [[7,7],[5,7],[6,8],[2,3]]
obj = Solution()
print(obj.merge(e))