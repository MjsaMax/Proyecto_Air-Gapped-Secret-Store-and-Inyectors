<!-- 1. Tablero Kanban (obligatorio, por proyecto) -->
<!-- Cada equipo debe trabajar con un tablero Kanban en GitHub Projects (u otra herramienta  -->
<!-- equivalente, pero se recomienda GitHub Projects para integrar con issues y PRs). -->
<!-- Columnas mínimas -->
<!-- El tablero debe tener, como mínimo, estas columnas: -->
<!-- • Backlog - Ideas / historias aún no preparadas. -->
<!-- • Ready - Historias/tareas listas para empezar (con criterio de aceptación claro). -->
<!-- • In Progress - Tareas en desarrollo. -->
<!-- • Code Review - PRs abiertas o tareas listas para revisión de código. -->
<!-- • Testing - Tareas en fase de pruebas (unitarias, integración, seguridad, etc.). -->
<!-- • Done - Tareas completamente terminadas según la Definition of Done. -->
<!-- Uso esperado -->
<!-- • Cada historia/tarea debe estar representada como un issue o tarjeta. -->
<!-- • Debe moverse entre columnas a medida que avanza el trabajo. -->
<!-- • Se espera que a lo largo de los 10 días se vea la evolución real del flujo (no llenar todo  -->
<!-- al final). -->
Proyecto 3 : Air Gapped Secret Store and Inyectors
Tablero de kanban:

Proyecto enfocado en el uso de secretos e inyecciön de estos en un contenedor.

FLUJO BÁSICO DE EJECUCIÓN:

git clone https://github.com/MjsaMax/Proyecto_Air-Gapped-Secret-Store-and-Inyectors -> make setup ->
-> make build -> source .venv/bin/activate -> make dev -> Ingresar en navegador http://127.0.0.1:5000

EL CONTENIDO DEBE SER: Conexión exitosa al servicio interno simulado. Token recibido.


Otros comandos útiles:

setup   - Crear entorno virtual e instalar dependencias"
build   - Construir la imagen Docker $(IMAGE)"
dev     - Ejecutar el contenedor de desarrollo localmente"
store-secret - Guardar un secreto nuevo (Interactivo)"
run-secure   - Ejecutar con inyección segura de secretos"
run-insecure   - Ejecutar con inyección insegura de secretos"
test    - Ejecutar pruebas unitarias con pytest"
scan    - Ejecutar escaneo de seguridad (simulado)"
help    - Mostrar este mensaje de ayuda"





Otras ejecuciones útiles:

TEST de secrets/secrets_cli.py:
pasos: make test

MANIPULACIÓN DE SECRETOS:
pasos: cd secrets/ , 
Crea un secreto con passphrase ingresado: python secrets_cli.py store API_TOKEN ContenidoSecreto
Lista secretos: python secrets_cli.py list
Obtiene secreto usando passphrase: python secrets_cli.py get API_TOKEN


