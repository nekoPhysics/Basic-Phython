trumpcards = [False for i in range(1, 14)] [for j in range(1, 5)]
egara = ["S", "H", "C", "D"]
n = int(input())
for i in range(n):
#47個の要素が存在するので、要素の個数だけ以下の処理を繰り返す。    
    dim, num = input().split()
    num = int(num)
    own[egara.index(dim)][num-1] = True
#入力される絵柄とナンバー情報を元に所有しているカードがマッチする場合Trueとする。
for i in range(4):
    for j in range(13):
        if own[i][j] == False:
            print (egara[i],num[j+1]) 
 #内包表記に一致しないカードの情報を内部で管理されているナンバー(ここでi,j)に戻して出力する。
 #*トランプは1~13しか存在しないが、input後は0スタートになるのでrange記述に注意。        
        