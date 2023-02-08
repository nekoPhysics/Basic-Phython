while True:
#以下の条件式(if)に一致するまでループ処理を続ける。
    n, x = map(int, input().split())
    #いつも通りn,xに変数を入力。
    if n == 0 and x == 0:
        break
        #n,xがともに0で処理を停止。
    patternbox = 0
    #パターンを数えるするための箱を準備
    for a in range(1, n+1):
    #1~nまでオブジェクトをaに入力
        for b in range(a+1, n+1):
        #a+1からnまでをbに入力
            for c in range(b+1, n+1):
            #b+1からnまでをcに入力
                if a + b + c == x:
                    patternbox += 1
                    #abcの和がxの場合カウント
    print(patternbox)
    #patternbox内の要素を出力                    
            