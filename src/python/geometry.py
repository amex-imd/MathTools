

class Point2D:
    def __init__(self, x: float, y: float):
        self.x, self.y = x, y
    def __str__(self): return f'<{self.x}, {self.y}>'
    
class Point3D(Point2D):
    def __init__(self, x: float, y: float, z: float):
        Point2D.__init__(self, x, y)
        self.z = z
    def __str__(self): return f'<{self.x:.2f}, {self.y:.2f}, {self.z:.2f}>'

