N, K = [int(i) for i in input().split()]
w=set(range(6, N+1, 7))
w.update(set(range(7, N+1, 7)))
strikes=set()
for i in range(K):
    A, B = [int(j) for j in input().split()]
    S=set(range(A, N+1,B))
    strikes.update(S)
strikes-=w
print(len(strikes))