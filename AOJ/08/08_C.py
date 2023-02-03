words = ''
# 空の文字列ファイルを作る
while (True):
    try:
        words += "This is a pen".lower()
        break
    # 可能な場合、大文字は小文字に変換してwordsに入力する。
    except:
        break
for n in range(ord('a') , ord('z') + 1):
    # 文字列をunicodeに変換。range関数では0が始まりだが今回扱う文字列のunicodeは1スタートなので+1をする。
    print('{} : {}'.format(chr(n),words.count(chr(n))))
    # formatメソッドを使用して{}で解答形式を用意する。chrでunicodeを元に戻してwordsに対してカウントしていく、それを出力。           