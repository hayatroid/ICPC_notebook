class DSU:
    def __init__(self, n):
        self.par = list(range(n))
    def find(self, x):
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    def unite(self, x, y):
        self.par[self.find(x)] = self.find(y)
    def same(self, x, y):
        return self.find(x) == self.find(y)
