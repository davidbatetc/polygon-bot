import math
import random
from PIL import Image, ImageDraw


# Zips xs and ys with ys starting by the `shift`-th element
def shiftZip(xs, ys, shift):
    return zip(xs, ys[shift:] + ys[0:shift])


def sign(x, tol=1e-9):
    if eq(x, 0):
        return 0
    elif lt(x, 0):
        return -1
    else:
        return 1


def cycle(xs):
    n = len(xs)
    while True:
        for i in range(0, n):
            yield xs[i]


def minWithComp(xs, comp=lambda x, y: x < y):
    if not xs:
        return None

    theMin = xs[0]
    n = len(xs)
    for i in range(1, n):
        if comp(xs[i], theMin):
            theMin = xs[i]
    return theMin


def lt(x, y, tol):
    return x - y < -tol


def gt(x, y, tol):
    return x - y > tol


def eq(x, y, tol):
    return abs(x - y) <= tol


def le(x, y, tol):
    return x - y < tol


def ge(x, y, tol):
    return x - y > -tol


class Point:
    # Constructor of the class
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # This is the method that the function `print()` uses
    def __repr__(self):
        return '({:.2f}, {:.2f})'.format(self.x, self.y)

    def __sub__(self, q):
        return Vector(self.x - q.x, self.y - q.y)

    def toTuple(self):
        return self.x, self.y

    @staticmethod
    def distance(p, q):
        return (q - p).norm()

    # `val` is the third coordinate of the vector w = v1 x v2,
    #  where v1 = p2 - p1 and v2 = p3 - p1. This coordinate gives us the
    #  orientation of the basis {v1, v2}:
    #  1. If this coordinate is positive, {v1, v2} is positive-oriented
    #  2. If this coordinate is negative, {v1, v2} is negative-oriented
    #  3. If this coordinate is 0, {v1, v2} is actually not a basis
    #
    # As a consequence, this also gives the orientation of the triangle given by
    #  p1 --> p2 --> p3 --> p1.
    #  1. If `orientationValue` is positive, the triangle is counter-clockwise oriented.
    #  2. If `orientationValue` is negative, the triangle is clockwise oriented.
    #  3. If `orientationValue` is zero, the triangle is degenerate.
    @staticmethod
    def orientation(p1, p2, p3, tol=1e-9):
        cross = Vector.crossProductZ(p2 - p1, p3 - p1)
        if eq(cross, 0, tol):
            return Orien.degen
        if lt(cross, 0, tol):
            return Orien.cw
        if gt(cross, 0, tol):
            return Orien.ccw

    @staticmethod
    def random(xdom=(0, 1), ydom=(0, 1)):
        return Point(xdom[0] + random.random()*(xdom[1] - xdom[0]),
                     ydom[0] + random.random()*(ydom[1] - ydom[0]))


class Vector:
    def __init__(self, x, y):
        if isinstance(x, Point) and isinstance(y, Point):
            self.x = y.x - x.x
            self.y = y.y - x.y
        else:
            self.x = x
            self.y = y

    def __repr__(self):
        return '({:.2f}, {:.2f})'.format(self.x, self.y)

    def norm(self):
        return math.sqrt(self.x**2 + self.y**2)

    @staticmethod
    def dotProduct(u, v):
        return u.x*v.x + u.y*v.y

    @staticmethod
    def crossProductZ(u, v):
        return u.x*v.y - u.y*v.x

    # Note that this will return the smaller angle in radians. The other angle
    #  can be obtained with `math.pi - computeAngle(u, v)`.
    @staticmethod
    def computeAngle(u, v):
        return math.acos(Vector.dotProduct(u, v)/(u.norm()*v.norm()))


# Orientation class defined as a sort of enum for better readibility
class Orien:
    ccw = 1    # Counter-clockwise
    degen = 0  # Degenerate
    cw = -1    # Clockwise


