s = input()
p = input()

s = s*2
if s.find(p):
# まずpがsの中に含まれるかどうかを検索する。   
    if len(p)>len(s)/2:
        print("No")
    # pの文字数がsよりも長い時を弾く。（円形を文字列で再現しているため、2周目で異常文字列が出てくるのを防ぐ）    
    else:
        print("Yes")

###　以下テスト ###
'''
s = "apple"
p = "ppl"

s = s*2
if s.find(p):
# まずpがsの中に含まれるかどうかを検索する。   
    if len(p)>len(s)/2:
        print("No")
    # pの文字数がsよりも長い時を弾く。（円形を文字列で再現しているため、2周目で異常文字列が出てくるのを防ぐ）    
    else:
        print("Yes")
'''