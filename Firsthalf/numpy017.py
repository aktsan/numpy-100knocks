#What is the result of the following expression? (★☆☆)
#nan = not a number 
#inf = 正の無限大を意味する特殊な浮動小数点
import numpy as np
a = 0 * np.nan #nanの四則演算は全てnan
b = np.nan == np.nan #非数の比較はfalse
c = np.inf > np.nan 
d = np.nan - np.nan 
e = np.nan in set([np.nan]) # is,inは比較ではないのでTrue
f = 0.3 == 3 * 0.1 #浮動小数点では二進数と十進数で同じ数値を表現できないから
print(a,b,c,d,e,f)