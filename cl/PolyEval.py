if __name__ is not None and "." in __name__:
    from .PolyParser import PolyParser
    from .PolyVisitor import PolyVisitor
else:
    from PolyParser import PolyParser
    from PolyVisitor import PolyVisitor

from polygons import *


class PolyEval(PolyVisitor):
    def __init__(self):
        self.polyDict = {}

    def visitStmt(self, ctx: PolyParser.StmtContext):
        l = list(ctx.getChildren())
        n = len(l)
        keyWord = l[0].getSymbol().type

        if keyWord == PolyParser.IDEN:
            self.polyDict[l[0].getText()] = self.visit(l[2])
        elif keyWord == PolyParser.COLOR:
            poly = self.polyDict[l[1].getText()]
            poly.color = self.visit(l[3])
        elif keyWord == PolyParser.PRINT:
            if type(l[1]) == PolyParser.PolyContext:
                print('Polygon:', self.visit(l[1]))
            elif l[1].getSymbol().type == PolyParser.QTEXT:
                print('Text:', l[1].getText()[1:-1])
        elif keyWord == PolyParser.AREA:
            print('Area: {:.3f}'.format(self.visit(l[1]).getArea()))
        elif keyWord == PolyParser.PERIM:
            print('Perimeter: {:.3f}'.format(self.visit(l[1]).getPerimeter()))
        elif keyWord == PolyParser.VERT:
            print('Vertices:', self.visit(l[1]).getNumberOfVertices())
        elif keyWord == PolyParser.CENTR:
            print('Centroid:', self.visit(l[1]).getCentroid())
        elif keyWord == PolyParser.INSIDE:
            poly1 = self.visit(l[1])
            poly2 = self.visit(l[3])
            yn = ConvexPolygon.isContained(poly1, poly2)
            if yn:
                print('Inside: yes')
            else:
                print('Inside: no')
        elif keyWord == PolyParser.EQUAL:
            poly1 = self.visit(l[1])
            poly2 = self.visit(l[3])
            yn = ConvexPolygon.isEqual(poly1, poly2)
            if yn:
                print('Equal: yes')
            else:
                print('Equal: no')
        elif keyWord == PolyParser.DRAW:
            fileName = l[1].getText()[1:-1]
            polys = [self.visit(l[i]) for i in range(3, n, 2)]
            ConvexPolygon.draw(polys, fileName=fileName, show=True)

    def visitPoly(self, ctx: PolyParser.PolyContext):
        l = list(ctx.getChildren())
        n = len(l)

        if type(l[0]) == PolyParser.PolyContext:
            opType = l[1].getSymbol().type
            if opType == PolyParser.INTER:
                print('Warning: to be replaced by the intersection.')
                return ConvexPolygon.convexUnion(self.visit(l[0]), self.visit(l[2]))

            elif opType == PolyParser.UNION:
                return ConvexPolygon.convexUnion(self.visit(l[0]), self.visit(l[2]))
        else:
            keyWord = l[0].getSymbol().type
            if keyWord == PolyParser.LSQUARE:
                if n == 2:
                    return ConvexPolygon()

                return ConvexPolygon(
                    [Point(float(l[i].getText()), float(l[i + 1].getText()))
                     for i in range(1, n - 1, 2)])

            elif keyWord == PolyParser.LPAREN:
                return self.visit(l[1])
            elif keyWord == PolyParser.BOUND:
                return self.visit(l[1]).getBoundingBox()
            elif keyWord == PolyParser.IDEN:
                return self.polyDict[l[0].getText()]
            elif keyWord == PolyParser.RAND:
                return ConvexPolygon.random(int(l[1].getText()))

    def visitColor(self, ctx: PolyParser.PolyContext):
        # Defined to make the code easier to read
        l = list(ctx.getChildren())
        r = float(l[1].getText())
        g = float(l[2].getText())
        b = float(l[3].getText())
        return Color(r, g, b)
