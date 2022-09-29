grammar atribuicao;

init: comando;

comando: tipo ID '=' (ID|NUM);

tipo: 'inteiro' | 'real' | 'boolean';

ID: [a-z]+;
NUM: [0-9]+(.[0-9]+)?;

Ws: [\t\r\n ]+ -> skip;
