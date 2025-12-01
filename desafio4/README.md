# Desafio 4: Microsserviços Independentes

## 🎯 Objetivo

Criar dois microsserviços independentes que se falam via HTTP:

- **Microsserviço A**: expõe uma lista de usuários em JSON.
- **Microsserviço B**: consome o A e monta uma mensagem mais "amigável" com essas informações.

Ambos rodam em containers separados, cada um com seu próprio Dockerfile.

## 💡 Solução, Arquitetura e Decisões Técnicas

- **`service_a`**
  - Implementado em Flask.
  - Expõe o endpoint `/users` na porta `5001`.
  - Retorna uma lista fixa de usuários com:
    - `id`
    - `name`
    - `active_since`

- **`service_b`**
  - Também em Flask.
  - Usa a biblioteca `requests` para chamar o `service_a`.
  - Expõe o endpoint `/report` na porta `5002`.
  - Ao ser acessado:
    - chama `http://service_a:5001/users`;
    - recebe o JSON de usuários;
    - monta frases do tipo: `"Usuário X ativo desde Y"`;
    - devolve tudo em um novo JSON.

- **Comunicação**
  - A comunicação entre os serviços é feita via HTTP, usando o nome do serviço no Compose:
    - `service_a:5001`
  - Isso garante o isolamento: se eu mudar a porta ou o host, basta ajustar a URL no serviço B.

- **Containers separados**
  - Cada microsserviço tem seu próprio Dockerfile e seu próprio conjunto de dependências.
  - Isso segue a ideia de **independência** típica de microsserviços.

## ⚙️ Funcionamento geral

1. O Compose sobe os dois serviços na rede `desafio4_net`.
2. `service_a` começa a ouvir em `0.0.0.0:5001` no container (mapeado para `localhost:5001`).
3. `service_b` começa a ouvir em `0.0.0.0:5002` (mapeado para `localhost:5002`).
4. Quando alguém acessa `service_b` em `/report`, ele:
   - faz uma requisição GET para `service_a`;
   - processa o JSON;
   - entrega um resumo mais legível.

## ▶️ Como subir os serviços

Dentro da pasta `desafio4`:

```bash
docker-compose up --build
```

Isso vai construir as imagens dos dois serviços e criar a rede `desafio4_net`.

## 🧪 Como testar

- Testar diretamente o service A:

  ```bash
  curl http://localhost:5001/users
  ```

- Testar o service B (que consome o A):

  ```bash
  curl http://localhost:5002/report
  ```

  A resposta deve ser um JSON com uma mensagem e uma lista de frases descrevendo os usuários.

## 📁 Estrutura de pastas

```text
desafio4/
  docker-compose.yml
  README.md
  service_a/
    Dockerfile
    requirements.txt
    app.py
  service_b/
    Dockerfile
    requirements.txt
    app.py
```

Aqui o foco é mostrar claramente a separação de responsabilidades e a comunicação via HTTP entre serviços.
