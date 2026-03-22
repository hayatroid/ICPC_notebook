---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/data_structure/DSU.test.py
    title: test/data_structure/DSU.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/home/runner/work/ICPC_notebook/ICPC_notebook/.venv/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/home/runner/work/ICPC_notebook/ICPC_notebook/.venv/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class DSU:\n    def __init__(self, n):\n        self.par = list(range(n))\n\
    \    def find(self, x):\n        while self.par[x] != x:\n            self.par[x]\
    \ = self.par[self.par[x]]\n            x = self.par[x]\n        return x\n   \
    \ def unite(self, x, y):\n        self.par[self.find(x)] = self.find(y)\n    def\
    \ same(self, x, y):\n        return self.find(x) == self.find(y)\n"
  dependsOn: []
  isVerificationFile: false
  path: src/data_structure/DSU.py
  requiredBy: []
  timestamp: '2026-03-22 11:50:10+00:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/data_structure/DSU.test.py
documentation_of: src/data_structure/DSU.py
layout: document
redirect_from:
- /library/src/data_structure/DSU.py
- /library/src/data_structure/DSU.py.html
title: src/data_structure/DSU.py
---
