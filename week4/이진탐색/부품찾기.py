import sys
# 데이터 개수 1,000,000개 까지 입력 가능 보통 데이터 개수 천만개가 넘어가면 이진탐색으로 풀자 

n=int(input())

inputData=sys.stdin.readline().rstrip()
inputData=inputData.split()

m=int(input())

searchData=sys.stdin.readline().rstrip()
searchData=searchData.split()

def binary_search(array, target, start, end):
    if start>end:
        return print('no', end=' ')
    mid=(start+end)//2

    if array[mid]==target:
        return print('yes', end=' ')

    # 중간값이 찾고자 하는 값보다 더 크면 왼쪽만 탐색
    elif array[mid]>target:
        return binary_search(array, target, start, mid-1)
    # 중간점이 찾고자 하는 값보다 더 작으면 오른쪽만 탐색
    else:
        return binary_search(array, target, mid+1, end)

for i in range(m):
    result=binary_search(inputData, searchData[i], 0, n-1)
