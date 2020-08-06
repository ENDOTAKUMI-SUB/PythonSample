print(0.7 + 0.2 + 0.1)


"""
# 正確に計算するコード

from decimal import *
getcontext().prec = 16
dec_var = Decimal("0.7")+Decimal("0.2")+Decimal("0.1")
print(dec_var)

"""
