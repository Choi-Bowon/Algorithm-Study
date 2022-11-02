X=int(input())
N=int(input())
total=0
for i in range(N):
    price, cnt=map(int,input().split())
    total+=price*cnt
if X==total:
    print('Yes')
else:
    print('No')