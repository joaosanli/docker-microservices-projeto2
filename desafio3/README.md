# Desafio 3: Docker Compose Orquestrando Serviços

## 🎯 Objetivo

Montar uma mini-aplicação com **três serviços** se comunicando via Docker Compose:

- um serviço **web**;
- um serviço de **banco de dados**;
- um serviço de **cache**.

Tudo orquestrado a partir de um único arquivo `docker-compose.yml`.

## 💡 Solução, Arquitetura e Decisões Técnicas

- **Serviço `web`**
  - Implementado em **Python + Flask**.
  - Expõe um endpoint `/` em `8081` (mapeando a porta interna `8080`).
  - Ao ser acessado, o serviço faz uma checagem simples de conectividade com:
    - o Postgres (`db`);
    - o Redis (`cache`).

- **Serviço `db`**
  - Usa a imagem oficial `postgres:16-alpine`.
  - Não expõe portas para fora da rede do Compose (só é acessível pela aplicação `web`).
  - É configurado com:
    - `POSTGRES_DB=desafio3`
    - `POSTGRES_USER=desafio3`
    - `POSTGRES_PASSWORD=desafio3`

- **Serviço `cache`**
  - Usa a imagem `redis:7-alpine`.
  - Fornece um cache simples, acessado pela aplicação `web`.

- **Rede interna**
  - Todos os serviços estão na rede `desafio3_net`, declarada no `docker-compose.yml`.
  - A comunicação é feita usando o nome dos serviços (`db`, `cache`, `web`).

- **Variáveis de ambiente**
  - O serviço `web` recebe:
    - `DATABASE_HOST=db`
    - `CACHE_HOST=cache`
  - Isso facilita trocar as dependências caso os nomes de host mudem.

## ⚙️ Funcionamento do endpoint

O arquivo `web/app.py` expõe um endpoint `/` que:

- tenta abrir uma conexão com o Postgres;
- tenta fazer um `PING` no Redis;
- devolve um JSON com o status de cada um:

```json
{
  "web": "ok",
  "postgres": "ok",
  "redis": "ok"
}
```

Se alguma coisa der errado, o campo correspondente vem como `"erro"`.

## ▶️ Como subir os serviços

Dentro da pasta `desafio3`:

```bash
docker-compose up --build
```

Isso vai:

- construir a imagem do serviço `web`;
- subir os serviços `db` (Postgres) e `cache` (Redis);
- criar a rede `desafio3_net`;
- expor o serviço web em `http://localhost:8081`.

## 🧪 Como testar

- Com tudo rodando, acesse:

  ```bash
  curl http://localhost:8081/
  ```

  ou pelo navegador.

- Você deve ver um JSON indicando o status de cada serviço.

- Para derrubar o ambiente:

  ```bash
  docker-compose down
  ```

## 📁 Estrutura de pastas

```text
desafio3/
  docker-compose.yml
  README.md
  web/
    Dockerfile
    requirements.txt
    app.py
```

Aqui o foco é menos na lógica de negócio e mais em mostrar como o Compose orquestra múltiplos serviços dependentes.
