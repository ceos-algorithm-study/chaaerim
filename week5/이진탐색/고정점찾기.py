# 이 문제는 시간복잡도 O(logN)으로 알고리즘을 설계하지 않으면 시간초과 판정을 받음. 
# -> 이진탐색으로 풀자

# 이진탐색 소스코드 (재귀함수)

n=int(input())
data=list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start>end:
        return None

    mid=(start+end)//2
    if array[mid]==target:
        return array[mid]
    elif array[mid]>target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

answer=[]
for i in range(n):
    result=binary_search(data, i, 0, n-1)
    if result!=None:
        answer.append(result)

if len(answer)!=0:
    for i in answer:
        print(i, end=' ')
else:
    print(-1)