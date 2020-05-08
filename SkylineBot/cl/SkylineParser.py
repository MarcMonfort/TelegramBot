# Generated from Skyline.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("T\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\5\3\24\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\5\4 \n\4\3\4\5\4#\n\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\7\4.\n\4\f\4\16\4\61\13\4\3\5\3\5\3")
        buf.write("\5\3\5\7\5\67\n\5\f\5\16\5:\13\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5J\n\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\2\3\6\7\2\4\6\b\n\2\4\3\2\n")
        buf.write("\13\3\2\f\r\2Y\2\f\3\2\2\2\4\23\3\2\2\2\6\"\3\2\2\2\b")
        buf.write("I\3\2\2\2\nK\3\2\2\2\f\r\5\4\3\2\r\16\7\2\2\3\16\3\3\2")
        buf.write("\2\2\17\20\7\21\2\2\20\21\7\17\2\2\21\24\5\6\4\2\22\24")
        buf.write("\5\6\4\2\23\17\3\2\2\2\23\22\3\2\2\2\24\5\3\2\2\2\25\26")
        buf.write("\b\4\1\2\26\27\7\3\2\2\27\30\5\6\4\2\30\31\7\4\2\2\31")
        buf.write("#\3\2\2\2\32\33\7\r\2\2\33#\5\6\4\b\34 \5\n\6\2\35 \5")
        buf.write("\b\5\2\36 \7\20\2\2\37\34\3\2\2\2\37\35\3\2\2\2\37\36")
        buf.write("\3\2\2\2 #\3\2\2\2!#\7\21\2\2\"\25\3\2\2\2\"\32\3\2\2")
        buf.write("\2\"\37\3\2\2\2\"!\3\2\2\2#/\3\2\2\2$%\f\7\2\2%&\7\16")
        buf.write("\2\2&.\5\6\4\7\'(\f\6\2\2()\t\2\2\2).\5\6\4\7*+\f\5\2")
        buf.write("\2+,\t\3\2\2,.\5\6\4\6-$\3\2\2\2-\'\3\2\2\2-*\3\2\2\2")
        buf.write(".\61\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60\7\3\2\2\2\61/\3")
        buf.write("\2\2\2\62\63\7\5\2\2\638\5\n\6\2\64\65\7\6\2\2\65\67\5")
        buf.write("\n\6\2\66\64\3\2\2\2\67:\3\2\2\28\66\3\2\2\289\3\2\2\2")
        buf.write("9;\3\2\2\2:8\3\2\2\2;<\7\7\2\2<J\3\2\2\2=>\7\b\2\2>?\5")
        buf.write("\6\4\2?@\7\6\2\2@A\5\6\4\2AB\7\6\2\2BC\5\6\4\2CD\7\6\2")
        buf.write("\2DE\5\6\4\2EF\7\6\2\2FG\5\6\4\2GH\7\t\2\2HJ\3\2\2\2I")
        buf.write("\62\3\2\2\2I=\3\2\2\2J\t\3\2\2\2KL\7\3\2\2LM\5\6\4\2M")
        buf.write("N\7\6\2\2NO\5\6\4\2OP\7\6\2\2PQ\5\6\4\2QR\7\4\2\2R\13")
        buf.write("\3\2\2\2\t\23\37\"-/8I")
        return buf.getvalue()


