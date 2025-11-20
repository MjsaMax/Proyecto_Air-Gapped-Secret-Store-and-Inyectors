# Con targets claros y autosuficientes, por ejemplo:
# • make setup - Preparar entorno local (crear venv, instalar dependencias, etc., si aplica).
# • make dev - Levantar entorno local (Docker/Compose o K8s según proyecto).
# • make build - Construir imagen(es) Docker con tags inmutables (por ejemplo, 
# app:<git_sha>).
# • make test - Ejecutar tests automáticos (unitarios/integación).
# • make scan - Ejecutar SAST/SCA/DAST/IaC scan según el proyecto.
# • make sbom - Generar SBOM (real con syft/trivy o simulado si no se dispone de la 
# herramienta).
# • make k8s-apply / make k8s-clean - Para proyectos con K8s.
# • make compose-up / make compose-down - Para proyectos con Docker Compose.
# Regla: nada crítico se ejecuta "a mano" si puede y debe estar en un target de Make + script 
# Bash.
