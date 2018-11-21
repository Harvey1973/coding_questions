class Solution(object):
    def findMedianSortedArrays(self,a,b):
        if len(a) == 0:
            if len(b) == 1:
                return b[0]
            b_index = int (len(b)/2)
            if len(b)%2 != 0:
                return b[b_index]
            else:
                return (b[b_index-1] + b[b_index])/2.0
        if len(b) == 0:
            if(len(a) ==0):
                return a[0]
            a_index = int(len(a)/2)
            if(len(a)%2 != 0):
                return a[a_index]
            else:
                return (a[a_index-1] + a[a_index])/2.0
        total_length = len(a) + len(b) 
        result = [0]*total_length
        i = 0
        j = 0
        k = 0
        while i < len(a) or j < len(b):
            if (a[i] < b[j]):
                result[k] = a[i]
                i += 1 
            else:
                result[k] = b[j]
                j += 1
            k = k + 1

            if (i == len(a)):
                leftover = int (total_length/2) + 1 - i - j
  
                for e in range (leftover):
                    if len(b) > len(a):
                        result[i+e+j] = b[j + e]
                    else:
                        result[i+e] = b[j + e]
                break
            if (j == len(b)):
                leftover = int (total_length/2) + 1 - j - i
  
                for e in range (leftover):
                    if len(a) > len(b):
                        result[j+e+i] = a[i + e]
                    else:
                        result[j+e] = a[i+e]
                break

        index = int (total_length / 2)
        print(result)
        print(index)
        if len(result)%2 == 0 :
        
            median = float ((result[index-1] + result[index ])) / 2
            print(median)
        else: 
            median = result[index]
        return median 
sol = Solution()
a = [1,2]
b = [3,4]
print(sol.findMedianSortedArrays(a,b))