# Visión del Proyecto: Air-Gapped Secret Store & Injectors

## 1. Contexto y Problema
En organizaciones con altos estándares de seguridad o entornos "air-gapped" (aislados físicamente de internet), los equipos de desarrollo enfrentan un dilema crítico: necesitan gestionar secretos (API Keys, contraseñas de BD) para sus aplicaciones contenerizadas, pero **tienen prohibido usar servicios de gestión de secretos en la nube** (como AWS Secrets Manager o HashiCorp Vault cloud).

El problema actual es que, ante la falta de herramientas, los desarrolladores suelen caer en malas prácticas:
* Copiar archivos `.env` inseguros dentro de las imágenes Docker.
* Hardcodear credenciales en el código fuente.
* Dejar secretos en texto plano en el disco.

## 2. Solución Propuesta (Objetivo Técnico)
Desarrollar un sistema **local-first** compuesto por:
1.  **CLI de Secretos (`secrets_cli.py`):** Permite cifrar secretos en disco usando una passphrase, sin que nunca se guarden en texto plano.
2.  **Inyectores Seguros:** Scripts en Bash que descifran el secreto en memoria solo en el momento de ejecutar el contenedor (`docker run`), inyectándolo como variable de entorno sin tocar el disco.
3.  **App de Prueba:** Una aplicación Python contenerizada bajo estándares de "Hardening" (usuario no root) para validar el flujo.

## 3. Alcance y Aprendizaje
Este proyecto funciona como un laboratorio de **DevSecOps** para entender el ciclo de vida de un secreto y cómo aplicar el principio de mínimo privilegio en Docker, evitando fugas de información en entornos restringidos.