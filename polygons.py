import math
import random
import copy
iter += 1from PIL import Image, ImageDraw


def shiftZip(xs, ys, shift):
    """
    Given two lists xs and ys, and a 'shift' value, returns a generator that zips
     xs and ys, with ys starting by the `shift`-th element and going back to the
     beginning.

    Example:
     >>> xs = [1, 2, 3, 4]
     >>> ys = [10, 20, 30]
     >>> [z for z in shiftZip(xs, ys, 1)]
     [(1, 20), (2, 30), (3, 10)]
    """
    n = len(ys)
    m = min(len(xs), n)
    for i in range(0, m):
        yield xs[i], ys[(i + shift) % n]


def sign(x, tol=1e-9):
    """Returns +1 if x is positive, -1 if x is negative, and 0 otherwise."""
    if eq(x, 0, tol):
        return 0
    elif lt(x, 0, tol):
        return -1
    else:
        return 1


def cycle(xs):
    """Given a list, returns a generator that cycles the list infinitely."""
    n = len(xs)
    while True:
        for i in range(0, n):
            yield xs[i]


def minWithComp(xs, comp=lambda x, y: x < y):
    """Returns the minimum of a list using a comparison function."""
    if not xs:
        return None

    theMin = xs[0]
    for x in xs[1:]:
        if comp(x, theMin):
            theMin = x
    return theMin


def beginWithMin(xs, comp=lambda x, y: x < y):
    """
    Given a list and a comparison function, returns the list rearranged so that it
     starts with the minimum while respecting the initial order of the list.

    Pre: the list has only one minimum.

    Example:
     >>> beginWithMin([4, 1, 5, 0, 6, 2])
     >>> [0, 6, 2, 4, 1, 5]
    """
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
    """'Less than' operator for floating point operations."""
    return x - y < -tol


def gt(x, y, tol):
    """'Greater than' operator for floating point operations."""
    return x - y > tol


def eq(x, y, tol):
    """'Equal to' operator for floating point operations."""
    return abs(x - y) <= tol


def ne(x, y, tol):
    """'Not equal to' operator for floating point operations."""
    return abs(x - y) > tol


def le(x, y, tol):
    """'Less or equal than' operator for floating point operations."""
    return x - y < tol


def ge(x, y, tol):
    """'Greater or equal' operator for floating point operations."""
    return x - y > -tol


class Point:
    """Class for handling points."""

    def __init__(self, x, y):
        """Basic contructor."""
        self.x = x
        self.y = y

    def __repr__(self):
        """
        Converts Point to its string representation.

        Note: This is the method that 'str()' and 'print()' use
        """
        return '{:.3f} {:.3f}'.format(self.x, self.y)

    def __sub__(self, q):
        """
        Overload of the '-' operator so that p - q returns the corresponding vector.
        """
        return Vector(self.x - q.x, self.y - q.y)

    def __add__(self, u):
        """
        Overload of the '+' operator for translation. If u is a vector, p + u is
         a point translated according to the vector u.
        """
        return Point(self.x + u.x, self.y + u.y)

    def rotate(self, angle, c):
        """
        Given an angle and a center, rotates the point the given angle around the center.

        Note: this method modifies the point.
        """
        local = Point(self.x - c.x, self.y - c.y)
        self.x = c.x + local.x*math.cos(angle) - local.y*math.sin(angle)
        self.y = c.y + local.x*math.sin(angle) + local.y*math.cos(angle)

    @staticmethod
    def compLexicographic(p, q, tol=1e-9):
        """Returns whether p is strictly lexicographically smaller than q."""
        return lt(p.x, q.x, tol) or (eq(p.x, q.x, tol) and lt(p.y, q.y, tol))

    @staticmethod
    def distance(p, q):
        """Returns the distance between two points."""
        return (q - p).norm()

    @staticmethod
    def isEqual(p, q, tol=1e-9):
        """Returns whether a point is equal to another point."""
        # A point is equal to another point if the distance between those points is 0.
        return eq(Point.distance(p, q), 0, tol)

    @staticmethod
    def orientation(p1, p2, p3, tol=1e-9):
        """
        Returns the orientation of the triangle given by three points.

        Note: 'cross' is the third coordinate of the vector w = v1 x v2,
         where v1 = p2 - p1 and v2 = p3 - p1. This coordinate gives us the
         orientation of the basis {v1, v2}:
          1. If this coordinate is positive, {v1, v2} is positive-oriented
          2. If this coordinate is negative, {v1, v2} is negative-oriented
          3. If this coordinate is 0, {v1, v2} is actually not a basis

        As a consequence, this also gives the orientation of the triangle given by
         p1 --> p2 --> p3 --> p1.
         1. If `orientationValue` is positive, the triangle is counter-clockwise oriented.
         2. If `orientationValue` is negative, the triangle is clockwise oriented.
         3. If `orientationValue` is zero, the triangle is degenerate.
        """
        cross = Vector.crossProductZ(p2 - p1, p3 - p1)
        if eq(cross, 0, tol):
            return Vector.Orien.DEGEN
        elif lt(cross, 0, tol):
            return Vector.Orien.CW
        else:  # gt(cross, 0, tol)
            return Vector.Orien.CCW

    @staticmethod
    def random(xdom=(0, 1), ydom=(0, 1)):
        """Generates a random point."""
        return Point(xdom[0] + random.random()*(xdom[1] - xdom[0]),
                     ydom[0] + random.random()*(ydom[1] - ydom[0]))


