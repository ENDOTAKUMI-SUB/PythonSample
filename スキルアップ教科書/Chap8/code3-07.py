from decimal import Decimal, ROUND_DOWN, ROUND_HALF_UP

#切り捨て
print(Decimal('7.325').quantize(Decimal('.01'), rounding=ROUND_DOWN))

#四捨五入
print(Decimal('7.325').quantize(Decimal('.01'), rounding=ROUND_HALF_UP))
