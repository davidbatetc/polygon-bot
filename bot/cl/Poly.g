// antlr4 -Dlanguage=Python3 -no-listener -visitor Poly.g
grammar Poly;

root : (COMMENT | stmt)* EOF;
stmt : IDEN ASSIGN poly
     | COLOR IDEN COLON color
     | PRINT (poly | QTEXT)
     | AREA poly
     | PERIM poly
     | VERT poly
     | CENTR poly
     | INSIDE poly COLON poly
     | EQUAL poly COLON poly
     | DRAW QTEXT (COLON poly)*
     | TRANS IDEN COLON NUM NUM
     ;
poly : LSQUARE (NUM NUM)* RSQUARE
     | LPAREN poly RPAREN
     | BOUND poly
     | poly INTER poly
     | poly UNION poly
     | COPY IDEN
     | IDEN
     | REGPOLY NUM COLON NUM COLON NUM NUM COLON NUM
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

// Others
LPAREN : '(';
RPAREN : ')';
LSQUARE : '[';
RSQUARE : ']';
LCURLY : '{';
RCURLY : '}';
COLON : ',';
NUM : ('+' | '-')?([0-9]+ | [0-9]+'.'[0-9]+);
IDEN : [a-zA-Z][a-zA-Z0-9]*;
WS : [ \t\n]+ -> skip;
QTEXT : '"' (~('"'))* '"';
COMMENT : '//' (~('\n' | '\r'))* -> skip;
