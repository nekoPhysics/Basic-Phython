n = int(input())
#変数nに整数として入力
Xlist = list(map(int, input().split())
#"Xlist"に分割して繰り返し登録する
Xlist.reverse()
#reverse()を利用してリスト内の要素を逆順にする
print(*Xlist)