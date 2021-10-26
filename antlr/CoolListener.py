# Generated from h:\Documentos\Escuela\Diseño de compiladores\Git\proyecto_etapa1y2\proyecto_etapa1y2\antlr\Cool.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CoolParser import CoolParser
else:
    from CoolParser import CoolParser

# This class defines a complete listener for a parse tree produced by CoolParser.
class CoolListener(ParseTreeListener):

    # Enter a parse tree produced by CoolParser#program.
    def enterProgram(self, ctx:CoolParser.ProgramContext):
        pass

    # Exit a parse tree produced by CoolParser#program.
    def exitProgram(self, ctx:CoolParser.ProgramContext):
        pass


    # Enter a parse tree produced by CoolParser#klass.
    def enterKlass(self, ctx:CoolParser.KlassContext):
        pass

    # Exit a parse tree produced by CoolParser#klass.
    def exitKlass(self, ctx:CoolParser.KlassContext):
        pass


    # Enter a parse tree produced by CoolParser#feature.
    def enterFeature(self, ctx:CoolParser.FeatureContext):
        pass

    # Exit a parse tree produced by CoolParser#feature.
    def exitFeature(self, ctx:CoolParser.FeatureContext):
        pass


    # Enter a parse tree produced by CoolParser#parameter.
    def enterParameter(self, ctx:CoolParser.ParameterContext):
        pass

    # Exit a parse tree produced by CoolParser#parameter.
    def exitParameter(self, ctx:CoolParser.ParameterContext):
        pass


    # Enter a parse tree produced by CoolParser#mult.
    def enterMult(self, ctx:CoolParser.MultContext):
        pass

    # Exit a parse tree produced by CoolParser#mult.
    def exitMult(self, ctx:CoolParser.MultContext):
        pass


    # Enter a parse tree produced by CoolParser#isvoid.
    def enterIsvoid(self, ctx:CoolParser.IsvoidContext):
        pass

    # Exit a parse tree produced by CoolParser#isvoid.
    def exitIsvoid(self, ctx:CoolParser.IsvoidContext):
        pass


    # Enter a parse tree produced by CoolParser#lt.
    def enterLt(self, ctx:CoolParser.LtContext):
        pass

    # Exit a parse tree produced by CoolParser#lt.
    def exitLt(self, ctx:CoolParser.LtContext):
        pass


    # Enter a parse tree produced by CoolParser#String.
    def enterString(self, ctx:CoolParser.StringContext):
        pass

    # Exit a parse tree produced by CoolParser#String.
    def exitString(self, ctx:CoolParser.StringContext):
        pass


    # Enter a parse tree produced by CoolParser#while.
    def enterWhile(self, ctx:CoolParser.WhileContext):
        pass

    # Exit a parse tree produced by CoolParser#while.
    def exitWhile(self, ctx:CoolParser.WhileContext):
        pass


    # Enter a parse tree produced by CoolParser#div.
    def enterDiv(self, ctx:CoolParser.DivContext):
        pass

    # Exit a parse tree produced by CoolParser#div.
    def exitDiv(self, ctx:CoolParser.DivContext):
        pass


    # Enter a parse tree produced by CoolParser#not.
    def enterNot(self, ctx:CoolParser.NotContext):
        pass

    # Exit a parse tree produced by CoolParser#not.
    def exitNot(self, ctx:CoolParser.NotContext):
        pass


    # Enter a parse tree produced by CoolParser#let.
    def enterLet(self, ctx:CoolParser.LetContext):
        pass

    # Exit a parse tree produced by CoolParser#let.
    def exitLet(self, ctx:CoolParser.LetContext):
        pass


    # Enter a parse tree produced by CoolParser#block.
    def enterBlock(self, ctx:CoolParser.BlockContext):
        pass

    # Exit a parse tree produced by CoolParser#block.
    def exitBlock(self, ctx:CoolParser.BlockContext):
        pass


    # Enter a parse tree produced by CoolParser#ID.
    def enterID(self, ctx:CoolParser.IDContext):
        pass

    # Exit a parse tree produced by CoolParser#ID.
    def exitID(self, ctx:CoolParser.IDContext):
        pass


    # Enter a parse tree produced by CoolParser#if.
    def enterIf(self, ctx:CoolParser.IfContext):
        pass

    # Exit a parse tree produced by CoolParser#if.
    def exitIf(self, ctx:CoolParser.IfContext):
        pass


    # Enter a parse tree produced by CoolParser#case.
    def enterCase(self, ctx:CoolParser.CaseContext):
        pass

    # Exit a parse tree produced by CoolParser#case.
    def exitCase(self, ctx:CoolParser.CaseContext):
        pass


    # Enter a parse tree produced by CoolParser#par.
    def enterPar(self, ctx:CoolParser.ParContext):
        pass

    # Exit a parse tree produced by CoolParser#par.
    def exitPar(self, ctx:CoolParser.ParContext):
        pass


    # Enter a parse tree produced by CoolParser#new.
    def enterNew(self, ctx:CoolParser.NewContext):
        pass

    # Exit a parse tree produced by CoolParser#new.
    def exitNew(self, ctx:CoolParser.NewContext):
        pass


    # Enter a parse tree produced by CoolParser#simplecall.
    def enterSimplecall(self, ctx:CoolParser.SimplecallContext):
        pass

    # Exit a parse tree produced by CoolParser#simplecall.
    def exitSimplecall(self, ctx:CoolParser.SimplecallContext):
        pass


    # Enter a parse tree produced by CoolParser#invert.
    def enterInvert(self, ctx:CoolParser.InvertContext):
        pass

    # Exit a parse tree produced by CoolParser#invert.
    def exitInvert(self, ctx:CoolParser.InvertContext):
        pass


    # Enter a parse tree produced by CoolParser#false.
    def enterFalse(self, ctx:CoolParser.FalseContext):
        pass

    # Exit a parse tree produced by CoolParser#false.
    def exitFalse(self, ctx:CoolParser.FalseContext):
        pass


    # Enter a parse tree produced by CoolParser#less.
    def enterLess(self, ctx:CoolParser.LessContext):
        pass

    # Exit a parse tree produced by CoolParser#less.
    def exitLess(self, ctx:CoolParser.LessContext):
        pass


    # Enter a parse tree produced by CoolParser#eq.
    def enterEq(self, ctx:CoolParser.EqContext):
        pass

    # Exit a parse tree produced by CoolParser#eq.
    def exitEq(self, ctx:CoolParser.EqContext):
        pass


    # Enter a parse tree produced by CoolParser#int.
    def enterInt(self, ctx:CoolParser.IntContext):
        pass

    # Exit a parse tree produced by CoolParser#int.
    def exitInt(self, ctx:CoolParser.IntContext):
        pass


    # Enter a parse tree produced by CoolParser#plus.
    def enterPlus(self, ctx:CoolParser.PlusContext):
        pass

    # Exit a parse tree produced by CoolParser#plus.
    def exitPlus(self, ctx:CoolParser.PlusContext):
        pass


    # Enter a parse tree produced by CoolParser#objectCall.
    def enterObjectCall(self, ctx:CoolParser.ObjectCallContext):
        pass

    # Exit a parse tree produced by CoolParser#objectCall.
    def exitObjectCall(self, ctx:CoolParser.ObjectCallContext):
        pass


    # Enter a parse tree produced by CoolParser#asgn.
    def enterAsgn(self, ctx:CoolParser.AsgnContext):
        pass

    # Exit a parse tree produced by CoolParser#asgn.
    def exitAsgn(self, ctx:CoolParser.AsgnContext):
        pass


    # Enter a parse tree produced by CoolParser#true.
    def enterTrue(self, ctx:CoolParser.TrueContext):
        pass

    # Exit a parse tree produced by CoolParser#true.
    def exitTrue(self, ctx:CoolParser.TrueContext):
        pass


    # Enter a parse tree produced by CoolParser#le.
    def enterLe(self, ctx:CoolParser.LeContext):
        pass

    # Exit a parse tree produced by CoolParser#le.
    def exitLe(self, ctx:CoolParser.LeContext):
        pass


    # Enter a parse tree produced by CoolParser#assign.
    def enterAssign(self, ctx:CoolParser.AssignContext):
        pass

    # Exit a parse tree produced by CoolParser#assign.
    def exitAssign(self, ctx:CoolParser.AssignContext):
        pass


    # Enter a parse tree produced by CoolParser#case_stat.
    def enterCase_stat(self, ctx:CoolParser.Case_statContext):
        pass

    # Exit a parse tree produced by CoolParser#case_stat.
    def exitCase_stat(self, ctx:CoolParser.Case_statContext):
        pass


    # Enter a parse tree produced by CoolParser#let_decl.
    def enterLet_decl(self, ctx:CoolParser.Let_declContext):
        pass

    # Exit a parse tree produced by CoolParser#let_decl.
    def exitLet_decl(self, ctx:CoolParser.Let_declContext):
        pass



del CoolParser