#!/usr/bin/env python3
"""
CLI para gestionar secretos en entorno air-gapped.
Maneja almacenamiento cifrado y extracción de secretos como variables de entorno.
"""

import argparse
import json
import os
import sys
import subprocess
from pathlib import Path
from cryptography.fernet import Fernet
from base64 import b64encode, b64decode

# Directorio para almacenar secretos cifrados
STORAGE_DIR = Path(__file__).parent / "storage"
STORAGE_DIR.mkdir(exist_ok=True)

# Archivo de clave maestra (derivada de passphrase)
KEYFILE = STORAGE_DIR / ".key"

def derive_key_from_passphrase(passphrase):
    """Deriva una clave Fernet de 32 bytes a partir de una passphrase."""
    # Usar la passphrase truncado a 32 bytes
    key_bytes = passphrase.encode()
    # Usar base64 para convertir a formato Fernet válido
    key_b64 = b64encode(key_bytes.ljust(32, b'\0')[:32])
    return key_b64

def get_cipher(passphrase):
    """Retorna un objeto Fernet con la clave derivada."""
    key = derive_key_from_passphrase(passphrase)
    return Fernet(key)

def store_secret(secret_id, secret_value, passphrase):
    """Guarda un secreto cifrado."""
    cipher = get_cipher(passphrase)
    encrypted = cipher.encrypt(secret_value.encode())
    
    secret_file = STORAGE_DIR / f"{secret_id}.enc"
    secret_file.write_bytes(encrypted)
    print(f" Secreto '{secret_id}' almacenado.", file=sys.stderr)

def list_secrets(passphrase):
    """Lista todos los IDs de secretos sin mostrar valores."""
    
    secrets = list(STORAGE_DIR.glob("*.enc"))
    print("Secretos disponibles:", file=sys.stderr)
    for secret_file in sorted(secrets):
        secret_id = secret_file.stem
        print(f"  - {secret_id}", file=sys.stderr)

def get_secret(secret_id, passphrase):
    """Extrae un secreto y lo retorna como string."""
    secret_file = STORAGE_DIR / f"{secret_id}.enc"

    try:
        cipher = get_cipher(passphrase)
        encrypted = secret_file.read_bytes()
        decrypted = cipher.decrypt(encrypted).decode()
        return decrypted
    except Exception as e:
        print(f"Password inválido al desencriptar: {e}", file=sys.stderr)
        sys.exit(1)

def run_with_env(secret_id, passphrase, command):
    """Ejecuta un comando con el secreto como variable de entorno."""
    secret_value = get_secret(secret_id, passphrase)
    
    # Crear ambiente hijo con el secreto inyectado
    env = os.environ.copy()
    env[secret_id.upper()] = secret_value
    
    try:
        # Convertir lista a string para bash si es necesario
        cmd_str = " ".join(command)
        result = subprocess.run(cmd_str, env=env, check=False, shell=True)
        sys.exit(result.returncode)
    except Exception as e:
        print(f"Error ejecutando comando: {e}", file=sys.stderr)
        sys.exit(1)
def main():
    parser = argparse.ArgumentParser(description="CLI para gestionar secretos en entorno air-gapped")
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponibles")
    
    # Comando: store
    store_parser = subparsers.add_parser("store", help="Guardar un secreto")
    store_parser.add_argument("id", help="ID del secreto")
    store_parser.add_argument("value", help="Valor del secreto")
    store_parser.add_argument("-p", "--passphrase", help="Passphrase (por defecto: input interactivo)",default=None)
    
    # Comando: list
    list_parser = subparsers.add_parser("list", help="Listar IDs de secretos")
    list_parser.add_argument("-p", "--passphrase",help="Passphrase (no requerida para listar)",default=None)
    
    # Comando: get
    get_parser = subparsers.add_parser("get", help="Obtener un secreto")
    get_parser.add_argument("id", help="ID del secreto")
    get_parser.add_argument("-p", "--passphrase",help="Passphrase (por defecto: input interactivo)",default=None)
    
    # Comando: run
    run_parser = subparsers.add_parser("run", help="Ejecutar comando con secreto inyectado como ENV")
    run_parser.add_argument("id", help="ID del secreto")
    run_parser.add_argument("-p", "--passphrase", help="Passphrase (por defecto: input interactivo)", default=None )
    run_parser.add_argument("run_command", nargs=argparse.REMAINDER, help="Comando a ejecutar")
    args = parser.parse_args()

    # Obtiene passphrase solo si el comando lo necesita
    passphrase = getattr(args, 'passphrase', None)
    if passphrase is None and args.command not in ["list"]:
        import getpass
        passphrase = getpass.getpass("Passphrase: ")
    if args.command == "store":
        store_secret(args.id, args.value, passphrase)
    elif args.command == "list":
        list_secrets(passphrase)
    elif args.command == "get":
        secret = get_secret(args.id, passphrase)
        print(secret)
    elif args.command == "run":
        run_with_env(args.id, passphrase, args.run_command)

if __name__ == "__main__":
    main()
