from collections import Counter

def solution(N, stages):
    answer = []
    stages.sort()
    
    #중복된 값 세어서 dictionary로 만들기 
    counter=dict(Counter(stages))
    
    #딕셔너리 튜플로 변경
    counter=list(counter.items())
    result=[]
    total=0
    fail=[]
    print(counter)
    
    a=[]
    for i in range(len(counter)):
        a.append(counter[i-1][0])
      
        # if (i in a):
        #     counter.append((i, 0))
    print(a)
    
    for i in range(1, N+1):
        if (i not in a):
            counter.append((i, 0))
    
    for i in range(len(counter)):
        total+=counter[len(counter)-1-i][1]
        fail.append(total)

        
    fail.reverse()
    print(fail)
      
    # 실패율 구하기
    for i in range(len(counter)):
        if fail[i]!=0:
             result.append((counter[i][0], counter[i][1]/fail[i]))
        else:
            result.append((counter[i][0], 0))
    # 내림차순 정렬
    result.sort(key=lambda x:(-x[1]))
    print(result)
    for i in range(len(result)):
        if result[i][0]<=N:
            answer.append(result[i][0])
    

    print(answer)

    return answer