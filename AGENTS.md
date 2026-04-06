# DriveSimLicencesServer - Documentación para Agentes

## Descripción del Proyecto
Servidor de validación de licencias desarrollado en Django para el ecosistema DriveSim. Permite verificar si una licencia (identificada por un UUID) existe y si su fecha de vencimiento es igual o posterior a la fecha actual.

## Arquitectura y Configuración
El proyecto utiliza una configuración dividida por entornos en `drivesim_licences/settings/`:
- **base.py**: Configuraciones comunes.
- **local.py**: Entorno de desarrollo. Utiliza SQLite y no requiere variables de entorno.
- **production.py**: Entorno de producción. Utiliza PostgreSQL y requiere variables de entorno.

## Modelo de Datos
### Licencia
- **id**: UUIDField (Primary Key). El ID debe ser ingresado manualmente (no se autogenera).
- **fecha_vencimiento**: DateField (Año-Mes-Día).

## API Endpoints
### Validar Licencia
- **URL**: `GET /api/validate-licence/<uuid>/`
- **Respuesta**:
  - `{"active": true}`: Si el UUID existe y `hoy <= fecha_vencimiento`.
  - `{"active": false}`: Si el UUID no existe o la licencia ha expirado.

## Despliegue y Ejecución

### Ambiente Local (Sin Docker)
1. Instalar dependencias: `pip install -r requirements.txt`
2. Aplicar migraciones: `python manage.py migrate`
3. Iniciar servidor: `python manage.py runserver`
*Por defecto utiliza `settings.local`.*

### Ambiente Local (Con Docker)
1. Construir y levantar: `docker-compose -f docker-compose.local.yml up --build`
*Utiliza SQLite dentro del contenedor para desarrollo rápido.*

### Ambiente Productivo (Docker + PostgreSQL)
1. Configurar variables de entorno (DB_NAME, DB_USER, DB_PASSWORD, etc.).
2. Construir y levantar: `docker-compose -f docker-compose.prod.yml up --build`
*Utiliza PostgreSQL y la configuración de `production.py`.*

## Tareas Administrativas
Para crear un superusuario en el ambiente local de Docker:
```bash
docker-compose -f docker-compose.local.yml exec web python manage.py createsuperuser
```
