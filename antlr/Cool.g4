grammar Cool;

program
    : ( klass SEMICOLON ) *
    ;

klass
    : KLASS TYPE ( INHERITS TYPE )? LBRA ( feature SEMICOLON )* RBRA
    ;

feature
    : ID LPAR (formal (COMMA formal )*)? RPAR COLON TYPE LBRA expr RBRA
    | ID COLON TYPE ( ASSIGN expr )?
    ;

formal
    : ID COLON TYPE  #parameter
    ;

expr
    : ID ASSIGN expr #assign
    | ID LPAR(expr (COMMA expr)*)? RPAR                        #simplecall
    | IF expr THEN expr ELSE expr FI                           #if
    | WHILE expr LOOP expr POOL                                #while
    | expr (AT TYPE)? '.' ID LPAR(expr (COMMA expr)*)? RPAR    #objectCall
    | LET let_decl (COMMA let_decl)* IN expr                   #let
    | CASE expr OF ( case_stat )* ESAC                         #case
    | NEW TYPE                                                 #new
    | LBRA (expr SEMICOLON)*RBRA                               #block
    | INTCOMP expr                                             #invert
    | ISVOID expr                                              #isvoid
    | expr op=MULT expr                                        #mult
    | expr op=DIV expr                                         #div
    | expr op=ADD expr                                         #plus
    | expr op=SUB expr                                         #less
    | expr LT expr                                             #lt
    | expr LE expr                                             #le
    | expr EQUAL expr                                          #eq
    | NOT expr                                                 #not
    | ID ASSIGN expr                                           #asgn
    | LPAR expr RPAR                                           #par
    | ID                                                       #ID
    | INTEGER                                                  #int
    | STRING                                                   #String
    | TRUE                                                     #true
    | FALSE                                                    #false
    ;

case_stat
    : ID COLON TYPE CASEASSIGN expr SEMICOLON
    ;

let_decl
    : ID COLON TYPE ( ASSIGN expr )?
    ;

// Letras fragmentadas
fragment A : [aA] ;
fragment C : [cC] ;
fragment D : [dD] ;
fragment E : [eE] ;
fragment F : [fF] ;
fragment H : [hH] ;
fragment I : [iI] ;
fragment L : [lL] ;
fragment N : [nN] ;
fragment O : [oO] ;
fragment P : [pP] ;
fragment R : [rR] ;
fragment S : [sS] ;
fragment T : [tT] ;
fragment V : [vV] ;
fragment W : [wW] ;

// Palabras Reservadas
KLASS : C L A S S ;
FI: F I;
IF: I F;
IN: I N;
INHERITS: I N H E R I T S;
ISVOID: I S V O I D;
LET: L E T;
LOOP: L O O P;
POOL: P O O L;
THEN: T H E N;
ELSE: E L S E;
WHILE: W H I L E;
CASE: C A S E;
ESAC: E S A C;
NEW: N E W;
OF: O F;
NOT: N O T;
TRUE: 'true';
FALSE: 'false';

// Expresiones regulares
TYPE: [A-Z][a-zA-Z_0-9]*;
ID: [a-z_][a-zA-Z0-9_]*;
INTEGER : [0-9]+;
STRING :'"' (('\\'|'\t'|'\r\n'|'\r'|'\n'|'\\"') | ~('\\'|'\t'|'\r'|'\n'|'"'))* '"';

// A ignorar...
COMMENT: LPAR .? '*)' -> skip;
LINE_COMMENT: TWODASHES ~[\r\n]* -> skip;
WHITESPACE: [ \t\n\r\u000c\u000b]+ -> skip;

// Extras...
LPAR: '(';
RPAR: ')';
LBRA: '{';
RBRA: '}';
COMMA: ',';
COLON: ':';
SEMICOLON: ';';
CASEASSIGN: '=>';
MULT: '*';
DIV: '/';
ADD: '+';
SUB: '-';
EQUAL:'=';
TWODASHES: '--';
INTCOMP: '~';
LT:'<';
LE: '<=';
ASSIGN: '<-';
AT:'@';