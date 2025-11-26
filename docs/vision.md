# Visión del Proyecto: Air-Gapped Secret Store

## Contexto y Problema
En entornos de alta seguridad u organizaciones "air-gapped" (aisladas de internet), los equipos de desarrollo no pueden depender de servicios de gestión de secretos en la nube (como AWS Secrets Manager o Azure Key Vault).

Actualmente, existe el riesgo de que los desarrolladores:
1. Hardcodeen credenciales en el código fuente.
2. Copien archivos .env inseguros dentro de las imágenes Docker.
3. Expongan secretos en texto plano en sus discos duros.

## Solución Propuesta
Desarrollar una herramienta CLI (Command Line Interface) local en Python llamada `secrets_cli.py` que permita cifrar secretos en reposo y mecanismos seguros en Bash para inyectarlos como variables de entorno en contenedores Docker, sin que estos toquen el disco en texto plano ni dependan de servicios externos.

## Objetivos del Proyecto
* **Técnico:** Implementar cifrado simétrico local para archivos y gestionar su inyección en tiempo de ejecución.
* **Seguridad:** Demostrar prácticas de "Container Hardening" (imágenes sin root, sistemas de archivos de solo lectura).
* **Aprendizaje:** Comprender el ciclo de vida de un secreto y cómo evitar errores comunes como copiar `.env` en el build de Docker.