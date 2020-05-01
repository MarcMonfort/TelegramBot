from skyline import Skyline
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
    from .SkylineVisitor import SkylineVisitor

else:
    from SkylineParser import SkylineParser
    from SkylineVisitor import SkylineVisitor

""" import sys
sys.path.append("..") """


class EvalVisitor(SkylineVisitor):

    #symTable = dict()

    def __init__(self, vars=dict()):
        self.symTable = vars

    def visitRoot(self, ctx: SkylineParser.RootContext):
        n = next(ctx.getChildren())
        return self.visit(n)
        # return Skyline(1,2,3)
        # print(self.visit(n))

    def visitParenthesis(self, ctx: SkylineParser.ParenthesisContext):
        return self.visit(ctx.expr())

    def visitMirror(self, ctx: SkylineParser.MirrorContext):
        return -self.visit(ctx.expr())

    def visitArithmetic(self, ctx: SkylineParser.ArithmeticContext):    #tratamiento de errores!
        l = [n for n in ctx.getChildren()]

        if ctx.ADD():
            return self.visit(l[0]) + self.visit(l[2])
        elif ctx.SUB():
            return self.visit(l[0]) - self.visit(l[2])
        elif ctx.MUL():
            return self.visit(l[0]) * self.visit(l[2])
        elif ctx.DIV():
            return self.visit(l[0]) / self.visit(l[2])
        elif ctx.POW():
            return self.visit(l[0]) ** self.visit(l[2])

    def visitExprIdent(self, ctx: SkylineParser.ExprIdentContext):
        return self.symTable.get(str(ctx.ID()))

    def visitValue(self, ctx: SkylineParser.ValueContext):  # deberia crear skyline
        n = next(ctx.getChildren())
        if ctx.NUM():
            return int(n.getText())
        elif ctx.building():
            xmin, top, xmax = self.visit(n)
            return Skyline(xmin, top, xmax-xmin)
        elif ctx.city():
            return self.visit(n)

    def visitBuilding(self, ctx: SkylineParser.BuildingContext):
        xmin = int(ctx.NUM(0).getText())
        top = int(ctx.NUM(1).getText())
        xmax = int(ctx.NUM(2).getText())
        return xmin, top, xmax

    def visitMultiple(self, ctx: SkylineParser.MultipleContext):
        start = []
        height = []
        width = []
        for x in ctx.building():
            xmin, top, xmax = self.visit(x)
            start.append(xmin)
            height.append(top)
            width.append(xmax-xmin)
        return Skyline(start, height, width)

    def visitRandom(self, ctx: SkylineParser.RandomContext):
        l = [int(n.getText()) for n in ctx.NUM()]
        return Skyline.random(l[0], l[1], l[2], l[3], l[4])

    def visitAssignStmt(self, ctx: SkylineParser.AssignStmtContext):
        self.symTable[str(ctx.ID())] = self.visit(ctx.expr())
        return self.symTable[str(ctx.ID())]
