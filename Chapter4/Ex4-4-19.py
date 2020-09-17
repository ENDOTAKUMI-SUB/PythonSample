a = [40, 20, 50, 30, 10]
i = 1
while i <= 4:
    w = a[i]
    j = i - 1
    while j >= 0 and a[j] > w:
        print('{} i:{} j:{} w:{}'.format(a,i,j,w))
        a[j + 1] = a[j]
        j -= 1
    print('{} i:{} j:{} w:{}'.format(a,i,j,w))
    a[j + 1] = w
    i += 1
print('{} i:{} j:{} w:{}'.format(a,i,j,w))