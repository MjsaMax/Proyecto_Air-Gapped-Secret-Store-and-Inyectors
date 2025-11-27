#!/usr/bin/env bash
set -euo pipefail

# Configuración 
IMAGE_NAME="app-secret-store:v1"
SECRET_ID="API_TOKEN"

echo "EJECUCIÓN SEGURA DE CONTENEDOR"
echo "-------------------------------------"
echo "El contenedor necesita el secreto con ID: $SECRET_ID"

read -s -p "Introduce tu Passphrase para desbloquear: " PASSPHRASE
echo ""

echo "Desencriptando en memoria..."

# Inyección en Memoria 
DECRYPTED_TOKEN=$(python3 secrets/secrets_cli.py get "$SECRET_ID" -p "$PASSPHRASE")

# Verificamos que no esté vacío 
if [ -z "$DECRYPTED_TOKEN" ]; then
    echo "Error: No se pudo obtener el secreto. Verifica tu passphrase."
    exit 1
fi

echo "Iniciando Docker..."

#  Ejecutar Docker pasando la variable
docker run --rm -p 5000:5000 \
  -e API_TOKEN="$DECRYPTED_TOKEN" \
  "$IMAGE_NAME"