class SkylineParser ( Parser ):

    grammarFileName = "Skyline.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'['", "','", "']'", "'{'", 
                     "'}'", "'*'", "'/'", "'+'", "'-'", "'**'", "':='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "MUL", "DIV", "ADD", "SUB", "POW", "ASSIGN", "NUM", 
                      "ID", "WS" ]

    RULE_root = 0
    RULE_statement = 1
    RULE_expr = 2
    RULE_city = 3
    RULE_building = 4

    ruleNames =  [ "root", "statement", "expr", "city", "building" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    MUL=8
    DIV=9
    ADD=10
    SUB=11
    POW=12
    ASSIGN=13
    NUM=14
    ID=15
    WS=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(SkylineParser.StatementContext,0)


        def EOF(self):
            return self.getToken(SkylineParser.EOF, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = SkylineParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.statement()
            self.state = 11
            self.match(SkylineParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SkylineParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExprStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SkylineParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStmt" ):
                return visitor.visitExprStmt(self)
            else:
                return visitor.visitChildren(self)


    class AssignStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SkylineParser.ID, 0)
        def ASSIGN(self):
            return self.getToken(SkylineParser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(SkylineParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = SkylineParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 17
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = SkylineParser.AssignStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.match(SkylineParser.ID)
                self.state = 14
                self.match(SkylineParser.ASSIGN)
                self.state = 15
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = SkylineParser.ExprStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SkylineParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MirrorContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SUB(self):
            return self.getToken(SkylineParser.SUB, 0)
        def expr(self):
            return self.getTypedRuleContext(SkylineParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMirror" ):
                return visitor.visitMirror(self)
            else:
                return visitor.visitChildren(self)


    class ExprIdentContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SkylineParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprIdent" ):
                return visitor.visitExprIdent(self)
            else:
                return visitor.visitChildren(self)


    class ArithmeticContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.ExprContext)
            else:
                return self.getTypedRuleContext(SkylineParser.ExprContext,i)

        def POW(self):
            return self.getToken(SkylineParser.POW, 0)
        def MUL(self):
            return self.getToken(SkylineParser.MUL, 0)
        def DIV(self):
            return self.getToken(SkylineParser.DIV, 0)
        def ADD(self):
            return self.getToken(SkylineParser.ADD, 0)
        def SUB(self):
            return self.getToken(SkylineParser.SUB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmetic" ):
                return visitor.visitArithmetic(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesisContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SkylineParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesis" ):
                return visitor.visitParenthesis(self)
            else:
                return visitor.visitChildren(self)


    class ValueContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def building(self):
            return self.getTypedRuleContext(SkylineParser.BuildingContext,0)

        def city(self):
            return self.getTypedRuleContext(SkylineParser.CityContext,0)

        def NUM(self):
            return self.getToken(SkylineParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SkylineParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = SkylineParser.ParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 20
                self.match(SkylineParser.T__0)
                self.state = 21
                self.expr(0)
                self.state = 22
                self.match(SkylineParser.T__1)
                pass

            elif la_ == 2:
                localctx = SkylineParser.MirrorContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 24
                self.match(SkylineParser.SUB)
                self.state = 25
                self.expr(6)
                pass

            elif la_ == 3:
                localctx = SkylineParser.ValueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 29
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SkylineParser.T__0]:
                    self.state = 26
                    self.building()
                    pass
                elif token in [SkylineParser.T__2, SkylineParser.T__5]:
                    self.state = 27
                    self.city()
                    pass
                elif token in [SkylineParser.NUM]:
                    self.state = 28
                    self.match(SkylineParser.NUM)
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 4:
                localctx = SkylineParser.ExprIdentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 31
                self.match(SkylineParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 45
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 43
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = SkylineParser.ArithmeticContext(self, SkylineParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 34
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 35
                        localctx.op = self.match(SkylineParser.POW)
                        self.state = 36
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = SkylineParser.ArithmeticContext(self, SkylineParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 37
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 38
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SkylineParser.MUL or _la==SkylineParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 39
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = SkylineParser.ArithmeticContext(self, SkylineParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 40
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 41
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SkylineParser.ADD or _la==SkylineParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 42
                        self.expr(4)
                        pass

             
                self.state = 47
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CityContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SkylineParser.RULE_city

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RandomContext(CityContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.CityContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.ExprContext)
            else:
                return self.getTypedRuleContext(SkylineParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRandom" ):
                return visitor.visitRandom(self)
            else:
                return visitor.visitChildren(self)


    class MultipleContext(CityContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.CityContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def building(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.BuildingContext)
            else:
                return self.getTypedRuleContext(SkylineParser.BuildingContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiple" ):
                return visitor.visitMultiple(self)
            else:
                return visitor.visitChildren(self)



    def city(self):

        localctx = SkylineParser.CityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_city)
        self._la = 0 # Token type
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SkylineParser.T__2]:
                localctx = SkylineParser.MultipleContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.match(SkylineParser.T__2)
                self.state = 49
                self.building()
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SkylineParser.T__3:
                    self.state = 50
                    self.match(SkylineParser.T__3)
                    self.state = 51
                    self.building()
                    self.state = 56
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 57
                self.match(SkylineParser.T__4)
                pass
            elif token in [SkylineParser.T__5]:
                localctx = SkylineParser.RandomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.match(SkylineParser.T__5)
                self.state = 60
                self.expr(0)
                self.state = 61
                self.match(SkylineParser.T__3)
                self.state = 62
                self.expr(0)
                self.state = 63
                self.match(SkylineParser.T__3)
                self.state = 64
                self.expr(0)
                self.state = 65
                self.match(SkylineParser.T__3)
                self.state = 66
                self.expr(0)
                self.state = 67
                self.match(SkylineParser.T__3)
                self.state = 68
                self.expr(0)
                self.state = 69
                self.match(SkylineParser.T__6)
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


    class BuildingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.ExprContext)
            else:
                return self.getTypedRuleContext(SkylineParser.ExprContext,i)


        def getRuleIndex(self):
            return SkylineParser.RULE_building

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBuilding" ):
                return visitor.visitBuilding(self)
            else:
                return visitor.visitChildren(self)




    def building(self):

        localctx = SkylineParser.BuildingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_building)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(SkylineParser.T__0)
            self.state = 74
            self.expr(0)
            self.state = 75
            self.match(SkylineParser.T__3)
            self.state = 76
            self.expr(0)
            self.state = 77
            self.match(SkylineParser.T__3)
            self.state = 78
            self.expr(0)
            self.state = 79
            self.match(SkylineParser.T__1)
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
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




