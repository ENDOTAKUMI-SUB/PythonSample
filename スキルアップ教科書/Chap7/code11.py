import datetime
try:
	raise Exception('RaiseTest', datetime.datetime.now())
except Exception as inst:
	print(inst)