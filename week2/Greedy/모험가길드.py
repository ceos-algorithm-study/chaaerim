n=int(input())

panic=input()
panic=panic.replace(' ', '')

# 리스트 정렬은 sort/ 문자열 정렬은 sorted를 사용
panic=sorted(panic)
groupMem=0
groups=0

for i in panic:
    groupMem+=1
    if(int(i)<=groupMem):
        groups+=1
        groupMem=0
print(groups)