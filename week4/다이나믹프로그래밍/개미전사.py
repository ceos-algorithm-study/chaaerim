n=int(input())

food=list(map(int, input().split()))


print(food)
# 초기화
d=[0]*100

# i번째 식량창고를 털기 위해서는 i-2번째 식량창고를 털면 됨. 
# i-3 전부터는 고려할 필요가 없음.
d[0]=food[0]
d[1]=max( food[0], food[1])

# 2이상 n미만. range 함수 제대로 기억하기.... 
for i in range(2, n):
    d[i]=max(d[i-1], d[i-2]+food[i])

print(d[n-1])