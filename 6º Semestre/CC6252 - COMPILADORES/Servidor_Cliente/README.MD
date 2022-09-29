### CC6270 - SISTEMAS OPERACIONAIS - CENTRO UNIVERSITÁRIO FEI
```bash
  __  __       _______ _    _    _____ ______ _______      ________ _____  
 |  \/  |   /\|__   __| |  | |  / ____|  ____|  __ \ \    / /  ____|  __ \ 
 | \  / |  /  \  | |  | |__| | | (___ | |__  | |__) \ \  / /| |__  | |__) |
 | |\/| | / /\ \ | |  |  __  |  \___ \|  __| |  _  / \ \/ / |  __| |  _  / 
 | |  | |/ ____ \| |  | |  | |  ____) | |____| | \ \  \  /  | |____| | \ \ 
 |_|  |_/_/    \_\_|  |_|  |_| |_____/|______|_|  \_\  \/   |______|_|  \_\
```
***

## 1. Introdução do Projeto📘

O projeto tem por objetivo a implementação de um servidor de cálculos baseado no protocolo UDP e utilizando a linguagem JAVA. O servidor deve ser  capaz de interpretar alguns comandos recebidos através de solicitações via cLiente e ser capaz de responder a essas solicitações corretamente.

***

## 2. Rodando localmente 🏠

Navegue até o diretório do projeto:

```bash
  cd /exercicio-so
```

Compile todos os arquivos .java utilizando o javac:

```bash
   javac *.java
```

Inicie o servidor:

```bash
  java ServidorUDP.java
```

Inicie o Cliente:

```bash
  java ClienteUDP.java
```

***

## 3. O Protocolo criado 👨‍💻

Após a correta conexão entre cliente e servidor, é possível enviar cálculos matemáticos ao servidor através da sintaxe abaixo.É importante ressaltar que todos os comandos devem ser enviado ao servidor em letras minúsculas e sem acentos.

```bash
operacao ':' primeiro_valor ':' segundo_valor ':'
```

As operações matemáticas implementadas foram : 
- [x] Soma

    ```bash
    soma ':' 10 ':' 10 ':'
    ```

- [x] Multiplicação

    ```bash
    multiplicacao ':' 10 ':' 10 ':'
    ```

- [x] Divisão

    ```bash
    divisao ':' 10 ':' 10 ':'
    ```

- [x] Subtração

    ```bash
    subtracao ':' 10 ':' 10 ':'
    ```

- [x] Potência

    ```bash
    potencia ':' 10 ':' 10 ':'
    ```

***

## 4. Autores 🤖

| <img src="https://avatars.githubusercontent.com/u/72151253?v=4" alt="drawing" width="150"/> | <img src="https://avatars.githubusercontent.com/u/69048604?v=4" alt="drawing" width="150"/> | <img src="https://avatars.githubusercontent.com/u/65295232?v=4" alt="drawing" width="150"/> |
|:-------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------:|---------------------------------------------------------------------------------------------|
| [Hugo Linhares Oliveira](https://github.com/hugolinhareso)                                 | [João Pedro Rosa Cezarino](https://github.com/akajhon)                                      | [Vitor Martins Oliveira](https://github.com/vihmar)                                         |
| R.A: 22.120.046-2                                                                           | R.A: 22.120.021-5                                                                           | R.A: 22.120.067-8                                                                       |