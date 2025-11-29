##### VIDEO_SPRINT1: https://1drv.ms/f/c/fdb226ef3c2e079a/IgB2noNVUJfPS5e81w-NccoyAUkVa5TpEi2qWCfg3MtLr-o?e=GoTnZd
Historia 3: Implementación y Ejecución de Pruebas (make test)
ID: #21

Título: Implementación y Ejecución de Pruebas (make test)

Descripción Corta: Crear tests unitarios de secrets_cli.py

Criterios de Aceptación:
1. Usa pytest
2. Implementa en el Makefile, make test
3. Se prueban todos los métodos de secrets_cli.py

Responsable(s): Serrano Max

Historia 19: Reporte de métricas, README y Video Final 

ID: #19

Título: Realizar reporte de métricas, documentar README y crear Enlace de videosprint2

Descripción Corta: Realizar reporte de métricas, documentar README y crear Enlace de videosprint2.

Criterios de Aceptación:
1. NÚMERO de secretos gestionados, NÚMERO de ejecuciones "seguras" vs "inseguras" en pruebas,Tiempo promedio del flujo "guardar ->ejecutar". 
2. Ejecutar 2-3 comandos (make dev, make test, make scan) y obtener el mismo resultado que muestra el Readme para cualquier persona. 
3. Enlace de Onedrive de video_sprint2

Responsable(s): Serrano Max

Historia 18: Escenario Inseguro y Registro de Riesgos

ID: #18

Título: Implementar escenario inseguro (Bad Example) y Registro de Riesgos.

Descripción Corta: Crear un script que demuestre la vulnerabilidad de gestionar secretos en texto plano (archivos .env inseguros) y documentar formalmente los riesgos de seguridad del proyecto.

Criterios de Aceptación:
1. El script `scripts/run-bad-example.sh` ejecuta un contenedor exponiendo un secreto en un archivo `.env` visible.
2. Se verifica visualmente en la terminal que el secreto es legible en texto plano.
3. El archivo `docs/risk-register.md` contiene al menos 5 riesgos identificados con su probabilidad, impacto y plan de mitigación.

Responsable(s): Aaron Davila

Historia 17: Implementación de Scripts de Inyección Segura (Bash)

ID: #17

Título: Implementar scripts de inyección segura (store y run-secure)

Descripción Corta: Desarrollo de scripts en Bash que orquestan la comunicación entre el CLI de Python y el contenedor Docker para garantizar que los secretos se inyecten directamente en memoria RAM, sin tocar el disco.

Criterios de Aceptación:

1. scripts/store-secret.sh: Permite guardar secretos cifrados de forma interactiva (ocultando la entrada de contraseña).

2. scripts/run-with-secret.sh: Desencripta el secreto usando el CLI y lo pasa al contenedor mediante docker run -e API_TOKEN=... sin generar archivos temporales.

3. Seguridad: Se verifica que tras la ejecución no quedan archivos residuales con credenciales en la carpeta del proyecto.

Responsable(s): Poma Walter

Historia 20: Actualización del Makefile y Automatización

ID: #20

Título: Actualización del Makefile para orquestación de scripts y correcciones

Descripción Corta: Integrar los nuevos scripts de Bash del Sprint 2 al Makefile principal para facilitar la ejecución y corregir bugs de integración en los scripts de prueba.

Criterios de Aceptación:

1. Nuevos Targets: make store-secret, make run-secure y make run-insecure ejecutan los scripts correspondientes sin pasos manuales.

Corrección de Bugs: El script run-bad-example.sh ejecuta correctamente tras corregir la referencia a la imagen Docker (app-secret-store:v1).


Responsable(s): Poma Walter

