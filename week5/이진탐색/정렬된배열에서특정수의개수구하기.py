# 시간복잡도 O(logN)으로 설계하지 않으면 시간초과
# 이진탐색은 한 번 확인할 때마다 원소의 개수가 절반씩 줄어들기 때문에 시간 복잡도가 O(logN)
# 수열이 정렬되어 있으므로 target 보다 작고 큰 범위는 잘라서 길이를 구하면 되지 않을까...?
# 따라서 이진탐색 함수를 2개 작성하여 문제를 해결. 

n, x=map(int, input().split())
data=list(map(int, input().split()))


# x가 처음 등장할 때의 인덱스를 찾는 이진탐색 함수
def first_binary_search(array, target, start, end):
    if start>end:
        return None
    mid=(start+end)//2
    # 처음 등장하는 인덱스만 반환
    # 0번째 인덱스에 등장하거나 
    if (mid==0 or target>array[mid-1]) and target== array[mid]:
        return mid
    elif array[mid]>=target: # 중간값이 찾고자 하는 값보다 크면 왼쪽만 다시 확인
        return first_binary_search(array, target, start, mid-1)
    else: #중간값이 찾고자 하는 값보다 작으면 오른쪽만 확인 
        return first_binary_search(array, target, mid+1, end)


# x가 마지막으로 등장할 때의 인덱스를 찾는 이진탐색 함수
def last_binary_search(array, target, start, end):
    if start>end:
        return None
    mid=(start+end)//2
    # 마지막에 등자앟는 인덱스만 반환
    #찾고자 하는 값이 마지막에 등장하거나 
    if (mid==n-1 or target<array[mid+1]) and target==array[mid]:
        return mid
    elif array[mid]>target:
        return last_binary_search(array, target, start, mid-1)
    else:
        return last_binary_search(array, target, mid+1, end)


start_index=first_binary_search(data, x, 0, n-1)
last_index=last_binary_search(data, x, 0, n-1)

if start_index==None:
    result=-1
else:
    result=last_index-start_index+1
print(result)