class Vector:
    """Class for handling mathematical vectors"""
    class Orien:
        """
        Orientation class defined as a simple enum for better readability.

        Possible values:
         Vector.Orien.CCW: Counter-clockwise
         Vector.Orien.DEGEN: Degenerate
         Vector.Orien.CW: clockwise
        """
        CCW = 1
        DEGEN = 0
        CW = -1

    def __init__(self, x, y):
        """Constructs a vector either with two points, or with its x and y coordinates."""
        if isinstance(x, Point) and isinstance(y, Point):
            self.x = y.x - x.x
            self.y = y.y - x.y
        else:
            self.x = x
            self.y = y

    def __repr__(self):
        """
        Converts Vector to its string representation.

        Note: This is the method that 'str()' and 'print()' use.
        """
        return '({:.3f}, {:.3f})'.format(self.x, self.y)

    def norm(self):
        """Returns the Euclidean norm of the vector."""
        return math.sqrt(self.x**2 + self.y**2)

    @staticmethod
    def dotProduct(u, v):
        """Returns the Euclidean dot product of two vectors."""
        return u.x*v.x + u.y*v.y

    @staticmethod
    def crossProductZ(u, v):
        """Returns the z coordinate of the cross product of the vectors u and v."""
        return u.x*v.y - u.y*v.x

    @staticmethod
    def computeAngle(u, v):
        """Returns the (oriented) angle between u and v."""
        return math.acos(Vector.dotProduct(u, v)/(u.norm()*v.norm()))


