import sys; input = sys.stdin.readline

def result(s):
    s = s.replace(' ','')
    return eval(s)

for _ in range(int(input())):
    N = int(input())
    nums = [i for i in range(1,N+1)]
    res = []
    answer = '1'
    def back(i, answer):
        global res
        if len(answer) == (N*2-1):
            if result(answer) == 0:
                res.append(answer)
            return
        else:
            for j in range(i+1,N+1):
                for k in ['+'+str(j),'-'+str(j),' '+str(j)]:
                    answer += k
                    back(j, answer)
                    answer = answer[:-2]
    back(1, answer)
    res.sort()
    for r in res:
        print(r)
    print()