#真の場合処理を実行（ループ）
while True:
    x, y = map(int, input().split())
#x,yが0となった場合に処理を終了
    if x == 0 and y == 0:
        break
#大小関係に応じて表示（分岐）    
    elif x < y:
        print(x, y)
    else:
        print(y, x)            