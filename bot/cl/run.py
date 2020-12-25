# antlr4 -Dlanguage=Python3 -no-listener -visitor Poly.g

import sys
from antlr4 import *
from PolyLexer import PolyLexer
from PolyParser import PolyParser
from PolyVisitor import PolyVisitor
from PolyEval import PolyEval

from polygons import *

visitor = PolyEval()
if False:
    input_stream = InputStream(
        """
    // Stupid script
    x := [0 0  1 0  0 1]
    print x
    """
    )
else:
    input_stream = InputStream(
        """
    // sample script
    p1 := [0 0  0 1  1 1  0.2 0.8]
    color p1, {1 0 0}
    print p1
    area p1
    perimeter p1
    vertices p1
    centroid p1

    print "---"

    p2 := [0 0  1 0  1 1]
    color p2, {0 1 0}
    print p2
    equal p1, p2
    inside p1, p2
    inside [0.8 0.2], p2

    draw "image.png", p1, p2

    print "---"

    print p1 + p2                           // convex union
    print p1 * p2                           // intersection
    print #p2                               // bounding box
    equal p1 + p2, #p2                      // complex operations
    p3 := #((p1 + p2) * [0 0  1 0  1 1])    // complex operations

    r := !100                               // convex polygon made with 100 random points
    """
    )

lexer = PolyLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = PolyParser(token_stream)
tree = parser.root()
print('===== Result =====')
text, images = visitor.visit(tree)
print(text, end='')
print(images)
