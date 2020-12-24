# Generated from Poly.g by ANTLR 4.9
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\32")
        buf.write("d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\7\2")
        buf.write("\17\n\2\f\2\16\2\22\13\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4#\n\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\7\4;\n\4\f\4\16\4>\13\4\5\4@\n\4")
        buf.write("\3\5\3\5\3\5\3\5\7\5F\n\5\f\5\16\5I\13\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\5\5Q\n\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5Y\n\5\f")
        buf.write("\5\16\5\\\13\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\2\3\b\7\2\4")
        buf.write("\6\b\n\2\2\2q\2\20\3\2\2\2\4\25\3\2\2\2\6?\3\2\2\2\bP")
        buf.write("\3\2\2\2\n]\3\2\2\2\f\17\5\4\3\2\r\17\5\6\4\2\16\f\3\2")
        buf.write("\2\2\16\r\3\2\2\2\17\22\3\2\2\2\20\16\3\2\2\2\20\21\3")
        buf.write("\2\2\2\21\23\3\2\2\2\22\20\3\2\2\2\23\24\7\2\2\3\24\3")
        buf.write("\3\2\2\2\25\26\7\32\2\2\26\5\3\2\2\2\27\30\7\27\2\2\30")
        buf.write("\31\7\3\2\2\31@\5\b\5\2\32\33\7\b\2\2\33\34\5\b\5\2\34")
        buf.write("\35\7\25\2\2\35\36\5\n\6\2\36@\3\2\2\2\37\"\7\t\2\2 #")
        buf.write("\5\b\5\2!#\7\31\2\2\" \3\2\2\2\"!\3\2\2\2#@\3\2\2\2$%")
        buf.write("\7\n\2\2%@\5\b\5\2&\'\7\13\2\2\'@\5\b\5\2()\7\f\2\2)@")
        buf.write("\5\b\5\2*+\7\r\2\2+@\5\b\5\2,-\7\16\2\2-.\5\b\5\2./\7")
        buf.write("\25\2\2/\60\5\b\5\2\60@\3\2\2\2\61\62\7\17\2\2\62\63\5")
        buf.write("\b\5\2\63\64\7\25\2\2\64\65\5\b\5\2\65@\3\2\2\2\66\67")
        buf.write("\7\20\2\2\67<\7\31\2\289\7\25\2\29;\5\b\5\2:8\3\2\2\2")
        buf.write(";>\3\2\2\2<:\3\2\2\2<=\3\2\2\2=@\3\2\2\2><\3\2\2\2?\27")
        buf.write("\3\2\2\2?\32\3\2\2\2?\37\3\2\2\2?$\3\2\2\2?&\3\2\2\2?")
        buf.write("(\3\2\2\2?*\3\2\2\2?,\3\2\2\2?\61\3\2\2\2?\66\3\2\2\2")
        buf.write("@\7\3\2\2\2AB\b\5\1\2BG\7\23\2\2CD\7\26\2\2DF\7\26\2\2")
        buf.write("EC\3\2\2\2FI\3\2\2\2GE\3\2\2\2GH\3\2\2\2HJ\3\2\2\2IG\3")
        buf.write("\2\2\2JQ\7\24\2\2KL\7\6\2\2LQ\5\b\5\7MQ\7\27\2\2NO\7\7")
        buf.write("\2\2OQ\7\26\2\2PA\3\2\2\2PK\3\2\2\2PM\3\2\2\2PN\3\2\2")
        buf.write("\2QZ\3\2\2\2RS\f\6\2\2ST\7\4\2\2TY\5\b\5\7UV\f\5\2\2V")
        buf.write("W\7\5\2\2WY\5\b\5\6XR\3\2\2\2XU\3\2\2\2Y\\\3\2\2\2ZX\3")
        buf.write("\2\2\2Z[\3\2\2\2[\t\3\2\2\2\\Z\3\2\2\2]^\7\21\2\2^_\7")
        buf.write("\26\2\2_`\7\26\2\2`a\7\26\2\2ab\7\22\2\2b\13\3\2\2\2\13")
        buf.write("\16\20\"<?GPXZ")
        return buf.getvalue()


