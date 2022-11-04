# 가장 인접한 공유기 사이의 거리의 최댓값을 탐색하는 문제 
# 좌표의 범위가 10억이므로 이진탐색으로 풀어야 할 것. 
# 파라메트릭 서치 문제 유형은 이진탐색을 반복문을 이용해서 구현하면 더 간결하게 문제 풀이 가능


# 집 개수 , 공유기 개수 입력받기
n,c=map(int, input().split())

# 집의 좌표를 한 줄에 하나씩 나타내기 
data=[]
for i in range(n):
    data.append(int(input()))

data.sort()

start=1
end=data[len(data)-1]-data[0]

while(start<=end):
    total=0
    mid=(start+end)//2
    for i in data:
        if i >mid:
            total+=i-mid
        if total<mid:
            end=mid-1
        else: 
            result=mid
            start=mid+1

print(result)