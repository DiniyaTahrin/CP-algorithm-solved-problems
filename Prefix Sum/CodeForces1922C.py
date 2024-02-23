T=int(input())
for _ in range(T):
    n=int(input())
    li=list(map(int,input().split()))
    m=int(input())
    ps=[]
    revPs=[]
    for i in range(n-1):
        if i==0:
            ps.append(1)
            revPs.append(1)
        else:
            backw=(li[i]-li[i-1])
            forw=li[i+1]-li[i]
            revForw=li[n-1-i]-li[n-2-i]
            revBackw=li[n-i]-li[n-1-i]
            if forw<backw:
                ps.append(ps[i-1]+1)
            else:
                ps.append(ps[i-1]+forw)
            if revForw<revBackw:
                revPs.append(1)
            else:
                revPs.append(revForw)
    revPs.reverse()
    r=[]
    suu=0
    for i in range(n-1):
        suu+=revPs[i]
        r.append(suu)
    for _ in range(m):
        x,y=map(int,input().split())
        if y>x:
            y-=2
            x-=1
            if x!=0:
                print(ps[y]-ps[x-1])
            else:
                print(ps[y])
        else:
            x-=2
            y-=1
            if y==0:
               print(r[x])
            else:
               print(r[x]-r[y-1])