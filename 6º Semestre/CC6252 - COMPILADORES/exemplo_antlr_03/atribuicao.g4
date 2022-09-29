grammar atribuicao;

//Regra de atribuicao
init: tipo id operador (id|num);

tipo: 'inteiro' | 'decimal' | 'palavra';

operador: '<-';

id: ID;
ID: [a-z]+;

num: NUM;
NUM: [0-9]+;

Ws: [ \t\r\n]+ -> skip;
