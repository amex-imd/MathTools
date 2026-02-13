import mathtools as mt

class Point2D:
    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y
        self.shape: int = 2

    def __str__(self) -> str: return f'<{self.x}, {self.y}> in {self.shape}D'

    def __eq__(self, other) -> bool:
        if not isinstance(other, Point2D): return False
        return other.x == self.x and other.y == self.y
    def __ne__(self, other): return not self.__eq__(other)
    
class Point3D(Point2D):
    def __init__(self, x: float, y: float, z: float) -> None:
        Point2D.__init__(self, x, y)
        self.z: float = z
        self.shape = 3

    def __str__(self) -> str: return f'<{self.x:.2f}, {self.y:.2f}, {self.z:.2f}> in {self.shape}D'

    def __eq__(self, other) -> bool:
        return super().__eq__(other) and other.z == self.z
    def __ne__(self, other): return not self.__eq__(other)

def EuclideanDistance(p1: Point2D, p2: Point2D):
    return mt.Newton_Raphson_root(p1.x * p2.x + p1.y * p2.y, 2)[0]
def EuclideanDistance(p1: Point3D, p2: Point3D):
    return mt.Newton_Raphson_root(p1.x * p2.x + p1.y * p2.y + p1.z * p2.z, 2)[0]

def middlePoint(p1: Point2D, p2: Point2D):
    return Point2D((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)
def middlePoint(p1: Point3D, p2: Point3D):
    return Point3D((p1.x + p2.x) / 2, (p1.y + p2.y) / 2, (p1.z + p2.z) / 2)
