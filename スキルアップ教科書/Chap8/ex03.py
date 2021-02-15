from decimal import Decimal

diff = 1000000000.2 - 1000000000
diff_d = Decimal("1000000000.2") - Decimal("1000000000")
print(diff)
print(diff_d)
