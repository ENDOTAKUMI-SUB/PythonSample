a = [40, 22, 55, 35, 10]
i = 0
while i <= 3:
    k = i
    j = i + 1
    while j <= 4:
        if a[j] < a[k]:
            k = j
        j += 1
    if i != k:
        w = a[i]
        a[i] = a[k]
        a[k] = w
    i += 1
    print(a)