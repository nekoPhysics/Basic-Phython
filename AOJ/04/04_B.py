#高度な数式計算を行うためにpython-mathモジュールを使用する
import math 
#半径rを数(浮動小数点数)として入力する、float型を利用
r = float(input())
#.format(円の面積,円周の長さ)で表示
#0.00001 以下の誤差を含んでもよい→:.6f
#パイはmath.piで代入
print('{0:.6f} {1:.6f}'.format(r*r*math.pi, r*2*math.pi))