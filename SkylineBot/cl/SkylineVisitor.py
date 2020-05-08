# Generated from Skyline.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
else:
    from SkylineParser import SkylineParser

# This class defines a complete generic visitor for a parse tree produced by SkylineParser.

class SkylineVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SkylineParser#root.
    def visitRoot(self, ctx:SkylineParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#assignStmt.
    def visitAssignStmt(self, ctx:SkylineParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#exprStmt.
    def visitExprStmt(self, ctx:SkylineParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#mirror.
    def visitMirror(self, ctx:SkylineParser.MirrorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#exprIdent.
    def visitExprIdent(self, ctx:SkylineParser.ExprIdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#arithmetic.
    def visitArithmetic(self, ctx:SkylineParser.ArithmeticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#parenthesis.
    def visitParenthesis(self, ctx:SkylineParser.ParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#value.
    def visitValue(self, ctx:SkylineParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#multiple.
    def visitMultiple(self, ctx:SkylineParser.MultipleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#random.
    def visitRandom(self, ctx:SkylineParser.RandomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#building.
    def visitBuilding(self, ctx:SkylineParser.BuildingContext):
        return self.visitChildren(ctx)



del SkylineParser