# pip install sympy

from sympy import isprime

temp = int(input('整数を入力してください >'))

if temp >= 2:
    if isprime(temp) == True:
        print('{}は素数です'.format(temp))
    else:
        print('{}は素数ではありません'.format(temp))
else:
    print('2以上の整数を入力してください')