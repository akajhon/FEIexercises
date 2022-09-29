CREATE TABLE public.lavanderia (
    func_quant integer NOT NULL,
    usuario_id integer NOT NULL,
    cnpj varchar(50) NOT NULL
);

CREATE INDEX ON public.lavanderia
    (usuario_id);
CREATE INDEX ON public.lavanderia
    (cnpj);


CREATE TABLE public.cadastro_cliente (
    cpf varchar(20) NOT NULL,
    rg varchar(20) NOT NULL,
    nome varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    cep varchar(10) NOT NULL,
    rua varchar(100) NOT NULL,
    cidade varchar(100) NOT NULL,
    numero integer NOT NULL,
    bairro varchar(100) NOT NULL,
    estado varchar(100) NOT NULL,
    cartao_numero varchar(255) NOT NULL,
    PRIMARY KEY (cpf)
);

CREATE INDEX ON public.cadastro_cliente
    (cartao_numero);


CREATE TABLE public.cadastro_lavanderia (
    cnpj varchar(50) NOT NULL,
    email varchar(255) NOT NULL,
    horario time without time zone NOT NULL,
    nome varchar(255) NOT NULL,
    rua varchar(100) NOT NULL,
    cidade varchar(100) NOT NULL,
    numero integer NOT NULL,
    bairro varchar(100) NOT NULL,
    estado varchar(100) NOT NULL,
    conta varchar(20) NOT NULL,
    PRIMARY KEY (cnpj)
);

CREATE INDEX ON public.cadastro_lavanderia
    (conta);


CREATE TABLE public.usuario (
    usuario_id integer NOT NULL,
    PRIMARY KEY (usuario_id)
);


CREATE TABLE public.dados_bancarios_lavanderia (
    banco varchar(10) NOT NULL,
    agencia varchar(10) NOT NULL,
    conta varchar(20) NOT NULL,
    PRIMARY KEY (conta)
);


CREATE TABLE public.lavagem (
    id_lavagem integer NOT NULL,
    valor real NOT NULL,
    objeto varchar(255) NOT NULL,
    lavanderia_nome varchar(255) NOT NULL,
    PRIMARY KEY (id_lavagem)
);


CREATE TABLE public.cliente (
    usuario_id integer NOT NULL,
    quant_pedidos integer NOT NULL,
    cpf varchar(20) NOT NULL
);

CREATE INDEX ON public.cliente
    (usuario_id);
CREATE INDEX ON public.cliente
    (cpf);


CREATE TABLE public.agendamento (
    id_lavagem integer NOT NULL,
    data date NOT NULL,
    horario time without time zone NOT NULL
);

CREATE INDEX ON public.agendamento
    (id_lavagem);


CREATE TABLE public.entregador (
    usuario_id integer NOT NULL,
    entregas_quant integer NOT NULL,
    cnh varchar(20) NOT NULL
);

CREATE INDEX ON public.entregador
    (usuario_id);
CREATE INDEX ON public.entregador
    (cnh);


CREATE TABLE public.telefone_cadastro_cliente (
    telefone varchar(20) NOT NULL,
    cpf_cliente varchar(20) NOT NULL
);

CREATE INDEX ON public.telefone_cadastro_cliente
    (cpf_cliente);


CREATE TABLE public.cadastro_entregador (
    nome varchar(255) NOT NULL,
    cnh varchar(20) NOT NULL,
    veiculo varchar(255) NOT NULL,
    PRIMARY KEY (cnh)
);


CREATE TABLE public.telefone_cadastro_entregador (
    cnh varchar(20) NOT NULL,
    telefone varchar(20) NOT NULL
);

CREATE INDEX ON public.telefone_cadastro_entregador
    (cnh);


CREATE TABLE public.telefone_cadastro_lavanderia (
    cnpj varchar(50) NOT NULL,
    telefone varchar(20) NOT NULL
);

CREATE INDEX ON public.telefone_cadastro_lavanderia
    (cnpj);


CREATE TABLE public.dados_bancarios_cliente (
    cartao_nome varchar(255) NOT NULL,
    cartao_numero varchar(20) NOT NULL,
    validade date NOT NULL,
    cvv integer NOT NULL,
    PRIMARY KEY (cartao_numero)
);


CREATE TABLE public.lavanderia_lavagem (
    id_lavagem integer NOT NULL,
    id_usuario_lavanderia integer NOT NULL
);

CREATE INDEX ON public.lavanderia_lavagem
    (id_lavagem);
