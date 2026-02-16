import mathtools as mt

class point2D:
    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y
        self._shape: int = 2

    @property
    def shape(self) -> int:
        return self._shape

    def __str__(self) -> str: return f'<{self.x}, {self.y}> in {self._shape}D'

    def __eq__(self, other) -> bool:
        if not isinstance(other, point2D): return False
        return other.x == self.x and other.y == self.y
    def __ne__(self, other): return not self.__eq__(other)
    
class point3D(point2D):
    def __init__(self, x: float, y: float, z: float) -> None:
        point2D.__init__(self, x, y)
        self.z: float = z
        self._shape = 3

    def __str__(self) -> str: return f'<{self.x:.2f}, {self.y:.2f}, {self.z:.2f}> in {self.shape}D'

    def __eq__(self, other) -> bool:
        return super().__eq__(other) and other.z == self.z
    def __ne__(self, other): return not self.__eq__(other)

class circle():
    def __init__(self, center: point2D, radius: float) -> None:
        self.center: point2D = center
        self._radius: float = radius # Major axle shaft

    @property
    def radius(self) -> float:
        return self._radius
    
    @radius.setter
    def radius(self, radius: float) -> None:
        if radius <= 0: raise ValueError('The argument \'radius\' must be greater than 0')
        self._radius = radius

    def __str__(self) -> str: return f"Center: <{self.center.x}, {self.center.y}>; Radius: {self._radius}"

    def area(self) -> float: return mt.PI * self._radius * self._radius

    def perimeter(self) -> float: return 2 * mt.PI * self._radius

class ellipse():
    def __init__(self, center: point2D, a: float, b: float) -> None:
        self._a: float = a
        self._b: float = b
        self.center: point2D = center

    def area(self) -> float: return mt.PI * self._a * self._b

    def perimeter(self) -> float: return mt.PI*(3*(self._a + self._b) - mt.NewtonRaphsonRoot((3*self._a + self._b)*(self._a + 3*self._b), 2)[0])

    def eccentricity(self) -> float: return mt.NewtonRaphsonRoot(1 - (self._b * self._b) / (self._a * self._a), 2)[0]

    def focalDistance(self) -> float: return mt.NewtonRaphsonRoot(self._a * self._a - self._b * self._b, 2)[0]

    def directrix(self) -> float: return self._a / self.eccentricity()


    @property
    def a(self) -> float:
        return self._a
    @a.setter
    def a(self, a: float) -> None:
        if a <= 0: raise ValueError('The argument \'a\' must be greater than 0')
        self._a = a

    @property
    def b(self) -> float:
        return self._b
    @b.setter
    def b(self, b: float) -> None:
        if b <= 0: raise ValueError('The argument \'b\' must be greater than 0')
        self._b = b

    def __str__(self) -> str: return f"Center: <{self.center.x}, {self.center.y}>; a: {self._a}; b: {self._b}"

def EuclideanDistance(p1: point2D, p2: point2D):
    return mt.Newton_Raphson_root(p1.x * p2.x + p1.y * p2.y, 2)[0]
def EuclideanDistance(p1: point3D, p2: point3D):
    return mt.Newton_Raphson_root(p1.x * p2.x + p1.y * p2.y + p1.z * p2.z, 2)[0]

def middlePoint(p1: point2D, p2: point2D):
    return point2D((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)
def middlePoint(p1: point3D, p2: point3D):
    return point3D((p1.x + p2.x) / 2, (p1.y + p2.y) / 2, (p1.z + p2.z) / 2)