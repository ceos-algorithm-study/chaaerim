from collections import deque

# 수의 개수 입력
n=int(input())

# 수열 입력
# 반복문으로 여러줄 입력받는 상황에서는 반드시 sys.stdin.readline()을 사용해야 시간초과가 발생하지 않는다.
data=list(map(int, input().split()))

# 덧셈 뺄셈 곱셈 나눗셈
pl, mi, mul, di=map(int, input().split())

# 최소 최댓값 초기화
minResult=1e9
maxResult=-1e9


# BFS
queue=deque()
queue.append((1, data[0], pl, mi, mul, di))

while queue:
    # i는 인덱스 num은 현재 연산 결과, 나머지는 연산자 
    i, num, p, m, mu, d=queue.popleft()

    # 네 연산자 합이 n-1이 되면 연산 종료 결과값 비교 
    if i==n:
        minResult=min(minResult, num)
        maxResult=max(maxResult, num)
        
    else:
    #연산자 비교
        if (p>0):
          queue.append((i+1, num+data[i], p-1, m, mu, d))
        if (m>0):
            queue.append((i+1, num-data[i], p, m-1, mu, d))
        if(mu>0):
            queue.append((i+1, num*data[i], p, m, mu-1, d))
        if(d>0):
            queue.append((i+1, num//data[i], p, m, mu, d-1))


# 최댓값 먼저 출력
print(maxResult)
print(minResult)