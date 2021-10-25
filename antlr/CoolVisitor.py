# Generated from h:\Documentos\Escuela\Diseño de compiladores\Git\proyecto_etapa1y2\proyecto_etapa1y2\antlr\Cool.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CoolParser import CoolParser
else:
    from CoolParser import CoolParser

# This class defines a complete generic visitor for a parse tree produced by CoolParser.

class CoolVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CoolParser#program.
    def visitProgram(self, ctx:CoolParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#klass.
    def visitKlass(self, ctx:CoolParser.KlassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#feature.
    def visitFeature(self, ctx:CoolParser.FeatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#parameter.
    def visitParameter(self, ctx:CoolParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#mult.
    def visitMult(self, ctx:CoolParser.MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#isvoid.
    def visitIsvoid(self, ctx:CoolParser.IsvoidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#lt.
    def visitLt(self, ctx:CoolParser.LtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#String.
    def visitString(self, ctx:CoolParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#while.
    def visitWhile(self, ctx:CoolParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#div.
    def visitDiv(self, ctx:CoolParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#not.
    def visitNot(self, ctx:CoolParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#let.
    def visitLet(self, ctx:CoolParser.LetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#block.
    def visitBlock(self, ctx:CoolParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#ID.
    def visitID(self, ctx:CoolParser.IDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#if.
    def visitIf(self, ctx:CoolParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#case.
    def visitCase(self, ctx:CoolParser.CaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#par.
    def visitPar(self, ctx:CoolParser.ParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#new.
    def visitNew(self, ctx:CoolParser.NewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#simplecall.
    def visitSimplecall(self, ctx:CoolParser.SimplecallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#invert.
    def visitInvert(self, ctx:CoolParser.InvertContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#false.
    def visitFalse(self, ctx:CoolParser.FalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#less.
    def visitLess(self, ctx:CoolParser.LessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#eq.
    def visitEq(self, ctx:CoolParser.EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#int.
    def visitInt(self, ctx:CoolParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#plus.
    def visitPlus(self, ctx:CoolParser.PlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#objectCall.
    def visitObjectCall(self, ctx:CoolParser.ObjectCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#asgn.
    def visitAsgn(self, ctx:CoolParser.AsgnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#true.
    def visitTrue(self, ctx:CoolParser.TrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#le.
    def visitLe(self, ctx:CoolParser.LeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#assign.
    def visitAssign(self, ctx:CoolParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#case_stat.
    def visitCase_stat(self, ctx:CoolParser.Case_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#let_decl.
    def visitLet_decl(self, ctx:CoolParser.Let_declContext):
        return self.visitChildren(ctx)



del CoolParser