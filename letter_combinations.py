#           2     3     4     5     6     7      8      9 
letters = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']


map = list(enumerate(letters,2))







def combination (s):
    result = []
    for i in range (len(s)):
        if (s[i] != '1'):
            if(i == 0):
                for e in map[int (s[0])-2][1]:
                    result.append(e)
            else:
                tmp = []
                for e in map[int (s[i])-2][1]:
                    tmp.append(e)
                result = permute_two(result,tmp)
        

    return result

def permute_two(a,b):
    res = []
    li = [[x,y] for x in a for y in b]
    for e in li :
        res.append("".join(e))
    return res


a = ['a','b','c']
b = ['d','e','f']
#print(permute_two(a,b))
print(combination("231"))




