from ast import walk
from antlr4 import *
from antlr4.error.Errors import InputMismatchException
from antlr4.PredictionContext import combineCommonParents

from antlr4.tree.Tree import ParseTreeWalker
from ANTLRListeners.JavaLexer import JavaLexer
from ANTLRListeners.JavaParser import JavaParser
from ANTLRListeners.JavaParserListener import JavaParserListener


class AttributesListener(JavaParserListener):
    inClass = False
    inMethod = False

    def enterVariableDeclaratorId(self, ctx: JavaParser.VariableDeclaratorIdContext):
        if self.inClass and self.inMethod:
            # atributo
            print("Variable dentro de un metodo: " + str(ctx.IDENTIFIER()))
        if self.inClass and self.inMethod == False:
            print("Variable fuera de un metodo: " + str(ctx.IDENTIFIER()))
    
    def enterClassDeclaration(self, ctx: JavaParser.ClassDeclarationContext):
        self.inClass = True

    def exitClassDeclaration(self, ctx: JavaParser.ClassDeclarationContext):
        self.inClass = False

    def enterMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext):
        self.inMethod = True

    def exitMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext):
        self.inMethod = False



def main(file):
    parser = JavaParser(CommonTokenStream(JavaLexer(FileStream(file))))
    tree = parser.compilationUnit()
    listener1 = AttributesListener()

    walker = ParseTreeWalker()
    walker.walk(listener1, tree)

if __name__ == '__main__':
    main("Prueba.java")
