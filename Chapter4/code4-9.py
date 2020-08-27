ages = [28, 50, 8, 20, 78, 25, 22, 10, 27, 33] # 対象データ
num = 5          # 目標の抽出数
samples = list() # サンプルデータを格納するリスト
for age in ages:
    if 20 <= age < 30:
        if len(samples) < num:
            samples.append(age)
print(samples)