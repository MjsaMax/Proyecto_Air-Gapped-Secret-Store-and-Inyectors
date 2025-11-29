#!/usr/bin/env bash
set -euo pipefail

# Pedir ID y Valor
echo "GUARDAR SECRETO NUEVO"
read -p "Introduce el ID del secreto: " SECRET_ID
read -s -p "Introduce el VALOR del secreto: " SECRET_VALUE
echo "" 

# Pedir la Passphrase 
read -s -p "Crea una Passphrase para encriptar este secreto: " PASSPHRASE
echo ""

echo "Guardando en secrets/storage..."

# Llamar al CLI pasando la passphrase con el flag -p
python3 secrets/secrets_cli.py store "$SECRET_ID" "$SECRET_VALUE" -p "$PASSPHRASE"

echo "Listo."