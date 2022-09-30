
num=input()

result=0
mulResult=1

# 만약 i 가 0이면 더하기 
# i 가 0 이 아니면 곱하기. 
for i in num:
    if(int(i)!=0):
        mulResult*=int(i)
    else:
        result+=int(i)

print(result+mulResult)