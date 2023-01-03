#数列の末端の数、nをint型で入力
n = int(input())
#map関数で反復し、文字の数の分だけ文字列を入力→int型に変換→list関数でリストを作成する
#listの名前をSとする
S = list(map(int, input().split()))
#リスト内より、最小,最大,和の順番で出力
print(min(S),max(S),sum(S))