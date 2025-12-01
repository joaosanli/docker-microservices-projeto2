#!/bin/sh

echo "Cliente iniciado. Vou começar a chamar o servidor a cada 5 segundos..."
while true; do
  echo "------------------------------------------"
  echo "[CLIENTE] Fazendo requisição para http://server:8080 ..."
  curl -s http://server:8080 || echo "Falha ao conectar no servidor."
  echo
  sleep 5
done