class PolyParser ( Parser ):

    grammarFileName = "Poly.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'*'", "'+'", "'#'", "'!'", "'color'", 
                     "'print'", "'area'", "'perimeter'", "'vertices'", "'centroid'", 
                     "'inside'", "'equal'", "'draw'", "'{'", "'}'", "'['", 
                     "']'", "','" ]

    symbolicNames = [ "<INVALID>", "ASSIGN", "INTER", "UNION", "BOUND", 
                      "RAND", "COLOR", "PRINT", "AREA", "PERIM", "VERT", 
                      "CENTR", "INSIDE", "EQUAL", "DRAW", "LCURLY", "RCURLY", 
                      "LSQUARE", "RSQUARE", "COLON", "FLOAT", "IDEN", "WS", 
                      "QTEXT", "COMMENT" ]

    RULE_root = 0
    RULE_cmt = 1
    RULE_stmt = 2
    RULE_poly = 3
    RULE_color = 4

    ruleNames =  [ "root", "cmt", "stmt", "poly", "color" ]

    EOF = Token.EOF
    ASSIGN=1
    INTER=2
    UNION=3
    BOUND=4
    RAND=5
    COLOR=6
    PRINT=7
    AREA=8
    PERIM=9
    VERT=10
    CENTR=11
    INSIDE=12
    EQUAL=13
    DRAW=14
    LCURLY=15
    RCURLY=16
    LSQUARE=17
    RSQUARE=18
    COLON=19
    FLOAT=20
    IDEN=21
    WS=22
    QTEXT=23
    COMMENT=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PolyParser.EOF, 0)

        def cmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PolyParser.CmtContext)
            else:
                return self.getTypedRuleContext(PolyParser.CmtContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PolyParser.StmtContext)
            else:
                return self.getTypedRuleContext(PolyParser.StmtContext,i)


        def getRuleIndex(self):
            return PolyParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = PolyParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PolyParser.COLOR) | (1 << PolyParser.PRINT) | (1 << PolyParser.AREA) | (1 << PolyParser.PERIM) | (1 << PolyParser.VERT) | (1 << PolyParser.CENTR) | (1 << PolyParser.INSIDE) | (1 << PolyParser.EQUAL) | (1 << PolyParser.DRAW) | (1 << PolyParser.IDEN) | (1 << PolyParser.COMMENT))) != 0):
                self.state = 12
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [PolyParser.COMMENT]:
                    self.state = 10
                    self.cmt()
                    pass
                elif token in [PolyParser.COLOR, PolyParser.PRINT, PolyParser.AREA, PolyParser.PERIM, PolyParser.VERT, PolyParser.CENTR, PolyParser.INSIDE, PolyParser.EQUAL, PolyParser.DRAW, PolyParser.IDEN]:
                    self.state = 11
                    self.stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 16
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 17
            self.match(PolyParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(PolyParser.COMMENT, 0)

        def getRuleIndex(self):
            return PolyParser.RULE_cmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmt" ):
                return visitor.visitCmt(self)
            else:
                return visitor.visitChildren(self)




    def cmt(self):

        localctx = PolyParser.CmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_cmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(PolyParser.COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDEN(self):
            return self.getToken(PolyParser.IDEN, 0)

        def ASSIGN(self):
            return self.getToken(PolyParser.ASSIGN, 0)

        def poly(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PolyParser.PolyContext)
            else:
                return self.getTypedRuleContext(PolyParser.PolyContext,i)


        def COLOR(self):
            return self.getToken(PolyParser.COLOR, 0)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(PolyParser.COLON)
            else:
                return self.getToken(PolyParser.COLON, i)

        def color(self):
            return self.getTypedRuleContext(PolyParser.ColorContext,0)


        def PRINT(self):
            return self.getToken(PolyParser.PRINT, 0)

        def QTEXT(self):
            return self.getToken(PolyParser.QTEXT, 0)

        def AREA(self):
            return self.getToken(PolyParser.AREA, 0)

        def PERIM(self):
            return self.getToken(PolyParser.PERIM, 0)

        def VERT(self):
            return self.getToken(PolyParser.VERT, 0)

        def CENTR(self):
            return self.getToken(PolyParser.CENTR, 0)

        def INSIDE(self):
            return self.getToken(PolyParser.INSIDE, 0)

        def EQUAL(self):
            return self.getToken(PolyParser.EQUAL, 0)

        def DRAW(self):
            return self.getToken(PolyParser.DRAW, 0)

        def getRuleIndex(self):
            return PolyParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = PolyParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PolyParser.IDEN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.match(PolyParser.IDEN)
                self.state = 22
                self.match(PolyParser.ASSIGN)
                self.state = 23
                self.poly(0)
                pass
            elif token in [PolyParser.COLOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.match(PolyParser.COLOR)
                self.state = 25
                self.poly(0)
                self.state = 26
                self.match(PolyParser.COLON)
                self.state = 27
                self.color()
                pass
            elif token in [PolyParser.PRINT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.match(PolyParser.PRINT)
                self.state = 32
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [PolyParser.BOUND, PolyParser.RAND, PolyParser.LSQUARE, PolyParser.IDEN]:
                    self.state = 30
                    self.poly(0)
                    pass
                elif token in [PolyParser.QTEXT]:
                    self.state = 31
                    self.match(PolyParser.QTEXT)
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [PolyParser.AREA]:
                self.enterOuterAlt(localctx, 4)
                self.state = 34
                self.match(PolyParser.AREA)
                self.state = 35
                self.poly(0)
                pass
            elif token in [PolyParser.PERIM]:
                self.enterOuterAlt(localctx, 5)
                self.state = 36
                self.match(PolyParser.PERIM)
                self.state = 37
                self.poly(0)
                pass
            elif token in [PolyParser.VERT]:
                self.enterOuterAlt(localctx, 6)
                self.state = 38
                self.match(PolyParser.VERT)
                self.state = 39
                self.poly(0)
                pass
            elif token in [PolyParser.CENTR]:
                self.enterOuterAlt(localctx, 7)
                self.state = 40
                self.match(PolyParser.CENTR)
                self.state = 41
                self.poly(0)
                pass
            elif token in [PolyParser.INSIDE]:
                self.enterOuterAlt(localctx, 8)
                self.state = 42
                self.match(PolyParser.INSIDE)
                self.state = 43
                self.poly(0)
                self.state = 44
                self.match(PolyParser.COLON)
                self.state = 45
                self.poly(0)
                pass
            elif token in [PolyParser.EQUAL]:
                self.enterOuterAlt(localctx, 9)
                self.state = 47
                self.match(PolyParser.EQUAL)
                self.state = 48
                self.poly(0)
                self.state = 49
                self.match(PolyParser.COLON)
                self.state = 50
                self.poly(0)
                pass
            elif token in [PolyParser.DRAW]:
                self.enterOuterAlt(localctx, 10)
                self.state = 52
                self.match(PolyParser.DRAW)
                self.state = 53
                self.match(PolyParser.QTEXT)
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PolyParser.COLON:
                    self.state = 54
                    self.match(PolyParser.COLON)
                    self.state = 55
                    self.poly(0)
                    self.state = 60
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PolyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSQUARE(self):
            return self.getToken(PolyParser.LSQUARE, 0)

        def RSQUARE(self):
            return self.getToken(PolyParser.RSQUARE, 0)

        def FLOAT(self, i:int=None):
            if i is None:
                return self.getTokens(PolyParser.FLOAT)
            else:
                return self.getToken(PolyParser.FLOAT, i)

        def BOUND(self):
            return self.getToken(PolyParser.BOUND, 0)

        def poly(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PolyParser.PolyContext)
            else:
                return self.getTypedRuleContext(PolyParser.PolyContext,i)


        def IDEN(self):
            return self.getToken(PolyParser.IDEN, 0)

        def RAND(self):
            return self.getToken(PolyParser.RAND, 0)

        def INTER(self):
            return self.getToken(PolyParser.INTER, 0)

        def UNION(self):
            return self.getToken(PolyParser.UNION, 0)

        def getRuleIndex(self):
            return PolyParser.RULE_poly

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPoly" ):
                return visitor.visitPoly(self)
            else:
                return visitor.visitChildren(self)



    def poly(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PolyParser.PolyContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_poly, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PolyParser.LSQUARE]:
                self.state = 64
                self.match(PolyParser.LSQUARE)
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PolyParser.FLOAT:
                    self.state = 65
                    self.match(PolyParser.FLOAT)
                    self.state = 66
                    self.match(PolyParser.FLOAT)
                    self.state = 71
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 72
                self.match(PolyParser.RSQUARE)
                pass
            elif token in [PolyParser.BOUND]:
                self.state = 73
                self.match(PolyParser.BOUND)
                self.state = 74
                self.poly(5)
                pass
            elif token in [PolyParser.IDEN]:
                self.state = 75
                self.match(PolyParser.IDEN)
                pass
            elif token in [PolyParser.RAND]:
                self.state = 76
                self.match(PolyParser.RAND)
                self.state = 77
                self.match(PolyParser.FLOAT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 88
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 86
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = PolyParser.PolyContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_poly)
                        self.state = 80
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 81
                        self.match(PolyParser.INTER)
                        self.state = 82
                        self.poly(5)
                        pass

                    elif la_ == 2:
                        localctx = PolyParser.PolyContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_poly)
                        self.state = 83
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 84
                        self.match(PolyParser.UNION)
                        self.state = 85
                        self.poly(4)
                        pass

             
                self.state = 90
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ColorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCURLY(self):
            return self.getToken(PolyParser.LCURLY, 0)

        def FLOAT(self, i:int=None):
            if i is None:
                return self.getTokens(PolyParser.FLOAT)
            else:
                return self.getToken(PolyParser.FLOAT, i)

        def RCURLY(self):
            return self.getToken(PolyParser.RCURLY, 0)

        def getRuleIndex(self):
            return PolyParser.RULE_color

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColor" ):
                return visitor.visitColor(self)
            else:
                return visitor.visitChildren(self)




    def color(self):

        localctx = PolyParser.ColorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_color)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(PolyParser.LCURLY)
            self.state = 92
            self.match(PolyParser.FLOAT)
            self.state = 93
            self.match(PolyParser.FLOAT)
            self.state = 94
            self.match(PolyParser.FLOAT)
            self.state = 95
            self.match(PolyParser.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.poly_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def poly_sempred(self, localctx:PolyContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




