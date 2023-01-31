Building = [[[0 for r in range(10)] for f in range(3)] for b in range(4)]
#要素が0の10部屋をfor関数で繰り替えし作成、同じくこれを3階層for関数で作成、さらにこの建物をfor関数で4つ建築する
n = int(input())
#最初に与えられる要素の数をnとし入力
for i in range(n):
#要素の数の分だけ処理を繰り返す。
    b, f, r, v = map(int, input().split())
    #与えられたbfrvをいつも通り入力
    Building[b - 1][f - 1][r - 1] += v
    #bfrの情報を元にv情報を+=を利用してBuildingに代入していく。
for b in range(4):
#b情報を表示(0~3)
    for f in Building[b]:
        print('', *f)
        #fの要素の数だけfの中身を表示(アスタリスクを利用)
    if b != 3:
        print('#' * 20)
        #不等価演算子!=を利用し、bの数量が3以外の時'#'を20個表示する            
