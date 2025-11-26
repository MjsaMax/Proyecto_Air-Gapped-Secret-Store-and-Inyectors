# Con targets claros y autosuficientes, por ejemplo:
# • make setup - Preparar entorno local (crear venv, instalar dependencias, etc., si aplica).
# • make dev - Levantar entorno local (Docker/Compose o K8s según proyecto).
# • make build - Construir imagen(es) Docker con tags inmutables (por ejemplo, 
# app:<git_sha>).
# • make test - Ejecutar tests automáticos (unitarios/integación).
# • make scan - Ejecutar SAST/SCA/DAST/IaC scan según el proyecto.
# • make sbom - Generar SBOM (real con syft/trivy o simulado si no se dispone de la 
# herramienta).
# • make k8s-apply / make k8s-clean - Para proyectos con K8s. 										# En estre proyecto no se usa
# • make compose-up / make compose-down - Para proyectos con Docker Compose.
# Regla: nada crítico se ejecuta "a mano" si puede y debe estar en un target de Make + script 
# Bash.
.PHONY: setup dev build test scan 

APP_NAME=app-ejemplo
DOCKERFILE=docker/Dockerfile
TAG=0.0.1
IMAGE=$(APP_NAME):$(TAG)
PYTHON=python3

setup:
	@echo "[+] Preparando entorno local..."
	$(PYTHON) -m venv .venv
	.venv/bin/pip install --upgrade pip
	@if [ -f app/requirements.txt ]; then \
		echo "[+] Instalando dependencias..."; \
		.venv/bin/pip install -r app/requirements.txt; \
	fi
	@echo "[->] setup completado."

build:
	@echo "[+] Construyendo imagen Docker: $(IMAGE)"
	docker build -t $(IMAGE) -f $(DOCKERFILE) .
	@echo "[->] build completado."

dev:
	@echo "[+] Ejecutando entorno de desarrollo..."
	docker run --rm -it -p 5000:5000 -e API_TOKEN="clave-dev" $(IMAGE)
	@echo "[->] dev finalizado."

test:
	@echo "[+] Ejecutando tests..."
	@if [ -x ".venv/bin/pytest" ]; then \
		.venv/bin/pytest -q; \
	else \
		echo "[!] pytest no está instalado. Instálalo usando un venv"; \
	fi
	@echo "[->] test completado."

scan:
	@echo "[+] (Simulado) Ejecutando escaneo de seguridad..."
	@echo "En Desarrollo..."
	@echo "[->] En Desarrollo..."
