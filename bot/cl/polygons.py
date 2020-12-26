from PIL import Image, ImageDraw
import copy
import random


import math
# Zips xs and ys with ys starting by the `shift`-th element


def shiftZip(xs, ys, shift):
    return zip(xs, ys[shift:] + ys[0:shift])


def sign(x, tol=1e-9):
    if eq(x, 0, tol):
        return 0
    elif lt(x, 0, tol):
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
    for x in xs[1:]:
        if comp(x, theMin):
            theMin = x
    return theMin


def maxWithComp(xs, comp=lambda x, y: x > y):
    return minWithComp(xs, comp=comp)


# Pre: there is only one minimum
def beginWithMin(xs, comp=lambda x, y: x < y):
    if not xs:
        return xs

    theMin = xs[0]
    iMin = 0
    n = len(xs)
    for i in range(1, n):
        if comp(xs[i], theMin):
            theMin = xs[i]
            iMin = i
    return xs[iMin:] + xs[:iMin]


def lt(x, y, tol):
    return x - y < -tol


def gt(x, y, tol):
    return x - y > tol


def eq(x, y, tol):
    return abs(x - y) <= tol


def ne(x, y, tol):
    return abs(x - y) > tol


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

    def __add__(self, u):
        return Point(self.x + u.x, self.y + u.y)

    @staticmethod
    def distance(p, q):
        return (q - p).norm()

    @staticmethod
    def isEqual(p, q, tol=1e-9):
        return eq(Point.distance(p, q), 0, tol)

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
            return Vector.Orien.DEGEN
        if lt(cross, 0, tol):
            return Vector.Orien.CW
        if gt(cross, 0, tol):
            return Vector.Orien.CCW

    @staticmethod
    def random(xdom=(0, 1), ydom=(0, 1)):
        return Point(xdom[0] + random.random()*(xdom[1] - xdom[0]),
                     ydom[0] + random.random()*(ydom[1] - ydom[0]))


class Vector:
    # Orientation class defined as a sort of enum for better readibility
    class Orien:
        CCW = 1    # Counter-clockwise
        DEGEN = 0  # Degenerate
        CW = -1    # Clockwise

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


class Edge:
    class Inter:
        CROSS = 1
        DEGEN = 0
        NONE = -1

    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __repr__(self):
        return '{:} --> {:}'.format(self.p, self.q)

    def getLength(self):
        return Point.distance(self.p, self.q)

    def isInLeftHalfPlane(self, r, tol=1e-9):
        u = self.q - self.p
        v = r - self.p
        return ge(Vector.crossProductZ(u, v), 0, tol)

    def isPointInside(self, p, tol=1e-9):
        return eq(Point.distance(self.p, p) + Point.distance(p, self.q), self.getLength(), tol)

    @staticmethod
    def computeAngle(e1, e2):
        return Vector.computeAngle(e1.q - e1.p, e2.q - e2.p)

    @staticmethod
    def isEqual(e1, e2, tol=1e-9):
        return (Point.isEqual(e1.p, e2.p, tol) and Point.isEqual(e1.q, e2.q, tol)) \
            or (Point.isEqual(e1.p, e2.q, tol) and Point.isEqual(e1.q, e2.p, tol))

    # Returns whether two edges intersect
    @staticmethod
    def hasIntersection(e1, e2, tol=1e-9):
        ori1p = Point.orientation(e1.p, e1.q, e2.p, tol)
        ori1q = Point.orientation(e1.p, e1.q, e2.q, tol)
        ori2p = Point.orientation(e2.p, e2.q, e1.p, tol)
        ori2q = Point.orientation(e2.p, e2.q, e1.q, tol)

        # Degenerate case
        if ori1p == Vector.Orien.DEGEN and ori1q == Vector.Orien.DEGEN \
                and ori2p == Vector.Orien.DEGEN and ori2q == Vector.Orien.DEGEN:
            if (ori1p == 0 and e1.isPointInside(e2.p)) or (ori1q == 0 and e1.isPointInside(e2.q)) \
                    or (ori2p == 0 and e2.isPointInside(e1.p)) or (ori2q == 0 and e2.isPointInside(e1.q)):
                return Edge.Inter.DEGEN
            else:
                return Edge.Inter.NONE

        # General case
        else:
            if ori1p != ori1q and ori2p != ori2q:
                return Edge.Inter.CROSS
            else:
                return Edge.Inter.NONE

    @staticmethod
    def intersect(e1, e2, tol=1e-9):
        interType = Edge.hasIntersection(e1, e2, tol)
        if interType == Edge.Inter.NONE:
            return Edge.Inter.NONE, []

        if interType == Edge.Inter.DEGEN:
            def comp(p, q):
                return lt(p.x, q.x, tol) or (eq(p.x, q.x, tol) and lt(p.y, q.y, tol))

            ce1 = copy.deepcopy(e1)
            ce2 = copy.deepcopy(e2)

            # Changing so that the points in ce1 and ce2 are sorted and ce1 is
            #  the edge with a smaller p
            if comp(ce1.q, ce1.p):
                ce1.p, ce1.q = ce1.q, ce1.p
            if comp(ce2.q, ce2.p):
                ce2.p, ce2.q = ce2.q, ce2.p
            if comp(ce2.p, ce1.p):
                ce1, ce2 = ce2, ce1

            if comp(ce1.q, ce2.p):
                return Edge.Inter.DEGEN, []
            elif Point.isEqual(ce1.q, ce2.p, tol):
                return Edge.Inter.DEGEN, [ce1.q]
            else:
                if comp(ce1.q, ce2.q):
                    return Edge.Inter.DEGEN, [ce2.p, ce1.q]
                else:
                    return Edge.Inter.DEGEN, [ce2.p, ce2.q]

        if interType == Edge.Inter.CROSS:
            den = (e1.p.x - e1.q.x)*(e2.p.y - e2.q.y) - (e1.p.y - e1.q.y)*(e2.p.x - e2.q.x)
            a = e1.p.x*e1.q.y - e1.p.y*e1.q.x
            b = e2.p.x*e2.q.y - e2.p.y*e2.q.x
            px = (a*(e2.p.x - e2.q.x) - (e1.p.x - e1.q.x)*b)/den
            py = (a*(e2.p.y - e2.q.y) - (e1.p.y - e1.q.y)*b)/den
            return Edge.Inter.CROSS, [Point(px, py)]


