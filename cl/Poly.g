// antlr4 -Dlanguage=Python3 -no-listener -visitor Poly.g
grammar Poly;

root : (COMMENT | stmt)* EOF;
stmt : IDEN ASSIGN poly
     | COLOR IDEN COMMA color
     | PRINT (poly | QTEXT)
     | AREA poly
     | PERIM poly
     | VERT poly
     | CENTR poly
     | INSIDE poly COMMA poly
     | EQUAL poly COMMA poly
     | DRAW QTEXT (COMMA poly)*
     | TRANS IDEN COMMA NUM NUM
     | ROTATE IDEN COMMA NUM
     | SCALE IDEN COMMA NUM
     ;
poly : LSQUARE (NUM NUM)* RSQUARE
     | LPAREN poly RPAREN
     | BOUND poly
     | poly INTER poly
     | poly UNION poly
     | COPY IDEN
     | IDEN
     | REGPOLY NUM COMMA NUM COMMA NUM NUM COMMA NUM
     | RAND NUM
     ;
color : LCURLY NUM NUM NUM RCURLY;


// Operators
ASSIGN : ':=';
INTER : '*';
UNION : '+';
BOUND : '#';
RAND : '!';

// Commands
COLOR : 'color';
PRINT : 'print';
AREA : 'area';
PERIM : 'perimeter';
VERT : 'vertices';
CENTR : 'centroid';
INSIDE : 'inside';
EQUAL : 'equal';
DRAW : 'draw';
REGPOLY : 'regular';
COPY : 'copy';
TRANS : 'translate';
ROTATE : 'rotate';
SCALE : 'scale';

// Others
LPAREN : '(';
RPAREN : ')';
LSQUARE : '[';
RSQUARE : ']';
LCURLY : '{';
RCURLY : '}';
COMMA : ',';
NUM : ('+' | '-')?([0-9]+ | [0-9]+'.'[0-9]+);
IDEN : [a-zA-Z][a-zA-Z0-9]*;
WS : [ \t\n]+ -> skip;
QTEXT : '"' (~('"'))* '"';
COMMENT : '//' (~('\n' | '\r'))* -> skip;