CREATE INDEX ON public.lavanderia_lavagem
    (id_usuario_lavanderia);


CREATE TABLE public.entregador_lavagem (
    id_usuario_entregador integer NOT NULL,
    id_lavagem integer NOT NULL,
    entrega_tipo varchar(255) NOT NULL
);

CREATE INDEX ON public.entregador_lavagem
    (id_usuario_entregador);
CREATE INDEX ON public.entregador_lavagem
    (id_lavagem);


CREATE TABLE public.cliente_lavagem (
    id_usuario_cliente integer NOT NULL,
    id_lavagem integer NOT NULL
);

CREATE INDEX ON public.cliente_lavagem
    (id_usuario_cliente);
CREATE INDEX ON public.cliente_lavagem
    (id_lavagem);


ALTER TABLE public.lavanderia ADD CONSTRAINT FK_lavanderia__usuario_id FOREIGN KEY (usuario_id) REFERENCES public.usuario(usuario_id);
ALTER TABLE public.lavanderia ADD CONSTRAINT FK_lavanderia__cnpj FOREIGN KEY (cnpj) REFERENCES public.cadastro_lavanderia(cnpj);
ALTER TABLE public.cadastro_cliente ADD CONSTRAINT FK_cadastro_cliente__cartao_numero FOREIGN KEY (cartao_numero) REFERENCES public.dados_bancarios_cliente(cartao_numero);
ALTER TABLE public.cadastro_lavanderia ADD CONSTRAINT FK_cadastro_lavanderia__conta FOREIGN KEY (conta) REFERENCES public.dados_bancarios_lavanderia(conta);
ALTER TABLE public.cliente ADD CONSTRAINT FK_cliente__usuario_id FOREIGN KEY (usuario_id) REFERENCES public.usuario(usuario_id);
ALTER TABLE public.cliente ADD CONSTRAINT FK_cliente__cpf FOREIGN KEY (cpf) REFERENCES public.cadastro_cliente(cpf);
ALTER TABLE public.agendamento ADD CONSTRAINT FK_agendamento__id_lavagem FOREIGN KEY (id_lavagem) REFERENCES public.lavagem(id_lavagem);
ALTER TABLE public.entregador ADD CONSTRAINT FK_entregador__usuario_id FOREIGN KEY (usuario_id) REFERENCES public.usuario(usuario_id);
ALTER TABLE public.entregador ADD CONSTRAINT FK_entregador__cnh FOREIGN KEY (cnh) REFERENCES public.cadastro_entregador(cnh);
ALTER TABLE public.telefone_cadastro_cliente ADD CONSTRAINT FK_telefone_cadastro_cliente__cpf_cliente FOREIGN KEY (cpf_cliente) REFERENCES public.cadastro_cliente(cpf);
ALTER TABLE public.telefone_cadastro_entregador ADD CONSTRAINT FK_telefone_cadastro_entregador__cnh FOREIGN KEY (cnh) REFERENCES public.cadastro_entregador(cnh);
ALTER TABLE public.telefone_cadastro_lavanderia ADD CONSTRAINT FK_telefone_cadastro_lavanderia__cnpj FOREIGN KEY (cnpj) REFERENCES public.cadastro_lavanderia(cnpj);
ALTER TABLE public.lavanderia_lavagem ADD CONSTRAINT FK_lavanderia_lavagem__id_lavagem FOREIGN KEY (id_lavagem) REFERENCES public.lavagem(id_lavagem);
ALTER TABLE public.lavanderia_lavagem ADD CONSTRAINT FK_lavanderia_lavagem__id_usuario_lavanderia FOREIGN KEY (id_usuario_lavanderia) REFERENCES public.usuario(usuario_id);
ALTER TABLE public.entregador_lavagem ADD CONSTRAINT FK_entregador_lavagem__id_usuario_entregador FOREIGN KEY (id_usuario_entregador) REFERENCES public.usuario(usuario_id);
ALTER TABLE public.entregador_lavagem ADD CONSTRAINT FK_entregador_lavagem__id_lavagem FOREIGN KEY (id_lavagem) REFERENCES public.lavagem(id_lavagem);
ALTER TABLE public.cliente_lavagem ADD CONSTRAINT FK_cliente_lavagem__id_usuario_cliente FOREIGN KEY (id_usuario_cliente) REFERENCES public.usuario(usuario_id);
ALTER TABLE public.cliente_lavagem ADD CONSTRAINT FK_cliente_lavagem__id_lavagem FOREIGN KEY (id_lavagem) REFERENCES public.lavagem(id_lavagem);

