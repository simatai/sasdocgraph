# Generated from ./grammar/SAS.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SASParser import SASParser
else:
    from SASParser import SASParser

# This class defines a complete listener for a parse tree produced by SASParser.
class SASListener(ParseTreeListener):

    # Enter a parse tree produced by SASParser#parse.
    def enterParse(self, ctx:SASParser.ParseContext):
        pass

    # Exit a parse tree produced by SASParser#parse.
    def exitParse(self, ctx:SASParser.ParseContext):
        pass


    # Enter a parse tree produced by SASParser#sas_stmt_list.
    def enterSas_stmt_list(self, ctx:SASParser.Sas_stmt_listContext):
        pass

    # Exit a parse tree produced by SASParser#sas_stmt_list.
    def exitSas_stmt_list(self, ctx:SASParser.Sas_stmt_listContext):
        pass


    # Enter a parse tree produced by SASParser#set_stmt.
    def enterSet_stmt(self, ctx:SASParser.Set_stmtContext):
        pass

    # Exit a parse tree produced by SASParser#set_stmt.
    def exitSet_stmt(self, ctx:SASParser.Set_stmtContext):
        pass


    # Enter a parse tree produced by SASParser#run_stmt.
    def enterRun_stmt(self, ctx:SASParser.Run_stmtContext):
        pass

    # Exit a parse tree produced by SASParser#run_stmt.
    def exitRun_stmt(self, ctx:SASParser.Run_stmtContext):
        pass


    # Enter a parse tree produced by SASParser#data_stmt.
    def enterData_stmt(self, ctx:SASParser.Data_stmtContext):
        pass

    # Exit a parse tree produced by SASParser#data_stmt.
    def exitData_stmt(self, ctx:SASParser.Data_stmtContext):
        pass


    # Enter a parse tree produced by SASParser#dataset_name.
    def enterDataset_name(self, ctx:SASParser.Dataset_nameContext):
        pass

    # Exit a parse tree produced by SASParser#dataset_name.
    def exitDataset_name(self, ctx:SASParser.Dataset_nameContext):
        pass


    # Enter a parse tree produced by SASParser#proc_stmt.
    def enterProc_stmt(self, ctx:SASParser.Proc_stmtContext):
        pass

    # Exit a parse tree produced by SASParser#proc_stmt.
    def exitProc_stmt(self, ctx:SASParser.Proc_stmtContext):
        pass


    # Enter a parse tree produced by SASParser#any_stmt.
    def enterAny_stmt(self, ctx:SASParser.Any_stmtContext):
        pass

    # Exit a parse tree produced by SASParser#any_stmt.
    def exitAny_stmt(self, ctx:SASParser.Any_stmtContext):
        pass


    # Enter a parse tree produced by SASParser#any_text.
    def enterAny_text(self, ctx:SASParser.Any_textContext):
        pass

    # Exit a parse tree produced by SASParser#any_text.
    def exitAny_text(self, ctx:SASParser.Any_textContext):
        pass


    # Enter a parse tree produced by SASParser#expression.
    def enterExpression(self, ctx:SASParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SASParser#expression.
    def exitExpression(self, ctx:SASParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SASParser#expressionList.
    def enterExpressionList(self, ctx:SASParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by SASParser#expressionList.
    def exitExpressionList(self, ctx:SASParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by SASParser#of_var_list.
    def enterOf_var_list(self, ctx:SASParser.Of_var_listContext):
        pass

    # Exit a parse tree produced by SASParser#of_var_list.
    def exitOf_var_list(self, ctx:SASParser.Of_var_listContext):
        pass


    # Enter a parse tree produced by SASParser#identifiers_list.
    def enterIdentifiers_list(self, ctx:SASParser.Identifiers_listContext):
        pass

    # Exit a parse tree produced by SASParser#identifiers_list.
    def exitIdentifiers_list(self, ctx:SASParser.Identifiers_listContext):
        pass


    # Enter a parse tree produced by SASParser#in_var_list.
    def enterIn_var_list(self, ctx:SASParser.In_var_listContext):
        pass

    # Exit a parse tree produced by SASParser#in_var_list.
    def exitIn_var_list(self, ctx:SASParser.In_var_listContext):
        pass


    # Enter a parse tree produced by SASParser#colonInts.
    def enterColonInts(self, ctx:SASParser.ColonIntsContext):
        pass

    # Exit a parse tree produced by SASParser#colonInts.
    def exitColonInts(self, ctx:SASParser.ColonIntsContext):
        pass


    # Enter a parse tree produced by SASParser#literal.
    def enterLiteral(self, ctx:SASParser.LiteralContext):
        pass

    # Exit a parse tree produced by SASParser#literal.
    def exitLiteral(self, ctx:SASParser.LiteralContext):
        pass


    # Enter a parse tree produced by SASParser#variables.
    def enterVariables(self, ctx:SASParser.VariablesContext):
        pass

    # Exit a parse tree produced by SASParser#variables.
    def exitVariables(self, ctx:SASParser.VariablesContext):
        pass


