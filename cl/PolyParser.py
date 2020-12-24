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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\34")
        buf.write("c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\7\2\r\n\2\f")
        buf.write("\2\16\2\20\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\5\3\36\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\7\3\66\n\3\f\3\16\39\13\3\5\3;\n\3\3\4\3\4\3\4\3\4")
        buf.write("\7\4A\n\4\f\4\16\4D\13\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\5\4P\n\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4X\n\4\f")
        buf.write("\4\16\4[\13\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\2\3\6\6\2\4")
        buf.write("\6\b\2\2\2r\2\16\3\2\2\2\4:\3\2\2\2\6O\3\2\2\2\b\\\3\2")
        buf.write("\2\2\n\r\7\34\2\2\13\r\5\4\3\2\f\n\3\2\2\2\f\13\3\2\2")
        buf.write("\2\r\20\3\2\2\2\16\f\3\2\2\2\16\17\3\2\2\2\17\21\3\2\2")
        buf.write("\2\20\16\3\2\2\2\21\22\7\2\2\3\22\3\3\2\2\2\23\24\7\31")
        buf.write("\2\2\24\25\7\3\2\2\25;\5\6\4\2\26\27\7\b\2\2\27\30\7\31")
        buf.write("\2\2\30\31\7\27\2\2\31;\5\b\5\2\32\35\7\t\2\2\33\36\5")
        buf.write("\6\4\2\34\36\7\33\2\2\35\33\3\2\2\2\35\34\3\2\2\2\36;")
        buf.write("\3\2\2\2\37 \7\n\2\2 ;\5\6\4\2!\"\7\13\2\2\";\5\6\4\2")
        buf.write("#$\7\f\2\2$;\5\6\4\2%&\7\r\2\2&;\5\6\4\2\'(\7\16\2\2(")
        buf.write(")\5\6\4\2)*\7\27\2\2*+\5\6\4\2+;\3\2\2\2,-\7\17\2\2-.")
        buf.write("\5\6\4\2./\7\27\2\2/\60\5\6\4\2\60;\3\2\2\2\61\62\7\20")
        buf.write("\2\2\62\67\7\33\2\2\63\64\7\27\2\2\64\66\5\6\4\2\65\63")
        buf.write("\3\2\2\2\669\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28;\3\2\2")
        buf.write("\29\67\3\2\2\2:\23\3\2\2\2:\26\3\2\2\2:\32\3\2\2\2:\37")
        buf.write("\3\2\2\2:!\3\2\2\2:#\3\2\2\2:%\3\2\2\2:\'\3\2\2\2:,\3")
        buf.write("\2\2\2:\61\3\2\2\2;\5\3\2\2\2<=\b\4\1\2=B\7\23\2\2>?\7")
        buf.write("\30\2\2?A\7\30\2\2@>\3\2\2\2AD\3\2\2\2B@\3\2\2\2BC\3\2")
        buf.write("\2\2CE\3\2\2\2DB\3\2\2\2EP\7\24\2\2FG\7\21\2\2GH\5\6\4")
        buf.write("\2HI\7\22\2\2IP\3\2\2\2JK\7\6\2\2KP\5\6\4\7LP\7\31\2\2")
        buf.write("MN\7\7\2\2NP\7\30\2\2O<\3\2\2\2OF\3\2\2\2OJ\3\2\2\2OL")
        buf.write("\3\2\2\2OM\3\2\2\2PY\3\2\2\2QR\f\6\2\2RS\7\4\2\2SX\5\6")
        buf.write("\4\7TU\f\5\2\2UV\7\5\2\2VX\5\6\4\6WQ\3\2\2\2WT\3\2\2\2")
        buf.write("X[\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z\7\3\2\2\2[Y\3\2\2\2\\")
        buf.write("]\7\25\2\2]^\7\30\2\2^_\7\30\2\2_`\7\30\2\2`a\7\26\2\2")
        buf.write("a\t\3\2\2\2\13\f\16\35\67:BOWY")
        return buf.getvalue()


