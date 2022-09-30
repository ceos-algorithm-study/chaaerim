s=input()

arranged=sorted(s)

alphaArranged=[]
numArranged=[]

for i in arranged:
    if 65<=ord(i):
        alphaArranged.append(i)
    else:
        numArranged.append(i)

newArranged=alphaArranged+numArranged

print(''.join(newArranged))