
import sys
from antlr4 import *
from saspyparser import SASLexer
from saspyparser import SASParser
from saspyparser import SASListener

class DataStepPrinter(SASListener.SASListener):     
    def enterData_stmt(self, ctx):         
        print("Oh, a Data Step!") 

    def enterSet_stmt(self, ctx):
        print("with a set")

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