def solution(S, K):
    # write your code in Python 3.6
    S = ''.join(S.split('-')).upper()
    S = S[::-1]
    print(S) 
    n = len(S)
    res = []
    for e in range(0,n,K):
        res.append(S[e:e+K][::-1])
    return '-'.join(list(res)[::-1])


a = "2-4A0r7-4k"
print(''.join(a.split('-')))
print(solution(a,4))