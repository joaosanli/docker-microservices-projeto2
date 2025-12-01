# Desafio 5: Microsserviços com API Gateway

## 🎯 Objetivo

Construir uma arquitetura com:

- dois microsserviços de dados (`users` e `orders`);
- um **API Gateway** que centraliza o acesso e expõe endpoints únicos para o mundo externo.

Tudo rodando em containers, orquestrado por **Docker Compose**.

## 💡 Solução, Arquitetura e Decisões Técnicas

- **Microsserviço `users`**
  - Flask simples retornando uma lista de usuários em `/users`.
  - Porta interna `5001`.

- **Microsserviço `orders`**
  - Outro Flask retornando uma lista de pedidos em `/orders`.
  - Porta interna `5003`.

- **Gateway**
  - Implementado em Flask para manter a stack simples e homogênea.
  - Porta interna `8000` (mapeada para `localhost:8000`).
  - Expõe:
    - `GET /users` → repassa a requisição para o serviço `users`.
    - `GET /orders` → repassa a requisição para o serviço `orders`.
  - Em caso de erro na chamada a algum serviço, retorna um JSON com mensagem de erro e status `502`.

- **Orquestração com Docker Compose**
  - O arquivo `docker-compose.yml` sobe os três serviços na rede `desafio5_net`.
  - O gateway depende de `users` e `orders` (`depends_on`).

- **Rede**
  - Todos os serviços estão na mesma rede interna `desafio5_net`.
  - O gateway acessa os serviços pelos nomes:
    - `users:5001`
    - `orders:5003`

## ⚙️ Fluxo das requisições

1. O cliente (navegador, curl, etc.) chama o gateway:
   - `GET http://localhost:8000/users`
   - `GET http://localhost:8000/orders`
2. O gateway recebe a requisição e faz um `GET` interno:
   - para `users:5001/users`, ou
   - para `orders:5003/orders`.
3. O gateway apenas repassa o JSON recebido do microsserviço de origem.
4. Se algo der errado (timeout, serviço fora do ar, etc.), o gateway devolve um JSON de erro.

## ▶️ Como subir a arquitetura

Dentro da pasta `desafio5`:

```bash
docker-compose up --build
```

Isso vai:

- construir as imagens de `gateway`, `users` e `orders`;
- criar a rede `desafio5_net`;
- expor o gateway em `http://localhost:8000`.

## 🧪 Como testar

- Listar usuários via gateway:

  ```bash
  curl http://localhost:8000/users
  ```

- Listar pedidos via gateway:

  ```bash
  curl http://localhost:8000/orders
  ```

Em ambos os casos, a resposta vem do microsserviço correspondente, mas **passa sempre pelo gateway**.

## 📁 Estrutura de pastas

```text
desafio5/
  docker-compose.yml
  README.md
  gateway/
    Dockerfile
    requirements.txt
    app.py
  users/
    Dockerfile
    requirements.txt
    app.py
  orders/
    Dockerfile
    requirements.txt
    app.py
```

O ponto principal aqui é mostrar o padrão de API Gateway: um único ponto de entrada, vários serviços por trás.
