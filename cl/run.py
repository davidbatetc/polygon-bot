import sys
from antlr4 import *
from PolyLexer import PolyLexer
from PolyParser import PolyParser

#input_stream = InputStream(input('? '))

input_stream = InputStream(
    """
// C'est la
// vie
print x + y
print "C'est la vie, mon ami!"
draw "image.png", p1, p2, p3
"""
)

lexer = PolyLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = PolyParser(token_stream)
tree = parser.root()

print(tree.toStringTree(recog=parser))
