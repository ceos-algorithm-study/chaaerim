from turtle import back


num=input()

numLength=len(num)//2
frontCount=0
backCount=0

for i in range(numLength):
    frontCount+=int(num[i])
    backCount+=int(num[i+numLength])

if (frontCount==backCount):
    print('LUCKY')
else:
    print('READY')
