---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/home/runner/work/ICPC_notebook/ICPC_notebook/.venv/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/home/runner/work/ICPC_notebook/ICPC_notebook/.venv/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# \u6A19\u6E96\u5165\u529B\u304B\u3089 Python \u30D5\u30A1\u30A4\u30EB\u3092\
    \u53D7\u3051\u53D6\u308A\u3001\u30B3\u30E1\u30F3\u30C8\u30FB\u7A7A\u767D\u30FB\
    \u6539\u884C\u3092\u7121\u8996\u3057\u3066 AST \u30D9\u30FC\u30B9\u3067 md5 \u30CF\
    \u30C3\u30B7\u30E5\u3059\u308B\nimport ast, hashlib, sys\n\nif __name__ == \"\
    __main__\":\n    tree = ast.parse(sys.stdin.read())\n    dump = ast.dump(tree)\n\
    \    print(hashlib.md5(dump.encode()).hexdigest()[:6], end=\"\")\n"
  dependsOn: []
  isVerificationFile: false
  path: build/hash.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: build/hash.py
layout: document
redirect_from:
- /library/build/hash.py
- /library/build/hash.py.html
title: build/hash.py
---
