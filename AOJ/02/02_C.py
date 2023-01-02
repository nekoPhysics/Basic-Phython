#入力
numbers_list = list(map(int, input().split()))
#並べ替え
numbers_list.sort(reverse=False)
#リスト内部を抽出して表示
print(*numbers_list)