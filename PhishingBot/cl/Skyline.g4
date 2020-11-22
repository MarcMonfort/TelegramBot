grammar Skyline;
root : statement EOF ;

statement
    : ID ASSIGN expr    # assignStmt
    | expr              # exprStmt
    ; 

expr 
    : '(' expr ')'                      # parenthesis
    | SUB expr                          # mirror
    | <assoc=right> expr op=POW expr    # arithmetic
    | expr op=(MUL|DIV) expr            # arithmetic
    | expr op=(ADD|SUB) expr            # arithmetic
    | (building|city|NUM)               # value
    | ID                                # exprIdent
    ;

city
    : '[' building (',' building)* ']'                  #multiple
    | '{' expr ',' expr ',' expr ',' expr ',' expr '}'  #random
    ;

building
    : '(' expr ',' expr ',' expr ')'
    ;


MUL : '*' ;
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;
POW : '**' ;

ASSIGN : ':=' ;
NUM : [0-9]+ ;
ID  : ('a'..'z'|'A'..'Z') ('a'..'z'|'A'..'Z'|'0'..'9')* ;

WS : [ \n]+ -> skip ;
