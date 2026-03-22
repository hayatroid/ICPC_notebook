---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: src/data_structure/DSU.py
    title: src/data_structure/DSU.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/unionfind
    links:
    - https://judge.yosupo.jp/problem/unionfind
  bundledCode: "Traceback (most recent call last):\n  File \"/home/runner/work/ICPC_notebook/ICPC_notebook/.venv/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/home/runner/work/ICPC_notebook/ICPC_notebook/.venv/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind\n\
    from src.data_structure.DSU import DSU\n\n\nN, Q = map(int, input().split())\n\
    dsu = DSU(N)\nfor _ in range(Q):\n    t, u, v = map(int, input().split())\n  \
    \  if t == 0:\n        dsu.unite(u, v)\n    else:\n        print(int(dsu.same(u,\
    \ v)))\n"
  dependsOn:
  - src/data_structure/DSU.py
  isVerificationFile: true
  path: test/data_structure/DSU.test.py
  requiredBy: []
  timestamp: '2026-03-22 11:50:10+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/data_structure/DSU.test.py
layout: document
redirect_from:
- /verify/test/data_structure/DSU.test.py
- /verify/test/data_structure/DSU.test.py.html
title: test/data_structure/DSU.test.py
---
