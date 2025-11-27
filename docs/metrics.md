<!-- Registro por sprint, incluyendo como mínimo: -->
<!-- § Throughput: Número de historias/tareas completadas. -->
<!-- § Lead time: tiempo desde que una tarea entra a In Progress hasta Done -->
<!-- (pueden medir en horas/días de trabajo). -->
<!-- § WIP: cuántas tareas en In Progress simultáneamente (máximo WIP  -->
<!-- acordado + observaciones). -->
<!-- § Builds: Número de builds/ejecuciones de pipeline exitosas vs fallidas. --> # No se realizo pipelines
<!-- § Para proyectos con foco en seguridad: -->
<!-- • Vulnerabilidades detectadas (por severidad si es posible). -->
<!-- • Vulnerabilidades mitigadas/cerradas por sprint. -->
Número de historias/tareas completadas: 13

 #1   Inicializar estructura de carpetas y Makefile                   Responsable(Max Serrano)			Lead-time:1 hora
 #2   Implementar secrets_cli.py con funcionalidad básica de cifrado  Responsable(Max Serrano)			Lead-time:2 dias   
 #3   Crear App de prueba y Dockerfile endurecido (Non-Root)          Responsable(Walter Poma)			Lead-time:1 dia
 #4   Redactar documentación base (Vision, Backlog y DoD)             Responsable(Aaron Davila)			Lead-time:1 dia
 #6   feat makefile                                                   Responsable(Aaron Davila)			Lead-time:2 horas
 #9   Sprint1-SerranoMax                                  			  Responsable(Max Serrano)			Lead-time:2 horas
 #10  Sprint1-PomaWalter                                              Responsable(Walter Poma)			Lead-time:2 horas
 #11  fix: Corregir puertos incorrectos en make dev                   Responsable(Walter Poma)			Lead-time:1 hora
 #17  Implementar scripts de inyección segura (store y run-secure)    Responsable(Walter Poma)			Lead-time:1 dia
 #18  Implementar escenario inseguro y registro de riesgos            Responsable(Aaron Davila)			Lead-time:1 dia
 #19  Reporte de métricas, README y Video Final                       Responsable(Max Serrano)			Lead-time:2 horas
 #20  Actualización del Makefile y Automatización                     Responsable(Walter Poma)			Lead-time:2 horas
 #21  Implementación y Ejecución de Pruebas (make test)               Responsable(Max Serrano)     		Lead-time:1 hora      
   
El wip acordado fue de 3 o uno por integrante.

Para proyectos con foco en seguridad:
Vulnerabilidades detectadas (por severidad si es posible): 1 secreto encriptado subido por error
Vulnerabilidades mitigadas/cerradas: 1, se agrego al gitignore.
NÚMERO de secretos gestionados:1
NÚMERO de ejecuciones "seguras" vs "inseguras" en pruebas:1,1
Tiempo promedio del flujo "guardar ->ejecutar" :  3s, debido a que es encriptacion simple 
