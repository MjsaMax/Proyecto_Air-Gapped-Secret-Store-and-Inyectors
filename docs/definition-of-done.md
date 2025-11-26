# Definition of Done (DoD)

Para que una historia o tarea se considere "Terminada" (Done), debe cumplir con los siguientes requisitos:

## Calidad de Código
- [ ] El código Python cumple con PEP-8 (en la medida de lo posible).
- [ ] [cite_start]Los scripts de Bash tienen `set -euo pipefail` al inicio[cite: 76].
- [ ] [cite_start]**Importante:** Todos los comentarios explicativos en el código están en **español**[cite: 167].
- [ ] [cite_start]No hay caracteres extraños ni marcas de generación automática por IA en el código o documentación[cite: 168].

## Funcionalidad y Pruebas
- [ ] [cite_start]Los targets del `Makefile` asociados funcionan sin intervención manual[cite: 41].
- [ ] Si aplica, se han realizado pruebas manuales locales (`make test` o ejecución directa).
- [ ] [cite_start]No existen "TODO" críticos pendientes en el código entregado[cite: 42].

## Seguridad
- [ ] [cite_start]No se han subido archivos `.env` ni credenciales reales al repositorio (verificar `.gitignore`)[cite: 176].
- [ ] [cite_start]Las imágenes Docker no usan el tag `:latest`, sino versiones específicas o hash[cite: 181].
- [ ] [cite_start]El contenedor final no corre como `root`[cite: 84].

## Documentación
- [ ] La documentación en `docs/` está actualizada con los cambios del Sprint.