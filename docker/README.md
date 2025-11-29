<!-- • Dockerfiles: -->
<!-- o Usar imágenes base mínimas y fijas (python:3.12-slim, alpine, distroless, etc.;  -->
<!-- no usar latest). -->
<!-- o Preferencia por multi-stage builds donde tenga sentido (build -> runtime  -->
<!-- mínimo). -->
<!-- o Uso obligatorio de: -->
<!-- § USER no root en la imagen final. -->
<!-- § .dockerignore para excluir .git/, __pycache__/, *.pyc, .env, docs/,  -->
<!-- reports/, etc. -->
<!-- o Evitar dejar herramientas de build (gcc, curl, etc.) en la imagen final cuando no  -->
<!-- sean necesarias. -->
<!-- • docker-compose.yml (si aplica): -->
<!-- o Uso de networks para aislar servicios (frontend/backend/db, etc.). -->
<!-- o mem_limit, cpus, restart: configurados. -->
<!-- o Uso de .env para variables, con: -->
<!-- § compose/.env.example en el repositorio. -->
<!-- § .env real no se sube (añadirlo a .gitignore). -->

<!--  -->
<!-- 3.4. Kubernetes (si el proyecto lo requiere) -->
<!-- • Manifiestos en k8s/: -->
<!-- o namespace.yaml (cuando aplique). -->
<!-- o deployment*.yaml, service*.yaml, configmap.yaml, secret.yaml,  -->
<!-- networkpolicy.yaml, ingress.yaml, rbac.yaml, etc. según el proyecto. -->
<!-- • Buenas prácticas: -->
<!-- o securityContext (runAsNonRoot, readOnlyRootFilesystem, capabilities.drop,  -->
<!-- etc.). -->
<!-- o resources.requests y resources.limits. -->
<!-- o No usar image: ...:latest. -->
<!-- o ServiceAccount específico (no usar default) cuando el proyecto lo pide. -->
<!-- o NetworkPolicies cuando el proyecto lo exige (zero-trust, aislamiento, etc.). -->
