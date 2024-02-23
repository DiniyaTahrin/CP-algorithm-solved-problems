s=input()
ps=[]
summ=0
for j in range(len(s)-1):
    if s[j]==s[j+1]:
        summ+=1
    ps.append(summ)
ps.append(summ)
m=int(input())
for _ in range(m):
    l, r = map(int,input().split())
    r-=2
    l-=1
    if l!=0:
        print(ps[r]-ps[l-1])
    else:
        print(ps[r])