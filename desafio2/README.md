# Desafio 2: Volumes e Persistência

## 🎯 Objetivo

Mostrar, de forma bem direta, que os dados de um banco rodando em container **não desaparecem** quando
o container é removido, desde que estejam guardados em um **volume Docker**.

## 💡 Solução, Arquitetura e Decisões Técnicas

- Usei a imagem oficial **`postgres:16-alpine`** como banco de dados.
- O serviço `db` é configurado no `docker-compose.yml` com:
  - database: `desafio2`
  - usuário: `desafio2`
  - senha: `desafio2`
- Os dados do Postgres são armazenados em um **volume nomeado** chamado `postgres_data`, montado em
  `/var/lib/postgresql/data`, que é o diretório padrão de dados do Postgres dentro do container.

Isso significa que:

- Se eu parar e remover o container, mas **não deletar o volume**, os arquivos físicos do banco
  continuam guardados no host Docker.
- Ao subir outro container apontando para o mesmo volume, ele encontra o banco com todas as tabelas e dados.

## ⚙️ Passo a passo de funcionamento

1. O `docker-compose.yml` declara um volume nomeado `postgres_data` na seção `volumes:`.
2. O serviço `db` monta esse volume em `/var/lib/postgresql/data`.
3. Na primeira vez que o Postgres sobe, ele inicializa o banco e escreve os arquivos de dados nesse caminho.
4. Quando o container é removido com `docker-compose down`, o volume **não é apagado** por padrão.
5. Se eu subir o serviço `db` novamente, o Postgres encontra os dados e reutiliza tudo que já estava lá.

## ▶️ Como subir o banco

Dentro da pasta `desafio2`:

```bash
docker-compose up -d
```

Isso vai:

- puxar a imagem `postgres:16-alpine` (caso ainda não exista);
- criar o volume `postgres_data`;
- iniciar o container `desafio2_db`.

## 🧪 Como testar a persistência na prática

1. **Subir o banco**

   ```bash
   docker-compose up -d
   ```

2. **Entrar no container**

   ```bash
   docker exec -it desafio2_db psql -U desafio2 -d desafio2
   ```

3. **Criar uma tabela e inserir um dado**

   Dentro do `psql`:

   ```sql
   CREATE TABLE usuarios (
     id SERIAL PRIMARY KEY,
     nome TEXT NOT NULL
   );

   INSERT INTO usuarios (nome) VALUES ('Rennan');
   SELECT * FROM usuarios;
   ```

   Você deve ver pelo menos uma linha com o nome inserido.

4. **Parar e remover o container (sem apagar o volume)**

   ```bash
   docker-compose down
   ```

5. **Subir de novo**

   ```bash
   docker-compose up -d
   ```

6. **Reconectar e verificar se os dados continuam lá**

   ```bash
   docker exec -it desafio2_db psql -U desafio2 -d desafio2
   ```

   E rodar:

   ```sql
   SELECT * FROM usuarios;
   ```

   Se a linha ainda estiver lá, você comprovou a persistência via volume.

## 💣 (Opcional) Apagando tudo, inclusive o volume

Se em algum momento você quiser realmente começar do zero:

```bash
docker-compose down -v
```

O `-v` força a remoção do volume `postgres_data`. Ao subir novamente, o banco será reinicializado em branco.

## 📁 Estrutura de pastas

```text
desafio2/
  docker-compose.yml
  README.md
```

A ideia aqui é que o foco fique no conceito de volume e não em uma aplicação complexa.
