# Docker & Microsserviços — Projeto 2

Implementação completa dos cinco desafios práticos da disciplina de **Fundamentos de Computação Concorrente, Paralela e Distribuída**, aplicando conceitos essenciais de conteinerização, redes Docker, persistência, orquestração e comunicação entre microsserviços.

O objetivo principal é demonstrar, de forma modular e explicada, como componentes distribuídos podem ser construídos, isolados e integrados utilizando Docker e Docker Compose.

---

## 📌 Visão Geral do Projeto

O repositório é dividido em cinco módulos independentes, cada um representando um aspecto fundamental da arquitetura baseada em serviços:

| Módulo | Conceito central | Portas utilizadas | Tecnologias principais |
|--------|------------------|------------------|------------------------|
| **Desafio 1 – Conectividade** | Redes Docker, isolamento e descoberta de serviços | 8080 | Flask, Alpine, curl |
| **Desafio 2 – Persistência** | Volumes e durabilidade de dados | 5432 | PostgreSQL |
| **Desafio 3 – Orquestração** | Multi-serviços e dependências com Compose | 8081, 5432, 6379 | Flask, PostgreSQL, Redis |
| **Desafio 4 – Comunicação entre Serviços** | Microsserviços independentes via HTTP | 5001, 5002 | Flask, Python |
| **Desafio 5 – API Gateway** | Camada centralizada de acesso | 8000 | Flask, Python |

Cada módulo possui:
- Dockerfiles próprios  
- docker-compose.yml (quando aplicável)  
- README interno com descrição, arquitetura e instruções de execução  

---

## 🧰 Pré-requisitos

Para executar qualquer módulo, você precisa:

- **Docker Desktop** (Windows/macOS/Linux)  
- **Docker Engine ≥ 20.10**  
- **Docker Compose ≥ 2.0**

### ✔ Como instalar Docker no Windows

1. Baixe o instalador:  
   👉 https://www.docker.com/products/docker-desktop  
2. Instale normalmente.  
3. Teste no terminal:

```bash
docker --version
docker compose version
docker run hello-world
```

Se o último comando imprimir a mensagem de boas-vindas, o ambiente está ok.

---

## 🧭 Comandos Essenciais (usados em todos os desafios)

| Objetivo | Comando | Descrição |
|----------|---------|-----------|
| Subir projeto e reconstruir imagens | `docker compose up --build` | Recria containers e dependências |
| Rodar em background | `docker compose up -d --build` | Modo “detached” |
| Acompanhar logs | `docker compose logs -f` | Atualização contínua |
| Parar containers | `docker compose down` | Remove containers e rede |
| Parar e apagar volumes (⚠️ apaga dados!) | `docker compose down -v` | Útil para reinício completo |
| Listar containers ativos | `docker ps` | Diagnóstico |
| Listar imagens | `docker images` | Limpeza e manutenção |

---

## 📚 Descrição dos Módulos

### **🧩 Desafio 1 — Conectividade e Comunicação**

Demonstra a criação de uma **rede Docker personalizada** para permitir interação direta entre containers.
- Servidor Flask respondendo em `/`
- Cliente baseado em Alpine executando chamadas HTTP periódicas para o servidor
- Simula descoberta de serviços e comunicação interna

---

### **🗄️ Desafio 2 — Persistência com Volumes**

Mostra como containers podem manter estado mesmo após serem destruídos.
- Ambiente PostgreSQL
- Volume nomeado armazenando dados
- Script SQL de inicialização
- Demonstração prática: parar / remover container → dados continuam

---

### **🔧 Desafio 3 — Orquestração com Docker Compose**

Stack completa com três serviços:
- Web (Flask)
- Banco (PostgreSQL)
- Cache (Redis)

Inclui:
- Variáveis de ambiente
- Rede interna própria
- Dependências via `depends_on`
- Endpoint de health check verificando conectividade com DB e Redis

---

### **🔗 Desafio 4 — Microsserviços Independentes**

Dois serviços isolados:
- `service_a` → fornece `/users`
- `service_b` → consome `/users` e gera `/report`

Aborda:
- Comunicação inter-serviço
- Independência de deploy
- Interface clara via HTTP

---

### **🚪 Desafio 5 — API Gateway**

Implementação de um ponto único de acesso:
- `GET /users` → encaminhado para microsserviço de usuários  
- `GET /orders` → encaminhado para microsserviço de pedidos  

O gateway realiza:
- Roteamento  
- Tratamento de falhas  
- Integração horizontal entre serviços  

É uma simulação direta de arquiteturas reais com gateway API.

---

## ▶️ Execução Geral

Cada módulo pode ser executado individualmente:

```bash
cd desafioX
docker compose up --build
```

O README interno explica:
- fluxo da aplicação  
- portas expostas  
- endpoints e exemplos  

---

## 🩺 Diagnóstico e Solução de Problemas

### 🔍 Serviço não responde
- Verifique se o **Docker Desktop está ativo**
- Verifique se a porta está ocupada:
  ```bash
  netstat -ano | findstr :8080
  ```
- Tente reconstruir tudo:
  ```bash
  docker compose up --build
  ```

### 🔍 Containers não se comunicam
- Confira se estão na **mesma rede** definida no Compose
- Teste a conexão interna:
  ```bash
  docker exec -it nome_do_container ping service_name
  ```

### 🔍 Volume não persiste dados
- Evite usar `docker compose down -v`  
- Ele apaga os volumes — e com eles, os dados

---

## 🗂 Estrutura Geral do Repositório

```
desafio1/
desafio2/
desafio3/
desafio4/
desafio5/
README.md
```

Cada módulo possui seu próprio ambiente e instruções.

---

## ✨ Considerações Finais

Este projeto demonstra, de forma progressiva e modular:

- Criação e isolamento de containers  
- Comunicação interna via redes Docker  
- Persistência real usando volumes  
- Orquestração completa com Compose  
- Padrões de microsserviços  
- Implementação de API Gateway  

É um guia prático para quem deseja entender como componentes distribuídos funcionam na prática utilizando Docker.
