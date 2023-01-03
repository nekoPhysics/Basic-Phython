#入力された数字を格納する型(ここではリスト)を空で定義する
box_list = []
#一時的に0を入れておく
numbers = 0
#if内の条件に当てはまる限り、処理を繰り返す
while True:
    #box_listに整数として入力
    box_list = int(input())
    #リスト内がゼロになった場合に処理を停止
    if box_list == 0:
        break
    #それ以外の時は数を入力    
    box_list.append(numbers)    
#len関数を利用してオブジェクトの数を取得、forを利用して取得個数分だけ出力を行う(繰り返し)
#rangeを利用してオブジェクトの数の分だけ連番をセット
for X in range(len(box_list)):
    #変数Xに入れられたリストを先頭より出力する
    print('Case {}: {}'.format(X+1, box_list[X]))    
