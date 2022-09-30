s=input()


# 문자열 길이만큼 다 잘라보자

# 문자열 길이 답으로 출력할 것. 
ans=len(s)
for j in range(1, len(s)):
    newString=""
    prev=s[0:j]

    # 비교할 문자열 하나는 존재. 
    count=1
    for i in range(j, len(s), j):
        if(prev==s[i:i+j]):
            count+=1
        else:
            if count>=2:
                newString+=str(count)+prev
            else:
                newString+=prev
                prev=s[i:i+j]
                count=1
    if count>=2:
        newString+=str(count)+prev
    else:
        newString+=prev
    ans=min(ans, len(newString))

print(ans)