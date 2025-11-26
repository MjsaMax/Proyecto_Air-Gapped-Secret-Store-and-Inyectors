# Definition of Done (DoD)

Para que una historia de usuario o tarea técnica se considere "Terminada" (Done), debe cumplir con los siguientes requisitos mínimos:

## 1. Calidad de Código
* [ ] **Comentarios en Español:** Todo el código (Python/Bash) debe estar comentado en español explicando la intención.
* [ ] **Sin "Basura" de IA:** No deben quedar caracteres extraños, bloques de código innecesarios o comentarios generados automáticamente sin revisión.
* [ ] **Linter:** El código Python debe respetar estándares básicos (PEP-8) y no tener errores de sintaxis.

## 2. Funcionalidad y Automatización
*[ ] **Makefile Ejecutable:** Los comandos `make setup`, `make build`, `make test` deben funcionar sin intervención manual.
* [ ] **Pruebas Locales:** La funcionalidad implementada ha sido verificada localmente (ej. el CLI cifra/descifra correctamente).
* [ ] **Sin TODOs Críticos:** No hay tareas pendientes marcadas como "TODO" o "FIXME" que afecten la funcionalidad principal.

## 3. Seguridad
* [ ] **Gestión de Secretos:** NO se han subido archivos `.env` reales, claves privadas o credenciales al repositorio git.
* [ ] **Docker Hardening:** Las imágenes Docker no usan el usuario `root` (deben usar `USER appuser` u otro UID).
* [ ] **Imágenes Base:** Se usan versiones fijas (ej. `python:3.12-slim`) y nunca `:latest`.

## 4. Documentación
* [ ] El archivo `docs/sprint-backlog-sprintX.md` refleja el trabajo realizado.
* [ ] Si hubo cambios de arquitectura, se actualizó el `README.md`.