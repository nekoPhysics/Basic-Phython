while True:
    numbersum = input()
    if numbersum == "0":
        break
        #要素が0になるまでループ処理を継続する。
    anser = 0
    #計算結果蓄積用の箱anser
    for n in numbersum:
    #一桁ずつnに入力
        anser += int(n)
        #intはinputの段階で使用するのはNG
        #anserに+=を使用してint(n)を足していく。
    print(anser)