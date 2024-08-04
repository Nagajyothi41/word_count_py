n=input().split()
k=[]
for i in n:
    if i not in k:
        k.append(i)
for j in range(len(k)):
    print(k[j]+":",str(n.count(k[j])))
    