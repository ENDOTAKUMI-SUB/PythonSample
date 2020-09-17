def log():
    print('{} i:{} j:{} w:{}'.format(a,i,j,w))

a = [40, 20, 50, 30, 10]
i = 1
while i <= 4:
    w = a[i]
    j = i - 1
    while j >= 0 and a[j] > w:
        log()
        a[j + 1] = a[j]
        j -= 1
    log()
    a[j + 1] = w
    i += 1
log()