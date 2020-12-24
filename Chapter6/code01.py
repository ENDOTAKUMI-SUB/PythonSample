tpl = '3人目は{}さん'
names = ['松田', '浅木']
names.append('工藤')
message = tpl.format(names[2])
print(message)