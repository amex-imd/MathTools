import mathtools as mt

class Point2D:
    def __init__(self, x: float, y: float):
        self.x, self.y = x, y
    def __str__(self): return f'<{self.x}, {self.y}>'
    
class Point3D(Point2D):
    def __init__(self, x: float, y: float, z: float):
        Point2D.__init__(self, x, y)
        self.z = z
    def __str__(self): return f'<{self.x:.2f}, {self.y:.2f}, {self.z:.2f}>'

def EuclideanDistance(p1: Point2D, p2: Point2D):
    return mt.Newton_Raphson_root(p1.x * p2.x + p1.y * p2.y, 2)[0]
def EuclideanDistance(p1: Point3D, p2: Point3D):
    return mt.Newton_Raphson_root(p1.x * p2.x + p1.y * p2.y + p1.z * p2.z, 2)[0]

def middlePoint(p1: Point2D, p2: Point2D):
    return Point2D((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)
def middlePoint(p1: Point3D, p2: Point3D):
    return Point3D((p1.x + p2.x) / 2, (p1.y + p2.y) / 2, (p1.z + p2.z) / 2)