class Edge:
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __repr__(self):
        return '{:} --> {:}'.format(self.p, self.q)

    def getLength(self):
        return Point.distance(self.p, self.q)

    def isInHalfPlane(self, r, tol=1e-9):
        u = self.q - self.p
        v = r - self.p
        return gt(Vector.crossProductZ(u, v), 0, tol)

    @staticmethod
    def computeAngle(e1, e2):
        return Vector.computeAngle(e1.q - e1.p, e2.q - e2.p)

    # Returns whether two edges intersect
    @staticmethod
    def hasIntersection(e1, e2, tol=1e-9):
        ori1p = Point.orientation(e1.p, e1.q, e2.p, tol)
        ori1q = Point.orientation(e1.p, e1.q, e2.q, tol)
        ori2p = Point.orientation(e2.p, e2.q, e1.p, tol)
        ori2q = Point.orientation(e2.p, e2.q, e1.q, tol)

        # Degenerate case
        if ori1p == Orien.degen and ori1q == Orien.degen \
                and ori2p == Orien.degen and ori2q == Orien.degen:
            return not (sign(e1.p.x - e2.p.x) == sign(e1.p.x - e2.q.x)
                        == sign(e1.q.x - e2.p.x) == sign(e1.q.x - e2.q.x)) \
                and not (sign(e1.p.y - e2.p.y) == sign(e1.p.y - e2.q.y)
                         == sign(e1.q.y - e2.p.y) == sign(e1.q.y - e2.q.y))

        # General case
        else:
            return ori1p != ori1q and ori2p != ori2q

    # Fix corner cases
    @staticmethod
    def intersect(e1, e2, tol=1e-9):
        if not Edge.hasIntersection(e1, e2, tol):
            return None

        den = (e1.p.x - e1.q.x)*(e2.p.y - e2.q.y) - (e1.p.y - e1.q.y)*(e2.p.x - e2.q.x)
        a = e1.p.x*e1.q.y - e1.p.y*e1.q.x
        b = e2.p.x*e2.q.y - e2.p.y*e2.q.x
        px = (a*(e2.p.x - e2.q.x) - (e1.p.x - e1.q.x)*b)/den
        py = (a*(e2.p.y - e2.q.y) - (e1.p.y - e1.q.y)*b)/den

        return Point(px, py)


class Color:
    def __init__(self, r=0, g=0, b=0):
        self.r = r
        self.g = g
        self.b = b

    def toIntegerTuple(self):
        return math.floor(255*self.r), math.floor(255*self.g), math.floor(255*self.b)