class Edge:
    """Class for handling edges of polygons."""
    class Inter:
        """
        Intersection class defined as a simple enum for better readability.

        Possible values:
         Edge.Inter.CROSS: Cross intersection. Two edges intersect in an X shape.
         Edge.Inter.DEGEN: Degenerate intersection. Two edges intersect but are collinear.
         Edge.Inter.NONE: No intersection between the two edges.
        """
        CROSS = 1
        DEGEN = 0
        NONE = -1

    def __init__(self, p, q):
        """Constructs an edge using two points."""
        self.p = p
        self.q = q

    def __repr__(self):
        """
        Converts Edge to its string representation.

        Note: This is the method that 'str()' and 'print()' use
        """
        return '{:} --> {:}'.format(self.p, self.q)

    def getLength(self):
        """Returns the length of an edge, that is the distance between its two points."""
        return Point.distance(self.p, self.q)

    def isInLeftHalfPlane(self, r, tol=1e-9):
        """Returns true if the given point is in the left half plane of the edge,
        and false otherwise."""
        u = self.q - self.p
        v = r - self.p
        return ge(Vector.crossProductZ(u, v), 0, tol)

    def isPointInside(self, p, tol=1e-9):
        """Returns whether a point is inside the edge."""
        # Note: a point is inside an edge if and only if the sum of the distance
        #  between the point and the extremes of the edge is equal to the length
        #  of the edge.
        return eq(Point.distance(self.p, p) + Point.distance(p, self.q), self.getLength(), tol)

    @staticmethod
    def computeAngle(e1, e2):
        """Returns the (oriented) angle between e1 and e2."""
        return Vector.computeAngle(e1.q - e1.p, e2.q - e2.p)

    @staticmethod
    def isEqual(e1, e2, tol=1e-9):
        """Returns whether two edges are equal."""
        # Note: two edges are equal if their extremes are equal.
        return (Point.isEqual(e1.p, e2.p, tol) and Point.isEqual(e1.q, e2.q, tol)) \
            or (Point.isEqual(e1.p, e2.q, tol) and Point.isEqual(e1.q, e2.p, tol))

    @staticmethod
    def hasIntersection(e1, e2, tol=1e-9):
        """Returns the kind of intersection that two edges have using Edge.Inter."""
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
        """
        Returns the kind of intersection of two edges using Edge.Inter, as well
         as a list of the points of intersection.
        """
        interType = Edge.hasIntersection(e1, e2, tol)
        if interType == Edge.Inter.NONE:
            return Edge.Inter.NONE, []

        elif interType == Edge.Inter.DEGEN:
            # Creating deep copies to prevent unexpected behavior in other parts
            #  of the program.
            ce1 = copy.deepcopy(e1)
            ce2 = copy.deepcopy(e2)

            # Rearranging so that the points in ce1 and ce2 are sorted, and ce1
            #  is the edge with a smaller p.
            if Point.compLexicographic(ce1.q, ce1.p):
                ce1.p, ce1.q = ce1.q, ce1.p
            if Point.compLexicographic(ce2.q, ce2.p):
                ce2.p, ce2.q = ce2.q, ce2.p
            if Point.compLexicographic(ce2.p, ce1.p):
                ce1, ce2 = ce2, ce1

            # Separing in three cases.
            if Point.compLexicographic(ce1.q, ce2.p):
                return Edge.Inter.DEGEN, []
            elif Point.isEqual(ce1.q, ce2.p, tol):
                return Edge.Inter.DEGEN, [ce1.q]
            else:
                if Point.compLexicographic(ce1.q, ce2.q):
                    return Edge.Inter.DEGEN, [ce2.p, ce1.q]
                else:
                    return Edge.Inter.DEGEN, [ce2.p, ce2.q]

        else:  # interType == Edge.Inter.CROSS
            den = (e1.p.x - e1.q.x)*(e2.p.y - e2.q.y) - (e1.p.y - e1.q.y)*(e2.p.x - e2.q.x)
            a = e1.p.x*e1.q.y - e1.p.y*e1.q.x
            b = e2.p.x*e2.q.y - e2.p.y*e2.q.x
            px = (a*(e2.p.x - e2.q.x) - (e1.p.x - e1.q.x)*b)/den
            py = (a*(e2.p.y - e2.q.y) - (e1.p.y - e1.q.y)*b)/den
            return Edge.Inter.CROSS, [Point(px, py)]


class Color:
    """
    Class created to handle colors in an easier way to read.

    The values r, g and b correspond to the red, green and blue channels of the
     RGB color space, and they are assumed to be between 0 and 1.
    """

    def __init__(self, r=0, g=0, b=0):
        """Constructs a color object using its RGB values. Defaults to black color."""
        self.r = r
        self.g = g
        self.b = b

    def __repr__(self):
        """
        Converts Color to its string representation.

        Note: This is the method that 'str()' and 'print()' use
        """
        return '{{{:.3f} {:.3f} {:.3f}}}'.format(self.r, self.g, self.b)

    def toIntegerTuple(self):
        """
        Converts to an RGB tuple whose values range between 0 and 255.
        """
        return math.floor(255*self.r), math.floor(255*self.g), math.floor(255*self.b)


