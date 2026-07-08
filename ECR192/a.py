def solution():
    k=int(input())
    c=[for int(i) for i in range(input().split()]

    cnt2=0
    for val in c:
        if val>=3:
            print("YES")
            return
        else:
            cnt2+=(val==2)
    
    if cnt2>1:
        print("YES")
    else:
        print("NO")



for _ in range(int(input())):
    solution()