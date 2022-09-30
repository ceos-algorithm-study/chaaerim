n, m=map(int, input().split())

data=list(map(int, input().split()))

count=0

for i in range(len(data)-1):
    for j in range(len(data)):
        if(i+j+1>=len(data)):
            break
        elif(data[i]!=data[i+j+1]):
            count+=1


print(count)