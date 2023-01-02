W, H, x, y, r = map(int,input().split())
#x軸に対して負の方向に円がはみ出る場合
if x - r < 0:
    print("No")
#x軸に対して正の方向に円がはみ出る場合
elif x + r > W:
    print("No")
#y軸に対して負の方向に円がはみ出る場合
elif y - r < 0:
    print("No")
#y軸に対して正の方向に円がはみ出る場合
elif y + r > H:
    print("No") 
#その他の場合、円ははみ出ない.
else:
    print("Yes")       