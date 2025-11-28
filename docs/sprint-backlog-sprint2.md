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