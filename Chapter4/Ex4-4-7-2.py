def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n -= 1
    return num

temp = int(input('整数を入力してください >'))

print('{}!={}'.format(temp,factorial(temp)))