class ConvexPolygon:
    # Constructor of the class
    def __init__(self, points=[], color=Color()):
        self.points = points
        self.color = color

    # This is the method that the function `print()` uses
    def __repr__(self):
        return self.points.__repr__()

    def getNumberOfVertices(self):
        return len(self.points)

    def toTupleList(self):
        return [p.toTuple() for p in self.points]

    def isTrivial(self):
        n = self.getNumberOfVertices()
        return n == 0 or n == 1

    # Checks if the given point is inside the polygon
    # TO-DO: Make it O(log n)
    def isInside(self, p, tol=1e-9):
        for (q1, q2) in shiftZip(self.points, self.points, 1):
            ori = Point.orientation(p, q1, q2, tol)
            if ori == Orien.degen:
                return True
            elif ori == Orien.cw:
                return False

        return True

    def getEdges(self):
        if self.isTrivial():
            return []
        return [Edge(p, q) for (p, q) in shiftZip(self.points, self.points, 1)]

    def getPerimeter(self):
        return sum([e.getLength() for e in self.getEdges()])

    def isRegular(self, tol=1e-9):
        n = self.getNumberOfVertices()
        if self.isTrivial() or n == 2:
            return True

        edges = self.getEdges()
        expectedAngle = 2*math.pi/n
        expectedLength = edges[0].getLength()  # Arbitrary

        def diffAngle(e1, e2): return abs(expectedAngle - Edge.computeAngle(e1, e2))
        def diffLength(e): return abs(expectedLength - e.getLength())

        return all((eq(diffAngle(e1, e2), 0, tol) and eq(diffLength(e1), 0, tol)
                    for (e1, e2) in shiftZip(edges, edges, 1)))

    def getArea(self):
        xs = [p.x for p in self.points]
        ys = [q.y - p.y for (p, q) in shiftZip(self.points, self.points, 2)]
        return sum([x*y for (x, y) in shiftZip(xs, ys, -1)])/2

    def getCentroid(self):
        n = self.getNumberOfVertices()
        return (sum([p.x for p in self.points])/n, sum([p.y for p in self.points])/n)

    def getBoundingBox(self, color=Color(), tol=1e-9):
        if self.isTrivial():
            return ConvexPolygon([], color=color)
        if self.getNumberOfVertices() == 2:
            # Defined for readibility
            x0, y0 = self.points[0].x, self.points[0].y
            x1, y1 = self.points[1].x, self.points[1].y
            if eq(x0 - x1, 0, tol) or eq(y0 - y1, 0, tol):
                return ConvexPolygon([], color=color)

        top = -math.inf
        bottom = math.inf
        left = math.inf
        right = -math.inf
        for p in self.points:
            top = max(top, p.y)
            bottom = min(bottom, p.y)
            left = min(left, p.x)
            right = max(right, p.x)

        return ConvexPolygon([Point(left, bottom), Point(right, bottom),
                              Point(right, top), Point(left, top)], color=color)

    @staticmethod
    def convexHull(points, color=Color(), tol=1e-9):
        if not points:
            return ConvexPolygon([], color=color)

        def initialComp(p, q):
            return lt(p.x, q.x, tol) or (eq(p.x, q.x, tol) and lt(p.y, q.y, tol))

        p0 = minWithComp(points, comp=initialComp)

        def swipeAngle(p):
            return (p.y - p0.y)/(p - p0).norm()

        spoints = [p for p in points if (p - p0).norm() > tol]
        spoints.sort(key=swipeAngle)

        n = len(spoints)
        stack = []
        iter = 0
        while iter < n:
            d = Point.distance(p0, spoints[iter])
            s = swipeAngle(spoints[iter])
            p = spoints[iter]

            # Of the points aligned with p0, chooses only the furthest ones
            while iter < n - 1 and eq(swipeAngle(spoints[iter + 1]), s, tol):
                newd = Point.distance(spoints[iter + 1], p0)
                if gt(newd, d, tol):
                    d = newd
                    p = spoints[iter + 1]
                iter = iter + 1

            while len(stack) >= 2 and Point.orientation(stack[-1], stack[-2], p) != Orien.cw:
                stack.pop()

            stack.append(p)
            iter = iter + 1

        return ConvexPolygon(points=[p0] + stack, color=color)

    @staticmethod
    def convexUnion(poly1, poly2, color=Color(), tol=1e-9):
        return ConvexPolygon.convexHull(poly1.points + poly2.points, color=color, tol=tol)

    @staticmethod
    def random(n, xdom=(0, 1), ydom=(0, 1), color=Color(), tol=1e-9):
        points = [Point.random(xdom=xdom, ydom=ydom) for _ in range(0, n)]
        return ConvexPolygon.convexHull(points, color=color, tol=tol)

    # Fix list order. Most rightern point should be the first
    @staticmethod
    def genRegularPolygon(n=0, r=1, c=Point(0, 0), phase=0, color=Color()):
        if n == 0:
            return ConvexPolygon([], color=color)
        if n == 1:
            return ConvexPolygon([c], color=color)
        return ConvexPolygon([Point(c.x + r*math.cos(2*math.pi*k/n + phase),
                                    c.y + r*math.sin(2*math.pi*k/n + phase)) for k in range(0, n)], color=color)

    @staticmethod
    def boundaries(polys):
        if not polys:
            return None

        left = math.inf
        bottom = math.inf
        right = -math.inf
        top = -math.inf
        for poly in polys:
            for p in poly.points:
                top = max(top, p.y)
                bottom = min(bottom, p.y)
                left = min(left, p.x)
                right = max(right, p.x)

        return left, bottom, right, top

    # Precondition: the vertices are ordered counter-clockwise
    @staticmethod
    def intersect(poly1, poly2, tol=1e-9):
        n1 = poly1.getNumberOfVertices()
        n2 = poly2.getNumberOfVertices()
        if n1 == 0 or n2 == 0:
            return None

        # Tbp
        if n1 <= 2 or n2 <= 2:
            return None

        gen1 = cycle(poly1.points)
        gen2 = cycle(poly2.points)
        e1 = Edge(next(gen1), next(gen1))
        e2 = Edge(next(gen2), next(gen2))
        inter = []
        inside = None
        iter = 0
        while iter <= 2*(n1 + n2):
            p = Edge.intersect(e1, e2)
            if p != None:
                if inter and (inter[0] - p).norm() <= tol:
                    break
                else:
                    inter.append(p)
                    if e2.isInHalfPlane(e1.q):
                        inside = 'poly1'
                    else:
                        inside = 'poly2'

            v1 = Vector(e1.p, e1.q)
            v2 = Vector(e2.p, e2.q)
            cross = Vector.crossProductZ(v1, v2)
            if ge(cross, 0, tol):  # Aka > 0
                if e1.isInHalfPlane(e2.q):
                    e1 = Edge(e1.q, next(gen1))
                else:
                    e2 = Edge(e2.q, next(gen2))
            elif le(cross, 0, tol):
                if e2.isInHalfPlane(e1.q):
                    e2 = Edge(e2.q, next(gen2))
                else:
                    e1 = Edge(e1.q, next(gen1))
            else:
                print('Oh no, we have found collinearity!')

            iter = iter + 1

        return inter

    @staticmethod
    def draw(polys=[], fileName='output.png', sideLength=400, margin=1, bg=Color(1, 1, 1), show=False):
        img = Image.new('RGB', (sideLength, sideLength), bg.toIntegerTuple())
        dib = ImageDraw.Draw(img)

        if not polys:
            if show:
                img.show()
            img.save(fileName)
            return

        left, bottom, right, top = ConvexPolygon.boundaries(polys)
        xspan = right - left
        yspan = top - bottom
        if xspan < yspan:
            x0 = left - (yspan - xspan)/2
            y0 = bottom
            factor = (sideLength - 2*margin)/yspan
        else:
            x0 = left
            y0 = bottom - (xspan - yspan)/2
            factor = (sideLength - 2*margin)/xspan

        def fitToCanvas(tupleList):
            return [((x - x0)*factor + margin, sideLength - (y - y0)*factor - margin) for (x, y) in tupleList]

        for poly in polys:
            dib.polygon(fitToCanvas(poly.toTupleList()), outline=poly.color.toIntegerTuple())

        if show:
            img.show()

        img.save(fileName)
