# Generated from Poly.g by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PolyParser import PolyParser
else:
    from PolyParser import PolyParser

# This class defines a complete generic visitor for a parse tree produced by PolyParser.

class PolyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PolyParser#root.
    def visitRoot(self, ctx:PolyParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyParser#cmt.
    def visitCmt(self, ctx:PolyParser.CmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyParser#stmt.
    def visitStmt(self, ctx:PolyParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyParser#poly.
    def visitPoly(self, ctx:PolyParser.PolyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyParser#color.
    def visitColor(self, ctx:PolyParser.ColorContext):
        return self.visitChildren(ctx)



del PolyParser