class PolyParser ( Parser ):

    grammarFileName = "Poly.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'*'", "'+'", "'#'", "'!'", "'color'", 
                     "'print'", "'area'", "'perimeter'", "'vertices'", "'centroid'", 
                     "'inside'", "'equal'", "'draw'", "'('", "')'", "'['", 
                     "']'", "'{'", "'}'", "','" ]

    symbolicNames = [ "<INVALID>", "ASSIGN", "INTER", "UNION", "BOUND", 
                      "RAND", "COLOR", "PRINT", "AREA", "PERIM", "VERT", 
                      "CENTR", "INSIDE", "EQUAL", "DRAW", "LPAREN", "RPAREN", 
                      "LSQUARE", "RSQUARE", "LCURLY", "RCURLY", "COLON", 
                      "NUM", "IDEN", "WS", "QTEXT", "COMMENT" ]

    RULE_root = 0
    RULE_stmt = 1
    RULE_poly = 2
    RULE_color = 3

    ruleNames =  [ "root", "stmt", "poly", "color" ]

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
    LPAREN=15
    RPAREN=16
    LSQUARE=17
    RSQUARE=18
    LCURLY=19
    RCURLY=20
    COLON=21
    NUM=22
    IDEN=23
    WS=24
    QTEXT=25
    COMMENT=26

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

        def COMMENT(self, i:int=None):
            if i is None:
                return self.getTokens(PolyParser.COMMENT)
            else:
                return self.getToken(PolyParser.COMMENT, i)

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
            self.state = 12
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PolyParser.COLOR) | (1 << PolyParser.PRINT) | (1 << PolyParser.AREA) | (1 << PolyParser.PERIM) | (1 << PolyParser.VERT) | (1 << PolyParser.CENTR) | (1 << PolyParser.INSIDE) | (1 << PolyParser.EQUAL) | (1 << PolyParser.DRAW) | (1 << PolyParser.IDEN) | (1 << PolyParser.COMMENT))) != 0):
                self.state = 10
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [PolyParser.COMMENT]:
                    self.state = 8
                    self.match(PolyParser.COMMENT)
                    pass
                elif token in [PolyParser.COLOR, PolyParser.PRINT, PolyParser.AREA, PolyParser.PERIM, PolyParser.VERT, PolyParser.CENTR, PolyParser.INSIDE, PolyParser.EQUAL, PolyParser.DRAW, PolyParser.IDEN]:
                    self.state = 9
                    self.stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 14
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 15
            self.match(PolyParser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PolyParser.IDEN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.match(PolyParser.IDEN)
                self.state = 18
                self.match(PolyParser.ASSIGN)
                self.state = 19
                self.poly(0)
                pass
            elif token in [PolyParser.COLOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.match(PolyParser.COLOR)
                self.state = 21
                self.match(PolyParser.IDEN)
                self.state = 22
                self.match(PolyParser.COLON)
                self.state = 23
                self.color()
                pass
            elif token in [PolyParser.PRINT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 24
                self.match(PolyParser.PRINT)
                self.state = 27
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [PolyParser.BOUND, PolyParser.RAND, PolyParser.LPAREN, PolyParser.LSQUARE, PolyParser.IDEN]:
                    self.state = 25
                    self.poly(0)
                    pass
                elif token in [PolyParser.QTEXT]:
                    self.state = 26
                    self.match(PolyParser.QTEXT)
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [PolyParser.AREA]:
                self.enterOuterAlt(localctx, 4)
                self.state = 29
                self.match(PolyParser.AREA)
                self.state = 30
                self.poly(0)
                pass
            elif token in [PolyParser.PERIM]:
                self.enterOuterAlt(localctx, 5)
                self.state = 31
                self.match(PolyParser.PERIM)
                self.state = 32
                self.poly(0)
                pass
            elif token in [PolyParser.VERT]:
                self.enterOuterAlt(localctx, 6)
                self.state = 33
                self.match(PolyParser.VERT)
                self.state = 34
                self.poly(0)
                pass
            elif token in [PolyParser.CENTR]:
                self.enterOuterAlt(localctx, 7)
                self.state = 35
                self.match(PolyParser.CENTR)
                self.state = 36
                self.poly(0)
                pass
            elif token in [PolyParser.INSIDE]:
                self.enterOuterAlt(localctx, 8)
                self.state = 37
                self.match(PolyParser.INSIDE)
                self.state = 38
                self.poly(0)
                self.state = 39
                self.match(PolyParser.COLON)
                self.state = 40
                self.poly(0)
                pass
            elif token in [PolyParser.EQUAL]:
                self.enterOuterAlt(localctx, 9)
                self.state = 42
                self.match(PolyParser.EQUAL)
                self.state = 43
                self.poly(0)
                self.state = 44
                self.match(PolyParser.COLON)
                self.state = 45
                self.poly(0)
                pass
            elif token in [PolyParser.DRAW]:
                self.enterOuterAlt(localctx, 10)
                self.state = 47
                self.match(PolyParser.DRAW)
                self.state = 48
                self.match(PolyParser.QTEXT)
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PolyParser.COLON:
                    self.state = 49
                    self.match(PolyParser.COLON)
                    self.state = 50
                    self.poly(0)
                    self.state = 55
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

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(PolyParser.NUM)
            else:
                return self.getToken(PolyParser.NUM, i)

        def LPAREN(self):
            return self.getToken(PolyParser.LPAREN, 0)

        def poly(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PolyParser.PolyContext)
            else:
                return self.getTypedRuleContext(PolyParser.PolyContext,i)


        def RPAREN(self):
            return self.getToken(PolyParser.RPAREN, 0)

        def BOUND(self):
            return self.getToken(PolyParser.BOUND, 0)

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
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_poly, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PolyParser.LSQUARE]:
                self.state = 59
                self.match(PolyParser.LSQUARE)
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PolyParser.NUM:
                    self.state = 60
                    self.match(PolyParser.NUM)
                    self.state = 61
                    self.match(PolyParser.NUM)
                    self.state = 66
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 67
                self.match(PolyParser.RSQUARE)
                pass
            elif token in [PolyParser.LPAREN]:
                self.state = 68
                self.match(PolyParser.LPAREN)
                self.state = 69
                self.poly(0)
                self.state = 70
                self.match(PolyParser.RPAREN)
                pass
            elif token in [PolyParser.BOUND]:
                self.state = 72
                self.match(PolyParser.BOUND)
                self.state = 73
                self.poly(5)
                pass
            elif token in [PolyParser.IDEN]:
                self.state = 74
                self.match(PolyParser.IDEN)
                pass
            elif token in [PolyParser.RAND]:
                self.state = 75
                self.match(PolyParser.RAND)
                self.state = 76
                self.match(PolyParser.NUM)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 87
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 85
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = PolyParser.PolyContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_poly)
                        self.state = 79
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 80
                        self.match(PolyParser.INTER)
                        self.state = 81
                        self.poly(5)
                        pass

                    elif la_ == 2:
                        localctx = PolyParser.PolyContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_poly)
                        self.state = 82
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 83
                        self.match(PolyParser.UNION)
                        self.state = 84
                        self.poly(4)
                        pass

             
                self.state = 89
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

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(PolyParser.NUM)
            else:
                return self.getToken(PolyParser.NUM, i)

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
        self.enterRule(localctx, 6, self.RULE_color)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(PolyParser.LCURLY)
            self.state = 91
            self.match(PolyParser.NUM)
            self.state = 92
            self.match(PolyParser.NUM)
            self.state = 93
            self.match(PolyParser.NUM)
            self.state = 94
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
        self._predicates[2] = self.poly_sempred
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
         




