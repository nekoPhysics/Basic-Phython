#入力がTureの限り処理を実行する
while True:
    #a, op ,b をinput.split()を利用して入力
    #str型で文字列でmap関数に入力
    #なぜ最初からint型で入力を行わないのか？
    #→演算子opが含まれるから、これは数ではなく文字列に分類される
    #計算で利用できるようにstr型→int型で変換をする
    a, op ,b = map(str, input().split())
    a = int(a)
    b = int(b)
    #演算子opが"?"になった場合処理を停止する
    if op == "?":
        break
    #演算子に応じて処理を設定する(計算用数値にはint型を利用する)    
    #opが+の場合
    elif op == "+":
        print(int(a+b))  
    #opが-の場合
    elif op == "-":
        print(int(a-b))
    #opが*の場合
    elif op == "*":
        print(int(a*b))
    #opが/の場合
    elif op == "/":
        print(int(a/b))
    #opがそれ以外の場合は処理を行わない
    else:
        pass            