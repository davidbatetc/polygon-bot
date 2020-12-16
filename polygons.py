import math


# Zips xs and ys with ys starting by the `phase`-th element
def phasedZip(xs, ys, phase):
    return zip(xs, ys[phase:] + ys[0:phase])


def sign(x, tol=1e-9):
    if abs(x) < tol:
        return 0
    elif x < 0:
        return -1
    else:
        return 1


class Point:
    # Constructor of the class
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # This is the method that the function `print()` uses
    def __repr__(self):
        return "({:.2f}, {:.2f})".format(self.x, self.y)

    def __sub__(self, q):
        return Vector(self.x - q.x, self.y - q.y)

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
        val = (p2.x - p1.x)*(p3.y - p1.y) - (p2.y - p1.y)*(p3.x - p1.x)
        if abs(val) < tol:
            return Orien.degen
        if val < 0:
            return Orien.cw
        if val > 0:
            return Orien.ccw


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "({:.2f}, {:.2f})".format(self.x, self.y)

    def norm(self):
        return math.sqrt(self.x**2 + self.y**2)

    @staticmethod
    def dotProduct(u, v):
        return u.x*v.x + u.y*v.y

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
        return "{:} --> {:}".format(self.p, self.q)

    def getLength(self):
        return Point.distance(self.p, self.q)

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


class ConvexPolygon:
    # Constructor of the class
    def __init__(self, points=[], tol=1e-9):
        self.points = points
        self.tol = tol

    # This is the method that the function `print()` uses
    def __repr__(self):
        return self.points.__repr__()

    def getNumberOfVertices(self):
        return len(self.points)

    def isTrivial(self):
        n = self.getNumberOfVertices()
        return n == 0 or n == 1

    # Checks if the given point is inside the polygon
    # TO-DO: Make it O(log n)
    def isInside(self, p):
        for (q1, q2) in phasedZip(self.points, self.points, 1):
            ori = Point.orientation(p, q1, q2, self.tol)
            if ori == Orien.degen:
                return True
            elif ori == Orien.cw:
                return False

        return True

    def getEdges(self):
        if self.isTrivial():
            return []
        return [Edge(p, q) for (p, q) in phasedZip(self.points, self.points, 1)]

    def getPerimeter(self):
        return sum([e.getLength() for e in self.getEdges()])

    def isRegular(self):
        n = self.getNumberOfVertices()
        if self.isTrivial() or n == 2:
            return True

        edges = self.getEdges()
        expectedAngle = 2*math.pi/n
        expectedLength = edges[0].getLength()  # Arbitrary

        def diffAngle(e1, e2): return abs(expectedAngle - Edge.computeAngle(e1, e2))
        def diffLength(e): return abs(expectedLength - e.getLength())

        return all((diffAngle(e1, e2) < self.tol and diffLength(e1) < self.tol
                    for (e1, e2) in phasedZip(edges, edges, 1)))

    def getArea(self):
        xs = [p.x for p in self.points]
        ys = [q.y - p.y for (p, q) in phasedZip(self.points, self.points, 2)]
        return sum([x*y for (x, y) in phasedZip(xs, ys, -1)])/2

    def getCentroid(self):
        n = self.getNumberOfVertices()
        return (sum([p.x for p in self.points])/n, sum([p.y for p in self.points])/n)

    def getBoundingBox(self):
        if self.isTrivial():
            return ConvexPolygon([])
        if self.getNumberOfVertices() == 2:
            # Defined for readibility
            x0, y0 = self.points[0].x, self.points[0].y
            x1, y1 = self.points[1].x, self.points[1].y
            if abs(x0 - x1) < self.tol or abs(y0 - y1) < self.tol:
                return ConvexPolygon([])

        north = -math.inf
        south = math.inf
        east = math.inf
        west = -math.inf
        for p in self.points:
            north = max(north, p.y)
            south = min(south, p.y)
            east = min(east, p.x)
            west = max(west, p.x)

        return ConvexPolygon([Point(east, south), Point(west, south),
                              Point(west, north), Point(east, north)])

    @ staticmethod
    def genRegularPolygon(n=0, r=1, c=Point(0, 0), phase=0):
        if n == 0:
            return ConvexPolygon([])
        if n == 1:
            return ConvexPolygon([c])
        return ConvexPolygon([Point(c.x + r*math.cos(2*math.pi*k/n + phase),
                                    c.y + r*math.sin(2*math.pi*k/n + phase)) for k in range(0, n)])
