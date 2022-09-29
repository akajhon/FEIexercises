grammar atribuicao;

init: tipo id op (num|id);

tipo: 'inteiro' {System.out.print("int ");} | 'decimal' {System.out.print("double ");} | 'palavra' {System.out.print("String ");};

op: '<-' {System.out.print(" = ");};

id: ID {System.out.print($ID.text);};
ID: [a-z]+;

num: NUM {System.out.print($NUM.text);};
NUM: [0-9]+;

repeticao: 'loop' {System.out.println("for");};

Ws: [\t\r\n ]+ -> skip;
