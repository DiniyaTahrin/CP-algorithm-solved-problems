T=int(input())
for _ in range(T):
    d=int(input())
    low=0
    high=d
    if d==0:
        print("Y", "0.000000000", "0.000000000")
    elif d<4:
        print("N")
    elif d==4:
        print("Y", "2.000000000", "2.000000000")
    else:
        while high-low>=10**-10:
            mid=(low+high)/2
            if (mid*(d-mid))>d:
                low=mid
            else:
                high=mid
        print("Y",low,d-low)
