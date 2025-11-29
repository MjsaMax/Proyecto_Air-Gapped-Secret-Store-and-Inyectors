#!/usr/bin/env bash

set -euo pipefail

IMAGE="app-secret-store:v1"

echo "============================================================"
echo "  ALERTA: Ejecutando DEMO de MALA PRÁCTICA (Inseguro)  "
echo "============================================================"


echo "[+] Generando archivo de secretos inseguro (.env.BAD)..."
echo "API_TOKEN=SOY_UN_SECRETO_EN_TEXTO_PLANO_12345" > .env.BAD

echo "[!] Contenido visible en disco:"
cat .env.BAD
echo "------------------------------------------------------------"

echo "[+] Levantando contenedor con el secreto expuesto..."
echo "    Prueba acceder a: http://localhost:5000"
echo "    (Presiona Ctrl+C para detener)"

trap 'rm -f .env.BAD; echo "\n[+] Limpieza realizada."' EXIT

docker run --rm \
    --env-file .env.BAD \
    -p 5000:5000 \
    "$IMAGE"