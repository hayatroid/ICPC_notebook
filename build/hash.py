# 標準入力から Python ファイルを受け取り、コメント・空白・改行を無視して AST ベースで md5 ハッシュする
import ast, hashlib, sys

tree = ast.parse(sys.stdin.read())
dump = ast.dump(tree)
print(hashlib.md5(dump.encode()).hexdigest()[:6], end="")
