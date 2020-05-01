import sys
from antlr4 import *
from cl.SkylineLexer import SkylineLexer
from cl.SkylineParser import SkylineParser

import matplotlib.pyplot as plt  # grafica

from skyline import Skyline


#from TreeVisitor import TreeVisitor
from cl.EvalVisitor import EvalVisitor


#input_stream = InputStream(input('? '))
input_stream = StdinStream()
#input_stream = FileStream(sys.argv[1])


lexer = SkylineLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = SkylineParser(token_stream)
tree = parser.root()
print(tree.toStringTree(recog=parser))

""" visitor = TreeVisitor()
visitor.visit(tree) """

#visitor2 = EvalVisitor({'a' : 7})
visitor2 = EvalVisitor()

a = visitor2.visit(tree)


if isinstance(a, Skyline):
    print(a.start)
    print(a.width)
    print(a.height)
    plt.bar(a.start, a.height, a.width, align='edge')
    plt.show()
else:
    print(a)