class Color:
    def __init__(self, r=0, g=0, b=0):
        self.r = r
        self.g = g
        self.b = b

    def __repr__(self):
        return '{{{:.3f} {:.3f} {:.3f}}}'.format(self.r, self.g, self.b)

    def toIntegerTuple(self):
        return math.floor(255*self.r), math.floor(255*self.g), math.floor(255*self.b)


class ConvexPolygon:
    # Constructor of the class
    def __init__(self, points=[], color=Color(), sortedList=False, tol=1e-9):
        self.color = color
        if sortedList or not points:
            self.points = points
            return

        def initialComp(p, q):
            return lt(p.x, q.x, tol) or (eq(p.x, q.x, tol) and lt(p.y, q.y, tol))

        p0 = minWithComp(points, comp=initialComp)

        def swipeAngle(p):
            return (p.y - p0.y)/(p - p0).norm()

        spoints = [p for p in points if not Point.isEqual(p, p0, tol)]
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

            while len(stack) >= 2 and Point.orientation(stack[-1], stack[-2], p) != Vector.Orien.CW:
                stack.pop()

            stack.append(p)
            iter = iter + 1

        self.points = [p0] + stack

    # This is the method that the function `print()` uses
    def __repr__(self):
        return self.points.__repr__()

    def getNumberOfVertices(self):
        return len(self.points)

    # O(log n)
    def isPointInside(self, p, tol=1e-9):
        n = self.getNumberOfVertices()
        if n == 0:
            return False
        if n == 1:
            return Point.isEqual(self.points[0], p, tol)
        if n == 2:
            return Edge(self.points[0], self.points[1]).isPointInside(p, tol)

        def isInsideTriangle(q1, q2, q3):
            ori1 = Point.orientation(p, q1, q2)
            ori2 = Point.orientation(p, q2, q3)
            ori3 = Point.orientation(p, q3, q1)
            return (ori1 == Vector.Orien.CCW and ori2 == Vector.Orien.CCW and ori3 == Vector.Orien.CCW) or \
                (ori1 == Vector.Orien.DEGEN and Edge(q1, q2).isPointInside(p)) or \
                (ori2 == Vector.Orien.DEGEN and Edge(q2, q3).isPointInside(p)) or \
                (ori3 == Vector.Orien.DEGEN and Edge(q3, q1).isPointInside(p))

        q0 = self.points[0]

        def binarySlicing(li, ri):
            if ri - li == 1:
                return isInsideTriangle(self.points[0], self.points[li], self.points[ri])

            mi = (li + ri)//2
            qm = self.points[mi]
            ori = Point.orientation(p, q0, qm)
            if ori == Vector.Orien.DEGEN:
                return Edge(q0, qm).isPointInside(p)
            elif ori == Vector.Orien.CW:
                return binarySlicing(li, mi)
            else:
                return binarySlicing(mi, ri)

        return binarySlicing(1, n - 1)

    # O(n + m)
    def isPolygonInside(self, poly, tol=1e-9):
        inter = ConvexPolygon.intersect(self, poly)
        return ConvexPolygon.isEqual(inter, poly)

    def getEdges(self):
        n = self.getNumberOfVertices()
        if n <= 1:
            return []
        if n == 2:
            return [Edge(self.points[0], self.points[1])]
        return [Edge(p, q) for (p, q) in shiftZip(self.points, self.points, 1)]

    def getPerimeter(self):
        return sum([e.getLength() for e in self.getEdges()])

    def isRegular(self, tol=1e-9):
        if self.getNumberOfVertices() <= 2:
            return True

        edges = self.getEdges()
        expectedAngle = 2*math.pi/n
        expectedLength = edges[0].getLength()  # Arbitrary

        return all(eq(Edge.computeAngle(e1, e2), expectedAngle, tol) and
                   eq(e1.getLength(), expectedLength, tol)
                   for (e1, e2) in shiftZip(edges, edges, 1))

    def getArea(self):
        if self.getNumberOfVertices() <= 2:
            return 0

        xs = [p.x for p in self.points]
        ys = [q.y - p.y for (p, q) in shiftZip(self.points, self.points, 2)]
        return sum([x*y for (x, y) in shiftZip(xs, ys, -1)])/2

    def getCentroid(self):
        n = self.getNumberOfVertices()
        return Point(sum([p.x for p in self.points])/n, sum([p.y for p in self.points])/n)

    def getBoundingBox(self, color=Color(), tol=1e-9):
        n = self.getNumberOfVertices()
        if n <= 1:
            return ConvexPolygon([], color=color, sortedList=True)
        if n == 2:
            # Defined for readibility
            x0, y0 = self.points[0].x, self.points[0].y
            x1, y1 = self.points[1].x, self.points[1].y
            if eq(x0, x1, tol) or eq(y0, y1, tol):
                return ConvexPolygon([], color=color, sortedList=True)

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
                              Point(right, top), Point(left, top)], color=color, sortedList=True)

    def translate(self, u):
        self.points = [p + u for p in self.points]

    @staticmethod
    def convexUnion(poly1, poly2, color=Color(), tol=1e-9):
        return ConvexPolygon(poly1.points + poly2.points, color=color, tol=tol)

    @staticmethod
    def isEqual(poly1, poly2, tol=1e-9):
        if poly1.getNumberOfVertices() != poly2.getNumberOfVertices():
            return False

        for (p, q) in zip(poly1.points, poly2.points):
            if not Point.isEqual(p, q, tol):
                return False

        return True

    @staticmethod
    def random(n, xdom=(0, 1), ydom=(0, 1), color=Color(), tol=1e-9):
        points = [Point.random(xdom=xdom, ydom=ydom) for _ in range(0, n)]
        return ConvexPolygon(points, color=color, tol=tol)

    @staticmethod
    def genRegularPolygon(n=0, r=1, c=Point(0, 0), phase=0, color=Color()):
        if n == 0:
            return ConvexPolygon([], color=color, sortedList=True)
        if n == 1:
            return ConvexPolygon([copy.deepcopy(c)], color=color, sortedList=True)

        idealShift = (math.pi - phase)*n/(2*math.pi)
        ceilShift = math.ceil(idealShift)
        if ceilShift - idealShift <= 0.5:
            shift = ceilShift
        else:
            shift = math.floor(idealShift)

        return ConvexPolygon([Point(c.x + r*math.cos(2*math.pi*k/n + phase),
                                    c.y + r*math.sin(2*math.pi*k/n + phase)) for k in range(shift, n + shift)],
                             color=color, sortedList=True)

    @staticmethod
    def boundaries(polys):
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

    # O(n + m)
    @staticmethod
    def intersect(poly1, poly2, color=Color(), tol=1e-9):
        emptyPoly = ConvexPolygon([], color=color, sortedList=True)

        def trivialCases(spoly1, spoly2, sn1, sn2):
            if sn1 == 0:
                return emptyPoly
            if sn1 == 1:
                if spoly2.isPointInside(spoly1.points[0]):
                    spoly1Copy = copy.deepcopy(spoly1)
                    spoly1Copy.color = color
                    return spoly1Copy
                else:
                    return emptyPoly
            if sn1 == 2:
                e1 = Edge(spoly1.points[0], spoly1.points[1])
                e2 = Edge(spoly2.points[0], spoly2.points[1])
                interType, ps = Edge.intersect(e1, e2)
                if interType == Edge.Inter.NONE:
                    return emptyPoly
                else:
                    return ConvexPolygon(copy.deepcopy(ps),
                                         color=color, sortedList=True)

        n1 = poly1.getNumberOfVertices()
        n2 = poly2.getNumberOfVertices()

        if (n1 == 2 and n2 >= 3):
            e1 = Edge(poly1.points[0], poly1.points[1])
            for e2 in poly2.getEdges():
                interType, ps = Edge.intersect(e1, e2)
                if interType == Edge.Inter.DEGEN:
                    return ConvexPolygon(ps, color=color, sortedList=True)
        elif (n1 >= 3 and n2 == 2):
            e2 = Edge(poly2.points[0], poly2.points[1])
            for e1 in poly1.getEdges():
                interType, ps = Edge.intersect(e1, e2)
                if interType == Edge.Inter.DEGEN:
                    return ConvexPolygon(ps, color=color, sortedList=True)
        elif (n1 <= 2 or n2 <= 2):
            if n1 <= n2:
                return trivialCases(poly1, poly2, n1, n2)
            else:
                return trivialCases(poly2, poly1, n2, n1)

        class Place:
            inPoly1 = -1
            unknown = 0
            inPoly2 = 1

        def comp(p, q):
            return lt(p.x, q.x, tol) or (eq(p.x, q.x, tol) and lt(p.y, q.y, tol))

        gen1 = cycle(poly1.points)
        gen2 = cycle(poly2.points)
        e1 = Edge(next(gen1), next(gen1))
        e2 = Edge(next(gen2), next(gen2))
        inter = []
        firstInterIter = -math.inf
        place = Place.unknown

        iter = 0
        while iter < 2*(n1 + n2):
            interType, currInter = Edge.intersect(e1, e2)
            if interType == Edge.Inter.CROSS:
                p = currInter[0]
                if len(inter) >= 2 and Edge(inter[-2], inter[-1]).isPointInside(p):
                    inter.pop()
                if firstInterIter + 1 != iter and inter and Point.isEqual(inter[0], p, tol):
                    return ConvexPolygon(beginWithMin(inter, comp), color=color, sortedList=True)
                else:
                    if not inter:
                        firstInterIter = iter
                    if not inter or (inter and not Point.isEqual(inter[0], p, tol)
                                     and not Point.isEqual(inter[-1], p, tol)):
                        inter.append(p)
                    if e2.isInLeftHalfPlane(e1.q):
                        place = Place.inPoly1
                    else:
                        place = Place.inPoly2

            if place == Place.inPoly1 and not Point.isEqual(inter[-1], e1.q, tol):
                inter.append(e1.q)
            elif place == Place.inPoly2 and not Point.isEqual(inter[-1], e2.q, tol):
                inter.append(e2.q)

            v1 = Vector(e1.p, e1.q)
            v2 = Vector(e2.p, e2.q)
            if ge(Vector.crossProductZ(v2, v1), 0, tol):
                if e2.isInLeftHalfPlane(e1.q):
                    e2 = Edge(e2.q, next(gen2))
                else:
                    e1 = Edge(e1.q, next(gen1))
            else:
                if e1.isInLeftHalfPlane(e2.q):
                    e1 = Edge(e1.q, next(gen1))
                else:
                    e2 = Edge(e2.q, next(gen2))

            iter = iter + 1

        if inter:
            return ConvexPolygon(beginWithMin(inter, comp), color=color, sortedList=True)

        p1 = poly1.points[0]
        p2 = poly2.points[0]
        if poly2.isPointInside(p1):
            spoly1Copy = copy.deepcopy(poly1)
            spoly1Copy.color = color
            return spoly1Copy
        if poly1.isPointInside(p2):
            spoly2Copy = copy.deepcopy(poly2)
            spoly2Copy.color = color
            return spoly2Copy
        return emptyPoly

    @staticmethod
    def draw(polys=[], fileName='output.png', sideLength=400, margin=1, bg=Color(1, 1, 1), show=False, tol=1e-9):
        img = Image.new('RGB', (sideLength, sideLength), bg.toIntegerTuple())
        dib = ImageDraw.Draw(img)

        if not polys:
            if show:
                img.show()
            img.save(fileName)
            return

        left, bottom, right, top = ConvexPolygon.boundaries(polys)

        if eq(left, right, tol) and eq(bottom, top, tol):
            def fitToCanvas(poly):
                return [(sideLength/2, sideLength/2) for p in poly.points]
        else:
            xspan = right - left
            yspan = top - bottom

            if xspan <= yspan:
                x0 = left - (yspan - xspan)/2
                y0 = bottom
                factor = (sideLength - 1 - 2*margin)/yspan
            else:
                x0 = left
                y0 = bottom - (xspan - yspan)/2
                factor = (sideLength - 1 - 2*margin)/xspan

            def fitToCanvas(poly):
                return [(round((p.x - x0)*factor + margin),
                         round(sideLength - 1 - (p.y - y0)*factor - margin)) for p in poly.points]

        for poly in polys:
            n = poly.getNumberOfVertices()
            if n == 1:
                dib.point(fitToCanvas(poly), fill=poly.color.toIntegerTuple())
            elif n >= 2:
                dib.polygon(fitToCanvas(poly), outline=poly.color.toIntegerTuple())

        if show:
            img.show()

        img.save(fileName)
