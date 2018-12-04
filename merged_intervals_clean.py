class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        
        '''
        sort intervals by start 
        '''
        merged = []
        intervals.sort(key=lambda x: x.start)
        for e in intervals:
            if not merged or merged[-1] < e.start:
                merged.append(e)
            else :
                merged[-1] = max(merged[-1].end,e.end)
        return merged
