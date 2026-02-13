import mathtools as mt
import geometry as gm
from random import randint
lst: gm.Point3D = [gm.Point3D(randint(0, 255), randint(0, 255), randint(0, 255)) for _ in range(5)]
for x in lst:
    print(x)