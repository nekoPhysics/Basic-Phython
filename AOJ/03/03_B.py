#入力された数字を格納する型(ここではリスト)を空で定義する
box_list = []
#一時的に0を入れておく
X = 0
#if内の条件に当てはまる限り、処理を繰り返す
while True:
    #Xに整数として入力
    X = int(input())
    #数がゼロになった場合に処理を停止
    if X == 0:
        break
    #それ以外の時は数を入力    
    box_list.append(X)    
#len関数を利用してオブジェクトの数を取得、forを利用して取得個数分だけ出力を行う(繰り返し)
#rangeを利用してオブジェクトの数の分だけ連番をセット
for y in range(len(box_list)):
    #変数Xに入れられたリストを先頭より出力する
    print('Case {}: {}'.format(y+1, box_list[y]))    
