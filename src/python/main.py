import mathtools as mt
import math as m

print(mt.interval_halving_method(lambda x: 5-m.exp(x), 0, 2))