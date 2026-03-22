# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind
from src.data_structure.DSU import DSU


N, Q = map(int, input().split())
dsu = DSU(N)
for _ in range(Q):
    t, u, v = map(int, input().split())
    if t == 0:
        dsu.unite(u, v)
    else:
        print(int(dsu.same(u, v)))
