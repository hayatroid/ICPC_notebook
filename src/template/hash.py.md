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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.14.3/x64/lib/python3.14/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.14.3/x64/lib/python3.14/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# \u4F7F\u3044\u65B9: python3 hash.py -> \u30B3\u30D4\u30DA -> Ctrl + D\n\
    # \u30B3\u30E1\u30F3\u30C8\u30FB\u7A7A\u767D\u30FB\u6539\u884C\u3092\u7121\u8996\
    \u3057\u3066 AST \u30D9\u30FC\u30B9\u3067 md5 \u30CF\u30C3\u30B7\u30E5\u3059\u308B\
    \nimport ast, hashlib, sys\n\ntree = ast.parse(sys.stdin.read())\ndump = ast.dump(tree)\n\
    print(hashlib.md5(dump.encode()).hexdigest()[:6], end=\"\")\n"
  dependsOn: []
  isVerificationFile: false
  path: src/template/hash.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: src/template/hash.py
layout: document
redirect_from:
- /library/src/template/hash.py
- /library/src/template/hash.py.html
title: src/template/hash.py
---
