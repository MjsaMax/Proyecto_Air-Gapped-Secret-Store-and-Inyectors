
##### VIDEO_SPRINT1: https://1drv.ms/f/c/fdb226ef3c2e079a/IgCuxgxCbmM5S4WuBql47mp6AZX8yf1Zn-jdvSnu5aZ04oA?e=ES2OCw
## SPRINT1_SerranoMax

ISSUES REALIZADOS: #1 #2 #9 
### ISSUE #1 Dev makefile
Creación de Estructura de Carpetas.
```bash
.
├── Makefile
├── README.md
├── app
│   ├── main.py
│   └── requirements.txt
├── docker
│   ├── Dockerfile
│   └── README.md
├── docs
│   ├── definition-of-done.md
│   ├── metrics.md
│   ├── risk-register.md
│   ├── sprint-backlog-sprint1.md
│   ├── sprint-backlog-sprint2.md
│   └── vision.md
├── scripts
│   ├── README.md
│   ├── run-bad-example.sh
│   ├── run-with-secret.sh
│   └── store-secret.sh
└── secrets
    ├── secrets_cli.py
    └── storage
        └── SECRETO0.enc

7 directories, 18 files
```
Creación de el Makefile en la raíz con los targets obligatorios: setup, dev, build, test, scan usando variables de entorno. Los puertos asignados son 8080 para el host y 80 para el contenedor. Creación de venv e instalando pytest.
Completado de ISSUE #1.
USO:
``` bash
.PHONY: setup dev build test scan 

APP_NAME=app-ejemplo
DOCKERFILE=docker/Dockerfile
TAG=0.0.1
IMAGE=$(APP_NAME):$(TAG)
PYTHON=python3

setup: # Crea venv e instala requirements.txt
	@echo "[+] Preparando entorno local..." 			
	$(PYTHON) -m venv .venv
	.venv/bin/pip install --upgrade pip
	@if [ -f app/requirements.txt ]; then \
		echo "[+] Instalando dependencias..."; \
		.venv/bin/pip install -r app/requirements.txt; \
	fi
	@echo "[->] setup completado."

build: # Construye el Dockerfile
	@echo "[+] Construyendo imagen Docker: $(IMAGE)"
	docker build -t $(IMAGE) -f $(DOCKERFILE) .
	@echo "[->] build completado."
 
dev:	# Ejecuta en el puerto 8080 del host y 80 del contenedor
	@echo "[+] Ejecutando entorno de desarrollo..."
	docker run --rm -it -p 8080:80 $(IMAGE)
	@echo "[->] dev finalizado."

test:   # Test usando pytest
	@echo "[+] Ejecutando tests..."
	@if [ -x ".venv/bin/pytest" ]; then \
		.venv/bin/pytest -q; \
	else \
		echo "[!] pytest no está instalado. Instálalo usando un venv"; \
	fi
	@echo "[->] test completado."

scan:  # Scaneo en desarrollo
	@echo "[+] (Simulado) Ejecutando escaneo de seguridad..."
	@echo "En Desarrollo..."
	@echo "[->] En Desarrollo..."
```
### ISSUE #2 Secrets cli
Creacion de secrets_cli.py
librerias:

argparse para los argumentos en python
json: Intente usar JSON para la gestión en STORAGE, pero me di cuenta que no debe estar en texto plano
os, sys,subprocess y path: para el manejo de directorios, archivo de storage/ y inyeccion de secretos en entorno de subproceso.
Se realiza una importación interna de getpass para ocultar el texto de password ingresado.
cryptography.fernet: Encontré esa ncriptación simple como solicita la pc.
base64: para la gestion de encriptación en entornos.
Creacion de metodos como get,store, list y getcipher esta con sus descripciones
SE RESUELVE EL ISSUE #2

Para ejecutar la funcionalidad de secretos:
EN secrets/
```bash
python secrets_cli.py store SECRETO0 CONTENIDO_SECRETO              # Para crear un nuevo secreto guardando su contenido y se ingresa un password
python secrets_cli.py list                                          # Listar los secretos en storage/ imprimiendolos
python secrets_cli.py get SECRETO0                                  # Se ingresa el password para obtener el contenido                                                    
python secrets_cli.py run SECRETO0 -- 'bash -c "echo $SECRETO0"'    # Ejecucion de inyeccion de secreto como variable de entorno, solocita el password para mostrarlo.
```
### ISSUE #3 App Dummy y Dockerfile Seguro
**Estado:** Done / En Progreso
**Descripción:** Implementación de la aplicación "víctima" que recibirá el secreto y su empaquetado seguro.

**Archivos creados/modificados:**
1.  `app/main.py`:
    * Script que lee la variable de entorno `API_TOKEN`.
    * Simula una conexión exitosa si el token existe, o falla si no está.
2.  `docker/Dockerfile`:
    * Base: `python:3.12-slim` (Tag inmutable).
    * Seguridad: Creación de usuario `appuser` (UID 1000) para ejecución **non-root**.
    * Optimización: Copia de `requirements.txt` y código fuente en capas separadas.
3.  `.dockerignore`:
    * Exclusión de carpetas `.git`, `__pycache__`, `.venv`, `secrets/storage` y `docs`.

**Validación:**
* `make build` construye la imagen correctamente.
* La imagen ejecutada manualmente muestra que el usuario no es root (`whoami` -> `appuser`).
=======
Historia 2: Aplicación de Prueba (App)

ID: #3

Título: Crear App Python básica con validación de entorno.

Descripción Corta: Implementar una aplicación web ligera (Flask) que valide la inyección de API_TOKEN a través de variables de entorno para simular una conexión exitosa.

Criterios de Aceptación:
1. La app expone un endpoint /health que responde 200 OK.
2. La ruta principal / valida la existencia de os.getenv('API_TOKEN').
3. El make dev finaliza con la app en estado funcional.

Responsable(s): Poma Walter

Historia 3: Infraestructura Segura (Docker)

ID: #3

Título: Dockerfile endurecido y Makefile.

Descripción Corta: Crear la imagen Docker con el máximo nivel de seguridad posible y optimizar el proceso de construcción.

Criterios de Aceptación:
1. El Dockerfile utiliza python:3.12-slim.
2. El contenedor se ejecuta con un usuario no privilegiado (appuser / UID > 0).
3. El Makefile incluye los targets build y dev.

Responsable(s): Poma Walter

