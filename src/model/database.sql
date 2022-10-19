/* comandos SQL usados no banco de dados "dados.db" */

CREATE TABLE IF NOT EXISTS "pessoas" (
    cpf    TEXT,
    nome   TEXT,
    estado TEXT,
    cidade TEXT,
    PRIMARY KEY(cpf)
);

CREATE INDEX IF NOT EXISTS "cpf_index" ON pessoas (
    "cpf"
);

CREATE INDEX IF NOT EXISTS "nome_index" ON pessoas (
    "nome"
);


/* comandos SQL usados no banco de dados "users.db" */

CREATE TABLE IF NOT EXISTS "owner" (
    token TEXT,
    nome  TEXt,
    email TEXT,
    PRIMARY KEY(token)
);

CREATE INDEX IF NOT EXISTS "token_owner" ON owner(
    "token"
);


CREATE TABLE IF NOT EXISTS "clientes" (
    token      TEXT,
    nome       TEXT,
    email      TEXT,
    created_at TEXt,
    PRIMARY KEY(token)
);

CREATE INDEX IF NOT EXISTS "token_clientes" ON clientes (
    "token"
);
