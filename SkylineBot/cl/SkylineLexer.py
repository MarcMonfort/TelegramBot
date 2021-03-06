# Generated from Skyline.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22")
        buf.write("R\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n")
        buf.write("\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\17\6\17")
        buf.write("A\n\17\r\17\16\17B\3\20\3\20\7\20G\n\20\f\20\16\20J\13")
        buf.write("\20\3\21\6\21M\n\21\r\21\16\21N\3\21\3\21\2\2\22\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33")
        buf.write("\17\35\20\37\21!\22\3\2\6\3\2\62;\4\2C\\c|\5\2\62;C\\")
        buf.write("c|\4\2\f\f\"\"\2T\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\3#\3\2\2\2\5%\3\2\2\2\7\'\3\2\2\2\t)\3\2\2\2\13+\3")
        buf.write("\2\2\2\r-\3\2\2\2\17/\3\2\2\2\21\61\3\2\2\2\23\63\3\2")
        buf.write("\2\2\25\65\3\2\2\2\27\67\3\2\2\2\319\3\2\2\2\33<\3\2\2")
        buf.write("\2\35@\3\2\2\2\37D\3\2\2\2!L\3\2\2\2#$\7*\2\2$\4\3\2\2")
        buf.write("\2%&\7+\2\2&\6\3\2\2\2\'(\7]\2\2(\b\3\2\2\2)*\7.\2\2*")
        buf.write("\n\3\2\2\2+,\7_\2\2,\f\3\2\2\2-.\7}\2\2.\16\3\2\2\2/\60")
        buf.write("\7\177\2\2\60\20\3\2\2\2\61\62\7,\2\2\62\22\3\2\2\2\63")
        buf.write("\64\7\61\2\2\64\24\3\2\2\2\65\66\7-\2\2\66\26\3\2\2\2")
        buf.write("\678\7/\2\28\30\3\2\2\29:\7,\2\2:;\7,\2\2;\32\3\2\2\2")
        buf.write("<=\7<\2\2=>\7?\2\2>\34\3\2\2\2?A\t\2\2\2@?\3\2\2\2AB\3")
        buf.write("\2\2\2B@\3\2\2\2BC\3\2\2\2C\36\3\2\2\2DH\t\3\2\2EG\t\4")
        buf.write("\2\2FE\3\2\2\2GJ\3\2\2\2HF\3\2\2\2HI\3\2\2\2I \3\2\2\2")
        buf.write("JH\3\2\2\2KM\t\5\2\2LK\3\2\2\2MN\3\2\2\2NL\3\2\2\2NO\3")
        buf.write("\2\2\2OP\3\2\2\2PQ\b\21\2\2Q\"\3\2\2\2\6\2BHN\3\b\2\2")
        return buf.getvalue()


class SkylineLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    MUL = 8
    DIV = 9
    ADD = 10
    SUB = 11
    POW = 12
    ASSIGN = 13
    NUM = 14
    ID = 15
    WS = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'['", "','", "']'", "'{'", "'}'", "'*'", "'/'", 
            "'+'", "'-'", "'**'", "':='" ]

    symbolicNames = [ "<INVALID>",
            "MUL", "DIV", "ADD", "SUB", "POW", "ASSIGN", "NUM", "ID", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "MUL", "DIV", "ADD", "SUB", "POW", "ASSIGN", "NUM", "ID", 
                  "WS" ]

    grammarFileName = "Skyline.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


