from skyline import Skyline
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
    from .SkylineVisitor import SkylineVisitor

else:
    from SkylineParser import SkylineParser
    from SkylineVisitor import SkylineVisitor


class EvalVisitor(SkylineVisitor):

    def __init__(self, symTable=dict()):
        self.symTable = symTable

    def visitRoot(self, ctx: SkylineParser.RootContext):
        n = next(ctx.getChildren())
        return self.visit(n)

    def visitParenthesis(self, ctx: SkylineParser.ParenthesisContext):
        return self.visit(ctx.expr())

    def visitMirror(self, ctx: SkylineParser.MirrorContext):
        return -self.visit(ctx.expr())

    def visitArithmetic(self, ctx: SkylineParser.ArithmeticContext):
        l = [self.visit(n) for n in ctx.getChildren()]

        isSky = isinstance(l[0], Skyline) or isinstance(l[0], Skyline)
        if isinstance(l[0], int) and isinstance(l[2], Skyline):
            raise Exception("No existeix l'operació: N " +
                            str(ctx.getChild(1)) + " Skyline")

        if ctx.ADD():
            return l[0] + l[2]
        elif ctx.SUB():
            if isinstance(l[2], Skyline):
                raise Exception("No existeix l'operació: Skyline - Skyline")
            return l[0] - l[2]
        elif ctx.MUL():
            return l[0] * l[2]
        elif ctx.DIV():
            if isSky:
                raise Exception("Operació '/' incompatible amb Skyline")
            return l[0] / l[2]
        elif ctx.POW():
            if isSky:
                raise Exception("Operació 'Pow' incompatible amb Skyline")
            return l[0] ** l[2]

    def visitExprIdent(self, ctx: SkylineParser.ExprIdentContext):
        if not str(ctx.ID()) in self.symTable:
            raise Exception("Variable '" + str(ctx.ID()) + "' no definida: ")
        return self.symTable.get(str(ctx.ID()))

    def visitValue(self, ctx: SkylineParser.ValueContext):
        n = next(ctx.getChildren())
        if ctx.NUM():
            return int(n.getText())
        elif ctx.building():
            xmin, top, xmax = self.visit(n)
            return Skyline.single(xmin, top, xmax)
        elif ctx.city():
            return self.visit(n)

    def visitBuilding(self, ctx: SkylineParser.BuildingContext):
        xmin = self.visit(ctx.expr(0))
        top = self.visit(ctx.expr(1))
        xmax = self.visit(ctx.expr(2))

        if not isinstance(xmin, int):
            raise Exception("xmin no es un enter")
        if not isinstance(top, int):
            raise Exception("alçada no es un enter")
        if not isinstance(xmax, int):
            raise Exception("xmax no es un enter")
        if (xmax <= xmin):
            raise Exception(
                "La posició final ha de ser més gran que la inicial: " + str(xmin) + '>' + str(xmax))
        if (top < 0):
            raise Exception("Alçada negativa: " + str(top))
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
        l = [self.visit(n) for n in ctx.expr()]
        for x in l:
            if not isinstance(x, int):
                raise Exception(
                    "El valors en {n, h, w, xmin, xmax} han de ser enters.")
        if (l[0] < 0):
            raise Exception("Nombre d'edificis negatius: " + str(l[0]))
        if (l[1] < 0):
            raise Exception("Alçada negativa: " + str(l[1]))
        if (l[2] <= 0):
            raise Exception("Amplada inferior a 1: " + str(l[2]))
        if (l[4] <= l[3]):
            raise Exception(
                "La posició final ha de ser més gran que la inicial: " + str(l[3]) + '>' + str(l[4]))
        return Skyline.random(l[0], l[1], l[2], l[3], l[4])

    def visitAssignStmt(self, ctx: SkylineParser.AssignStmtContext):
        self.symTable[str(ctx.ID())] = self.visit(ctx.expr())
        return self.symTable[str(ctx.ID())]
