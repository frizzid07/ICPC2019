from collections import defaultdict
def look(a):
    result = defaultdict(list)
    for pair in a:
        result[pair[0]].append(pair[1])
    for key,val in result.items():
        mi=val.count("1")
        maa=val.count("0")
        ans.append(max(mi,maa))
    print(sum(ans))

a=[]
ans=[]
n= int(input())
for i in range(n):
    a=[]
    ans=[]
    n1 = int(input())
    for j in range(n1):
        k,v=input().split()
        
        a.append((k,v))
    look(a)
