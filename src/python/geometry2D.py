import mathtools as mt
from typing import Tuple, List, Optional
from abc import ABC, abstractmethod
from math import sin, cos # TODO


class geometricObject2D(ABC):
    @abstractmethod
    def move(self, dx: float, dy: float) -> None: pass

    @abstractmethod
    def rotate(self, angle: float, center: 'point2D' = None) -> None: pass

    @abstractmethod
    def scale(elf, factor: float, center: 'point2D' = None) -> None: pass

    @property
    def dimenshion(self) -> int: return 2

class geometricFigure2D(geometricObject2D):
    @abstractmethod
    def area(self) -> float: pass
    @abstractmethod
    def perimeter(self) -> float: pass

class point2D(geometricObject2D):
    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y

    def move(self, dx: float, dy: float) -> None:
        self.x += dx
        self.y += dy

    def rotate(self, angle: float, center: 'point2D' = None) -> None:
        if center is None:
            cx, cy = 0, 0
        else:
            cx, cy = center.x, center.y
        
        x: float = self.x - cx
        y: float = self.y - cy

        tmp1: float = cos(angle)
        tmp2: float = sin(angle)

        self.x = x * tmp1 - y * tmp2 + cx
        self.y = x * tmp2 + y * tmp1 + cy        

    def scale(self, factor: float, center: 'point2D' = None) -> None:
        if factor <= 0: raise ValueError('The argument \'factor\' must be greater than 0')

        if center is None:
            cx, cy = 0, 0
        else:
            cx, cy = center.x, center.y

        self.x = cx + (self.x - cx) * factor
        self.y = cy + (self.y - cy) * factor

    def __str__(self) -> str: return f'Point2D({self.x}, {self.y})'

    def __eq__(self, other) -> bool:
        if not isinstance(other, point2D): return False
        return other.x == self.x and other.y == self.y
    def __ne__(self, other): return not self.__eq__(other)

class circle(geometricFigure2D):
    def __init__(self, center: point2D, radius: float) -> None:
        self.center: point2D = center
        self._radius: float = radius

    def move(self, dx: float, dy: float) -> None:
        self.center.move(dx, dy)

    def rotate(self, angle: float, center: 'point2D' = None) -> None:
        self.center.rotate(angle, center)      

    def scale(self, factor: float, center: 'point2D' = None) -> None:
        self.center.scale(factor, center)
        self._radius *= factor

    @property
    def radius(self) -> float:
        return self._radius
    
    @radius.setter
    def radius(self, radius: float) -> None:
        if radius <= 0: raise ValueError('The argument \'radius\' must be greater than 0')
        self._radius = radius

    def __str__(self) -> str: return f"Circle(Center={self.center}; Radius={self._radius})"

    def area(self) -> float: return mt.PI * self._radius * self._radius

    def perimeter(self) -> float: return 2 * mt.PI * self._radius

class ellipse(geometricFigure2D):
    def __init__(self, center: point2D, a: float, b: float) -> None:
        self._a: float = a
        self._b: float = b
        self.center: point2D = center

    def area(self) -> float: return mt.PI * self._a * self._b

    def perimeter(self) -> float: return mt.PI*(3*(self._a + self._b) - mt.NewtonRaphsonRoot((3*self._a + self._b)*(self._a + 3*self._b), 2)[0])

    def eccentricity(self) -> float: return mt.NewtonRaphsonRoot(1 - (self._b * self._b) / (self._a * self._a), 2)[0]

    def focalDistance(self) -> float: return mt.NewtonRaphsonRoot(self._a * self._a - self._b * self._b, 2)[0]

    def directrix(self) -> float: return self._a / self.eccentricity()

    def move(self, dx: float, dy: float) -> None:
        self.center.move(dx, dy)

    def rotate(self, angle: float, center: 'point2D' = None) -> None:
        self.center.rotate(angle, center)      

    def scale(self, factor: float, center: 'point2D' = None) -> None:
        self.center.scale(factor, center)
        self._a *= factor
        self._b *= factor

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

class square(geometricFigure2D):
    def __init__(self, center: point2D, side: float):
        if side < 0: raise ValueError('The argument \'side\' must be greater than or equal to 0')
        self._side = side
        self.center = center

    @property
    def side(self) -> float:
        return self._side
    
    @side.setter
    def side(self, side: float) -> None:
        if side < 0: raise ValueError('The argument \'side\' must be greater than or equal to 0')
        self._side = side

    def __str__(self) -> str: return f"Ellipse(Center={self.center}; Side={self._side})"

    def area(self): return self._side * self._side
    def perimeter(self): return 4 * self._side
    def diagonal(self): return self._side * mt.NewtonRaphsonRoot(2, 2)[0]
    def radius(self) -> Tuple[float, float]: return (self._side / 2, self._a / mt.NewtonRaphsonRoot(2, 2)[0])
    def vertices(self) -> Tuple[Tuple[float, float], Tuple[float, float], Tuple[float, float], Tuple[float, float]]:
        half: float = self._side / 2
        x, y = self.center.x, self.center.y
        return ((x - half, y + half),
                (x + half, y + half),
                (x + half, y - half),
                (x - half, y - half))
    
    def move(self, dx: float, dy: float) -> None:
        self.center.move(dx, dy)

    def rotate(self, angle: float, center: 'point2D' = None) -> None:
        self.center.rotate(angle, center)      

    def scale(self, factor: float, center: 'point2D' = None) -> None:
        self.center.scale(factor, center)
        self._side *= factor
    

def EuclideanDistance(p1: point2D, p2: point2D) -> float:
    return mt.Newton_Raphson_root(p1.x * p2.x + p1.y * p2.y, 2)[0]

def middlePoint(p1: point2D, p2: point2D) -> float:
    return point2D((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)