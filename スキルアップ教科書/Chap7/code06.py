def to_int(x):
	try:
		return int(x)
	except:
		return None

print(to_int('a'))
print(to_int('5'))