# Backlog del Sprint 1

**Objetivo del Sprint:** Tener las piezas fundamentales listas: la CLI de cifrado funcional y la aplicación "víctima" dockerizada de forma segura.

---

## Historia 1: Infraestructura Base
**ID:** S1-01
**Descripción:** Inicializar la estructura de carpetas y el Makefile estándar.
**Responsable:** (Nombre de tu compañero)
**Criterios de Aceptación:**
- [cite_start]Estructura de carpetas creada (`app/`, `secrets/`, `scripts/`, etc.)[cite: 327].
- `Makefile` funcional con targets `setup`, `dev`, `build`.

---

## Historia 2: CLI de Gestión de Secretos
**ID:** S1-02
[cite_start]**Descripción:** Desarrollar `secrets_cli.py` para gestionar el cifrado de secretos locales[cite: 345].
**Responsable:** (Tu nombre)
**Criterios de Aceptación:**
- El script permite guardar un secreto cifrado en `storage/` mediante una passphrase.
- El script permite listar los IDs de los secretos guardados.
- El script puede descifrar un valor internamente (preparación para inyección).
- Uso de librerías estándar o `cryptography` sin depender de APIs externas.

---

## Historia 3: Aplicación Dummy y Hardening
**ID:** S1-03
[cite_start]**Descripción:** Crear una app Python mínima que consuma el secreto y un Dockerfile seguro[cite: 346, 347].
**Responsable:** (Tu nombre)
**Criterios de Aceptación:**
- La app (`main.py`) valida la existencia de la variable de entorno `API_TOKEN`.
- El Dockerfile usa una imagen base ligera (`python:3.12-slim`).
- El contenedor se ejecuta con un usuario no root (`USER appuser`).
- Existe un `.dockerignore` para excluir archivos innecesarios.