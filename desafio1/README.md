# Desafio 1: Containers em Rede

## 🎯 Objetivo

Criar dois containers que consigam conversar entre si por meio de uma **rede Docker customizada**.

- Um container roda um **servidor web** simples.
- Outro container faz **requisições periódicas** para esse servidor.

## 💡 Solução, Arquitetura e Decisões Técnicas

- **Servidor (`server`)**
  - Implementado em **Python + Flask**.
  - Exposto na porta **8080** dentro do container.
  - Responde em `/` com um JSON contendo:
    - mensagem de texto;
    - timestamp da requisição;
    - nome do container.

- **Cliente (`client`)**
  - Baseado em uma imagem **Alpine Linux** bem enxuta.
  - Usa `curl` em um script `ping.sh` que entra em loop e faz requisições HTTP a cada 5 segundos.
  - Enxerga o servidor pelo hostname **`server`**, graças à rede Docker configurada no `docker-compose.yml`.

- **Rede Docker**
  - Definida como `desafio1_net` no `docker-compose.yml`.
  - É uma rede do tipo `bridge`, interna ao Compose.
  - Permite que os containers se resolvam pelo nome do serviço.

## ⚙️ Como funciona na prática

1. O `docker-compose` cria a rede `desafio1_net`.
2. O serviço `server` é construído a partir do Dockerfile em `./server` e passa a escutar em `0.0.0.0:8080`.
3. O serviço `client` é construído a partir do Dockerfile em `./client`.
4. Quando o `client` inicia, ele executa o script `ping.sh`, que:
   - imprime uma mensagem no console;
   - chama `curl http://server:8080`;
   - espera 5 segundos;
   - repete o processo indefinidamente.

O importante aqui é perceber que **não uso IP fixo**: o cliente fala com o servidor usando o *nome lógico* `server`, que é exatamente o nome do serviço no Compose.

## ▶️ Como subir o desafio

No diretório `desafio1`:

```bash
docker-compose up --build
```

Isso vai:

- construir as imagens `desafio1_server` e `desafio1_client`;
- criar a rede `desafio1_net`;
- subir os dois containers.

## 🧪 Como testar

- Abra um terminal e suba o projeto com:

  ```bash
  docker-compose up --build
  ```

- Você deve ver no log algo como:

  - O servidor Flask inicializando.
  - O cliente escrevendo periodicamente mensagens do tipo:

    ```
    [CLIENTE] Fazendo requisição para http://server:8080 ...
    {"message": "...", "timestamp": "...", "container": "..."}
    ```

- Se quiser testar diretamente o servidor, basta acessar no navegador:

  - `http://localhost:8080`

## 📁 Estrutura de pastas

```text
desafio1/
  docker-compose.yml
  README.md
  server/
    Dockerfile
    requirements.txt
    app.py
  client/
    Dockerfile
    ping.sh
```

Essa estrutura ajuda a manter as responsabilidades bem separadas: a aplicação do servidor fica isolada da lógica do cliente.
