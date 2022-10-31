# 각각의 위치에서 더한 값을 다 계산한 뒤 정렬

n=int(input())

houses=list(map(int, input().split()))

distance=[]
for i in range(n):
    sum=0
    for j in range(n):
        sum+=abs(houses[i]-houses[j])
    distance.append((houses[i], sum))

# 튜플 두번째 원소로 오름차순 정렬하고 두번재 원소가 같다면 첫번째 원소로 정렬
distance.sort(key=lambda x:(x[1],x[0]))

# 튜플 첫번째 원소만 출력
print(distance[0][0])