class ConvexPolygon:
    """
    Class to handle convex polygons.

    Each polygon is represented as a list of its vertices, which are ordered and
     counter-clockwise oriented, starting from the smaller vertex in
     lexicographic order.
    """

    def __init__(self, points=[], color=Color(), sortedList=False, tol=1e-9):
        """
        Constructor of the ConvexPolygon class.

        If the constructor is called with sortedList=True, then the given points
         are assumed to be the vertices of the polygon and are also assumed to be
         arranged in the correct way. Hence, no further computation is done other
         than assignments.
        Otherwise, if the constructor is called with sortedList=False, the points
         are used to generate the corresponding convex hull using Graham's scan,
         which has time complexity O(nlogn) where n is the number of points.
        """
        self.color = color
        if sortedList or not points:
            self.points = points
            return

        # Choosing the first vertex of the final list of vertices.
        p0 = minWithComp(points, comp=Point.compLexicographic)

        # This is actually the cosine of the angle corresponding to the vectors
        #  u = (1, 0) and v = p - p0. This orders the points with respect to p0
        #  in a hand fan shape with origin in p0.
        def swipeAngle(p):
            return (p.y - p0.y)/(p - p0).norm()

        spoints = [p for p in points if not Point.isEqual(p, p0, tol)]
        spoints.sort(key=swipeAngle)

        n = len(spoints)
        self.points = [p0]
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
                iter += 1

            while len(self.points) >= 2 and Point.orientation(self.points[-1], self.points[-2], p) != Vector.Orien.CW:
                self.points.pop()  # The pop() method is O(1) for lists in Python.

            self.points.append(p)
            iter += 1

    def __repr__(self):
        """
        Converts ConvexPolygon to its string representation.

        Note: This is the method that 'str()' and 'print()' use
        """
        n = self.numberOfVertices()
        if n == 0:
            return ''
        else:
            return str(self.points[0]) + ' ' + ' '.join([str(self.points[i]) for i in range(-1, -n, -1)])

    def numberOfVertices(self):
        """Returns the number of vertices of the polygon."""
        return len(self.points)

    def isPointInside(self, p, tol=1e-9):
        """
        Returns whether a given point is inside the polygon.

        The time complexity of this method is O(log n), where n is the number of vertices.
        """
        n = self.numberOfVertices()
        if n == 0:
            return False
        elif n == 1:
            return Point.isEqual(self.points[0], p, tol)
        elif n == 2:
            return Edge(self.points[0], self.points[1]).isPointInside(p, tol)

        # Base case for the recursive algorithm
        def isInsideTriangle(q1, q2, q3):
            ori1 = Point.orientation(p, q1, q2)
            ori2 = Point.orientation(p, q2, q3)
            ori3 = Point.orientation(p, q3, q1)
            return (ori1 == Vector.Orien.CCW and ori2 == Vector.Orien.CCW and ori3 == Vector.Orien.CCW) or \
                (ori1 == Vector.Orien.DEGEN and Edge(q1, q2).isPointInside(p)) or \
                (ori2 == Vector.Orien.DEGEN and Edge(q2, q3).isPointInside(p)) or \
                (ori3 == Vector.Orien.DEGEN and Edge(q3, q1).isPointInside(p))

        q0 = self.points[0]

        # Recursive algorithm that finds in which of the triangles determined
        #  by the vertex indices (0, i-1, i) for all i, lies the point p, and uses
        #  that as base case to determine if p is in the convex polygon.
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

    def isPolygonInside(self, poly, tol=1e-9):
        """
        Returns whether a given polygon is inside our polygon.

        This method has O(n + m) time complexity, where n and m are the number
         of vertices of the polygons.
        """
        # Note: This method could also be implemented checking whether each of the
        #  points of the given polygon are inside our polygon with the 'isPointInside'
        #  method, but that would give us O(mlogn) time complexity, which is worse.
        inter = ConvexPolygon.intersect(self, poly)
        return ConvexPolygon.isEqual(inter, poly, tol)

    def edges(self):
        """Returns a list with the edges of the polygon."""
        n = self.numberOfVertices()
        if n <= 1:
            return
        elif n == 2:
            return [Edge(self.points[0], self.points[1])]
        else:
            return [Edge(p, q) for (p, q) in shiftZip(self.points, self.points, 1)]

    def perimeter(self):
        """Returns the perimeter of the polygon."""
        return sum(e.getLength() for e in self.edges())

    def isRegular(self, tol=1e-9):
        """
        Returns whether the polygon is regular or not.

        This method works by checking if all the inner angles are the same and the
         length of all the edges is also the same.
        """
        if self.numberOfVertices() <= 2:
            return True

        edges = self.edges()
        expectedAngle = 2*math.pi/n
        expectedLength = edges[0].getLength()  # Arbitrary, we could have chosen the i-th.

        # Using a generator with all(), means that whenever one of the conditions
        #  is not satisfied, it will immediately return 'False' without having
        #  to compute the next ones
        return all(eq(Edge.computeAngle(e1, e2), expectedAngle, tol) and
                   eq(e1.getLength(), expectedLength, tol)
                   for (e1, e2) in shiftZip(edges, edges, 1))

    def area(self):
        """
        Returns the area of the polygon.

        This method is linear in time and uses Green's theorem of integral calculus.
        """
        if self.numberOfVertices() <= 2:
            return 0

        n = self.numberOfVertices()
        ps = self.points  # For better readability
        sum = 0
        for i in range(-1, n - 1):
            sum += ps[i].x*(ps[i + 1].y - ps[i - 1].y)

        return sum/2

    def centroid(self):
        """Returns the centroid of the polygon. If n == 0 it returns None."""
        n = self.numberOfVertices()
        if n == 0:
            return None
        elif n == 1:
            return copy.deepcopy(self.points[0])
        elif n == 2:
            ps = self.points  # Defined for readability
            return Point((ps[0].x + ps[1].x)/2, (ps[0].y + ps[1].y)/2)

        ps = self.points  # For better readability
        doubleArea = 0  # Area computed again to avoid redundant operations
        cx = cy = 0
        for i in range(-1, n - 1):
            a = ps[i].x*ps[i + 1].y - ps[i + 1].x*ps[i].y
            cx += (ps[i].x + ps[i + 1].x)*a
            cy += (ps[i].y + ps[i + 1].y)*a
            doubleArea += a

        return Point(cx/(3*doubleArea), cy/(3*doubleArea))

    def boundingBox(self, color=Color(), tol=1e-9):
        """Returns the bounding box of the polygon as a polygon of the given color."""
        n = self.numberOfVertices()
        if n <= 1:
            return ConvexPolygon([], color=color, sortedList=True)
        if n == 2:
            # Defined for readability
            x0, y0 = self.points[0].x, self.points[0].y
            x1, y1 = self.points[1].x, self.points[1].y
            if eq(x0, x1, tol) or eq(y0, y1, tol):  # Degenerate case
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
        """
        Translates the whole polygon by a given vector.

        Note: this method modifies the polygon.
        """
        self.points = [p + u for p in self.points]

    def rotate(self, angle):
        """
        Rotates the polygon a given angle around its centroid.

        Note: this method modifies the polygon.
        """
        center = self.centroid()
        for p in self.points:
            p.rotate(angle, c=center)

        self.points = beginWithMin(self.points, comp=Point.compLexicographic)

    def scale(self, factor, tol=1e-9):
        """
        Scales the polygon with respect to its centroid by given factor.

        Note: this method modifies the polygon
        """
        center = self.centroid()
        if eq(factor, 0, tol):
            self.points = [center]
        else:
            for p in self.points:
                p.x = center.x + (p.x - center.x)*factor
                p.y = center.y + (p.y - center.y)*factor

    @staticmethod
    def convexUnion(poly1, poly2, color=Color(), tol=1e-9):
        """
        Returns the convex union of two polygons.

        It does so by computing the convex hull of its vertices, which has a
         O((n + m)log(n + m)) time complexity, where n and m are the number of
         vertices of the polygons.
        """
        return ConvexPolygon(copy.deepcopy(poly1.points) + copy.deepcopy(poly2.points),
                             color=color, tol=tol)

    @staticmethod
    def isEqual(poly1, poly2, tol=1e-9):
        """
        Returns whether two given polygons are equal.

        Note: since the way in which the vertices of the polygons are arranged in
         the self.points lists is unique, it suffices to compare the polygons vertex
         per vertex, which gives us a O(n) time complexity, where n is the number of
         vertices.
        """
        if poly1.numberOfVertices() != poly2.numberOfVertices():
            return False

        for (p, q) in zip(poly1.points, poly2.points):
            if not Point.isEqual(p, q, tol):
                return False

        return True

    @staticmethod
    def random(n, xdom=(0, 1), ydom=(0, 1), color=Color(), tol=1e-9):
        """Generates a random polygon."""
        points = [Point.random(xdom=xdom, ydom=ydom) for _ in range(0, n)]
        return ConvexPolygon(points, color=color, tol=tol)

    @staticmethod
    def genRegularPolygon(n=0, r=1, c=Point(0, 0), phase=0, color=Color()):
        """
        Generates a regular polygon with n vertices, radius r and center c.

        By default, the righ-most vertex of the polygon will lie on the line
         {y = c.y}. However, it can be rotated using the phase parameter, which
         takes an angle in radians.
        """
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
        """
        Computes the boundaries of a list of polygons.

        In other words, it returns the left-most, bottom.most, right-most and
         top-most coordinates of the vertices of the given polygons.

        Note: If the list is empty or only has 0-gons, then it returns left = math.inf,
         bottom = math.inf, right = -math.inf and top = -math.inf
        """
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

    @staticmethod
    def intersect(poly1, poly2, color=Color(), tol=1e-9):
        """
        Computes the intersection of two given polygons.

        The algorithm implemented in this method is adapted from the intersection
         of convex polygons algorithm described in the paper by O'Rourke, Chien
         et al. This algorithm has O(n + m) time complexity, where n and m are
         the number of vertices of the polygons.
        """

        # Defined just to make code easier to read
        emptyPoly = ConvexPolygon([], color=color, sortedList=True)

        # Function defined to handle the trivial cases, that is n1 <= 2 or n2 <= 2.
        #  The purpose of this function is to prevent duplicated code by ensuring
        #  that sn1 <= sn2.
        def trivialCases(spoly1, spoly2, sn1, sn2):
            if sn1 == 0:
                return emptyPoly
            if sn1 == 1:
                if spoly2.isPointInside(spoly1.points[0]):
                    return ConvexPolygon(copy.deepcopy(spoly1.points),
                                         color=color, sortedList=True)
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

        n1 = poly1.numberOfVertices()
        n2 = poly2.numberOfVertices()

        # Handling of trivial cases
        if (n1 == 2 and n2 >= 3):
            e1 = Edge(poly1.points[0], poly1.points[1])
            for e2 in poly2.edges():
                interType, ps = Edge.intersect(e1, e2)
                if interType == Edge.Inter.DEGEN:
                    return ConvexPolygon(ps, color=color, sortedList=True)
        elif (n1 >= 3 and n2 == 2):
            e2 = Edge(poly2.points[0], poly2.points[1])
            for e1 in poly1.edges():
                interType, ps = Edge.intersect(e1, e2)
                if interType == Edge.Inter.DEGEN:
                    return ConvexPolygon(ps, color=color, sortedList=True)
        elif (n1 <= 2 or n2 <= 2):
            if n1 <= n2:
                return trivialCases(poly1, poly2, n1, n2)
            else:
                return trivialCases(poly2, poly1, n2, n1)

        # Handling of the general case
        class Place:
            inPoly1 = -1
            unknown = 0
            inPoly2 = 1

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
                    return ConvexPolygon(beginWithMin(inter, comp=Point.compLexicographic),
                                         color=color, sortedList=True)
                else:
                    if not inter:
                        firstInterIter = iter
                    if not inter or (inter and not Point.isEqual(inter[0], p, tol) and
                                     not Point.isEqual(inter[-1], p, tol)):
                        inter.append(p)
                    if e2.isInLeftHalfPlane(e1.q):
                        place = Place.inPoly1
                    else:
                        place = Place.inPoly2

            if place == Place.inPoly1 and not Point.isEqual(inter[-1], e1.q, tol):
                inter.append(copy.deepcopy(e1.q))
            elif place == Place.inPoly2 and not Point.isEqual(inter[-1], e2.q, tol):
                inter.append(copy.deepcopy(e2.q))

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

            iter += 1

        if inter:
            return ConvexPolygon(beginWithMin(inter, comp=Point.compLexicographic),
                                 color=color, sortedList=True)

        p1 = poly1.points[0]
        p2 = poly2.points[0]
        if poly2.isPointInside(p1):
            return ConvexPolygon(copy.deepcopy(poly1.points), color=color, sortedList=True)
        if poly1.isPointInside(p2):
            return ConvexPolygon(copy.deepcopy(poly2.points), color=color, sortedList=True)
        return emptyPoly

    @staticmethod
    def draw(polys=[], fileName='output.png', sideLength=400, margin=1, bg=Color(1, 1, 1), show=False, tol=1e-9):
        """
        Draws a list of polygons on a square image.

        By default, the file name is 'output.png', the side length of the image
         is 400, the drawing margin is 1, the background color is white, and the
         image is not automatically shown in a new window.
        """
        img = Image.new('RGB', (sideLength, sideLength), bg.toIntegerTuple())
        dib = ImageDraw.Draw(img)

        if not polys:
            if show:
                img.show()
            img.save(fileName)
            return

        left, bottom, right, top = ConvexPolygon.boundaries(polys)

        # Degenerate cases
        if left == math.inf or eq(left, right, tol) and eq(bottom, top, tol):
            def fitToCanvas(poly):
                return [(sideLength/2, sideLength/2) for p in poly.points]

        # General case
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
            n = poly.numberOfVertices()
            if n == 1:
                dib.point(fitToCanvas(poly), fill=poly.color.toIntegerTuple())
            elif n >= 2:
                dib.polygon(fitToCanvas(poly), outline=poly.color.toIntegerTuple())

        if show:
            img.show()

        img.save(fileName)
