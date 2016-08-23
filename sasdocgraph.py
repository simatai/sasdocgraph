
import sys
from antlr4 import *
from saspyparser import SASLexer
from saspyparser import SASParser
from saspyparser import SASListener


class DataStepPrinter(SASListener.SASListener):
    def __init__(self):
       self.fromDataSet =""
       self.toDataSet =""
     
    def enterParse(self, ctx):
        print("digraph {")
     
    def enterData_stmt(self, ctx):
        self.toDataSet = ctx.dataset_name().getText()

    def enterSet_stmt(self, ctx):
        self.fromDataSet=ctx.dataset_name().getText()
        print(self.fromDataSet + "->" + self.toDataSet)

    def exitParse(self, ctx):
        print("}")

def main(argv):
    if len(argv) > 1:
      inFileName = argv[1]
    else:
      inFileName = "./tests/test-grammar.sas"
    input = FileStream(inFileName)
    lexer = SASLexer.SASLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SASParser.SASParser(stream)
    tree = parser.parse()
    printer = DataStepPrinter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
	
if __name__ == '__main__':
    main(sys.argv)