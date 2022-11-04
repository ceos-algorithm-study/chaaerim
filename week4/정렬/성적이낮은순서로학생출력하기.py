# 학생 수 n입력 
n=int(input())

data=[]
result=[]
# n명의 학생정보 입력
for i in range(n):
    data.append(input().split())
    data[i][1]=int(data[i][1])

# 정렬 결과 출력
def setting(data):
    return data[1]
result=sorted(data, key=setting)


for i in range(n):
    print(data[i][0], end=' ')

