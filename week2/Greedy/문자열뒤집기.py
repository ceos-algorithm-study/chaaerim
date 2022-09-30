num=list(map(int, input()))

makeZero=0
makeOne=0

# 101010 입력하면 2가 나옴 .. 왜 ? 첫번째 원소 따로 처리 필요. 

if num[0]==0:
    makeZero+=1
elif num[0]==1:
    makeOne+=1

for i in range(len(num)-1):
    if (num[i]!=num[i+1]):
        if(num[i+1]==0):
            makeZero+=1
        else:
            makeOne+=1

print(min(makeOne, makeZero))