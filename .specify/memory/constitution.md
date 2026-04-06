# Constitución de DriveSimLicencesServer

## Principios Fundamentales

### I. Validación Estricta de Licencias
Toda validación de licencia debe seguir un flujo jerárquico: existencia previa en la base de datos y luego verificación de vigencia temporal. Una licencia es válida hasta el final del día de su fecha de vencimiento inclusive.

### II. Integridad del Modelo de Datos
El modelo de licencia debe utilizar UUIDs como identificadores únicos para garantizar la seguridad por oscuridad y evitar la enumeración de recursos. Las fechas de vencimiento deben almacenarse sin componentes de tiempo (solo Año, Mes, Día).

### III. Simplicidad de la API
Los endpoints de validación deben ser minimalistas y retornar respuestas booleanas claras (`active`). El sistema debe priorizar la rapidez de respuesta y la facilidad de consumo por parte de clientes externos.

### IV. Seguridad y Privacidad
Nunca se deben exponer detalles internos de la base de datos o del servidor en las respuestas de error. Las licencias inexistentes deben ser tratadas con el mismo formato de respuesta que las licencias vencidas para evitar ataques de recolección de IDs.

### V. Desarrollo Basado en Pruebas
Cualquier cambio en la lógica de validación o en el modelo de datos debe estar respaldado por pruebas unitarias que cubran casos de éxito, expiración exacta y recursos inexistentes.

## Requisitos Tecnológicos
- **Framework:** Django con Django Rest Framework (DRF).
- **Base de Datos:** SQLite para desarrollo, compatible con modelos relacionales estándar.
- **Identificadores:** UUID v4.

## Flujo de Trabajo
1. Definición de la especificación técnica.
2. Implementación de pruebas de validación.
3. Desarrollo de la lógica de negocio y endpoints.
4. Verificación de integridad y estándares.

**Versión**: 1.0.0 | **Ratificada**: 2026-03-24 | **Última Enmienda**: 2026-03-24
