# Mantenimiento de actividad para servicio en Render

Este directorio contiene workflows de GitHub Actions para mantener activo nuestro servicio en Render.

## ¿Por qué es necesario?

Los planes gratuitos de Render hibernan las aplicaciones web después de un período de inactividad. Esto hace que la primera solicitud después de un período de inactividad sea lenta, ya que Render necesita "despertar" la aplicación.

## Cómo funciona

El workflow `keep-alive.yml` hace lo siguiente:

1. Se ejecuta automáticamente cada 20 minutos
2. Envía una solicitud HTTP a nuestra aplicación en Render
3. Registra el resultado del ping
4. Esta actividad periódica evita que Render hiberne la aplicación

## Configuración

Para que funcione correctamente:

1. Asegúrate de reemplazar `TU-URL-DE-RENDER.onrender.com` con la URL real de tu aplicación en Render
2. Verifica que los GitHub Actions estén habilitados en tu repositorio

## Monitoreo

Puedes verificar el estado de los pings en la pestaña "Actions" de tu repositorio de GitHub.

## Notas

- El cronograma está configurado para ejecutarse cada 20 minutos
- Ajusta la frecuencia según tus necesidades, teniendo en cuenta los límites de uso de GitHub Actions
- También puedes ejecutar manualmente el workflow desde la interfaz de GitHub
