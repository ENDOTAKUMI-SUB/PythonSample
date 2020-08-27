ages = [28, 50, 8, 20, 78, 25, 22, 10, 27, 33] # 対象データ
num = 5          # 目標の抽出数
samples = list() # サンプルデータを格納するリスト
for data in ages:
    if 20 <= data < 30:
        samples.append(data)
        if len(samples) == num:
            break
print(samples)
