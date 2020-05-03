grammar Skyline;
root : statement EOF ;

statement
    : ID ASSIGN expr    # assignStmt
    | expr              # nana
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
    : '[' building (',' building)* ']'              #multiple
    | '{' expr ',' expr ',' expr ',' expr ',' expr '}'   #random
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
/* //SINGLE : '(' NUM ',' NUM ',' NUM ')' ;
MULTIPLE : '['SINGLE (',' SINGLE)* ']' ;
RANDOM : '{' NUM ',' NUM ',' NUM ',' NUM ',' NUM '}' ; */

ID  : ('a'..'z'|'A'..'Z'|'_') ('a'..'z'|'A'..'Z'|'_'|'0'..'9')* ;


WS : [ \n]+ -> skip ;
