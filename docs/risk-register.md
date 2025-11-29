# Registro de Riesgos (Risk Register)

Este documento identifica los riesgos de seguridad y técnicos asociados al manejo de secretos y contenedores en el proyecto.

| ID | Riesgo / Descripción | Probabilidad / Impacto | Plan de Mitigación | Estado |
|----|----------------------|------------------------|--------------------|--------|
| **R-01** | **Secretos en texto plano en disco (.env)**<br>Guardar credenciales en archivos ".env" sin cifrar aumenta el riesgo de exfiltración si el atacante gana acceso al sistema de archivos o si se sube el archivo al repositorio por error. | **Alta / Alto** | Utilizar "secrets_cli.py" para cifrar secretos en reposo ("storage/*.enc") e inyectarlos solo en memoria durante la ejecución. |  En Progreso |
| **R-02** | **Secretos visibles en historial de Shell**<br>Pasar secretos como argumentos ("docker run -e PASS=...") deja la credencial guardada en el historial de comandos ("~/.bash_history") y visible en la lista de procesos ("ps aux"). | **Media / Medio** | No pasar secretos por línea de comandos. Usar inyección de variables de entorno desde memoria o archivos temporales seguros. |  Mitigado |
| **R-03** | **Ejecución de contenedores como Root**<br>Si el contenedor se compromete, un atacante siendo "root" podría escalar privilegios hacia el host. | **Media / Alto** | Configurar "USER appuser" en el Dockerfile y usar imágenes base mínimas ("python:3.12-slim"). |  Mitigado (Ver Dockerfile) |
| **R-04** | **Hardcoding de credenciales en código**<br>Incluir tokens o claves directamente en el código fuente ("main.py") hace imposible rotarlos sin redesplegar y expone el secreto a todos los desarrolladores. | **Baja / Alto** | Leer siempre desde variables de entorno ("os.getenv") y nunca escribir valores por defecto sensibles en el código. |  Mitigado |
| **R-05** | **Persistencia de secretos en capas Docker**<br>Copiar un archivo de secretos o usar "ENV" en el Dockerfile deja el secreto grabado permanentemente en el historial de la imagen, accesible con "docker history". | **Media / Medio** | Usar ".dockerignore" para excluir archivos de secretos y nunca usar instrucciones "ENV" para definir claves en tiempo de build. |Mitigado |

**Leyenda de Estado:**
*  Abierto: El riesgo existe y no se ha tratado.
*  En Progreso: Se está implementando la solución en el sprint actual.
*  Mitigado: La arquitectura actual ya previene este riesgo.