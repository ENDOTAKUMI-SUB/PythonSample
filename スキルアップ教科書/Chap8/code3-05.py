from decimal import Decimal, getcontext, FloatOperation

# float トラップを有効にする
getcontext().trap[FloatOperation]

Decimal(0.1)
