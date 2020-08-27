temp = int(input('整数を入力してください >'))


primes = []
for n in range(2, temp + 1):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        primes.append(n)
if temp >= 2:
    if (temp in primes) == True:
        print('{}は素数です'.format(temp))
    else:
        print('{}は素数ではありません'.format(temp))
else:
    print('2以上の整数を入力してください')