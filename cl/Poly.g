// antlr4 -Dlanguage=Python3 -no-listener -visitor Poly.g
grammar Poly;

root : (cmt | stmt)* EOF;
cmt : COMMENT;
stmt : IDEN ASSIGN poly
     | COLOR poly COLON color
     | PRINT (poly | QTEXT)
     | AREA poly
     | PERIM poly
     | VERT poly
     | CENTR poly
     | INSIDE poly COLON poly
     | EQUAL poly COLON poly
     | DRAW QTEXT (COLON poly)*
     ;
poly : LSQUARE (FLOAT FLOAT)* RSQUARE
     | BOUND poly
     | poly INTER poly
     | poly UNION poly
     | IDEN
     | RAND FLOAT
     ;
color : LCURLY FLOAT FLOAT FLOAT RCURLY;


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

// Others
LCURLY : '{';
RCURLY : '}';
LSQUARE : '[';
RSQUARE : ']';
COLON : ',';
FLOAT : [0-9]+ | [0-9]+'.'[0-9]+;
IDEN : [a-zA-Z][a-zA-Z0-9]*;
WS : [ \t\n]+ -> skip;
QTEXT : '"' (~('"'))* '"';
COMMENT : '//' (~('\n' | '\r'))* -> skip;
