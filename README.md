#DriveLoop Admin Desktop

Aplicación de escritorio desarrollada en **Python + PySide6** para la gestión administrativa del sistema DriveLoop.

Permite a un administrador gestionar vehículos, visualizar reservas asociadas y consultar tickets desde una interfaz gráfica moderna.

---

## Tecnologías utilizadas

* Python 3.10+
* PySide6 (Interfaz gráfica)
* MySQL / MariaDB
* mysql-connector-python
* bcrypt (seguridad de contraseñas)
* python-dotenv

---

## Acceso

Esta aplicación **solo permite el acceso a usuarios con rol Administrador**.

---

## Requisitos del sistema

Antes de ejecutar el proyecto, debes tener instalado:

### Software requerido

* Python 3.10 o superior
* MySQL o MariaDB
* Git (opcional pero recomendado)
* Visual Studio Code

---

### Extensiones recomendadas en VS Code

Instalar en VS Code:

* Python (Microsoft)
* Pylance
* MySQL (opcional)

---

## Instalación paso a paso

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/driveloop-admin-desktop.git
cd driveloop-admin-desktop
```

---

### 2. Crear entorno virtual

```bash
python -m venv venv
```

---

### 3. Activar entorno virtual

En Windows (PowerShell):

```bash
venv\Scripts\Activate.ps1
```

---

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 5. Configurar variables de entorno

Crear archivo `.env` en la carpeta `app/config/` o raíz del proyecto:

```env
DB_HOST=127.0.0.1
DB_PORT=3306
DB_NAME=driveloop
DB_USER=root
DB_PASSWORD=tu_password
```

---

### 6. Importar base de datos

* Abrir MySQL Workbench o phpMyAdmin
* Crear base de datos:

```sql
CREATE DATABASE driveloop;
```

* Importar el archivo `.sql` del proyecto

---

### 7. Ejecutar la aplicación

```bash
python main.py
```

---

## Uso de la aplicación

### Módulos disponibles:

* Dashboard administrativo
* Gestión de vehículos
* Visualización de reservas por vehículo
* Gestión de tickets

---

## Funcionalidades destacadas

* Login con validación de rol (Administrador)
* Tabla de vehículos simplificada
* Modal de detalle de vehículo
* Edición y eliminación de vehículos
* Visualización de reservas:

  * Activas
  * Finalizadas
* Modal de tickets con detalle completo

---

## Notas importantes

* No eliminar la carpeta `venv/`
* Verificar conexión a la base de datos antes de ejecutar
* Algunos registros no pueden eliminarse por restricciones de base de datos (FK)

---

## Autor

Proyecto desarrollado como parte del proceso de formación en análisis y desarrollo de software.

---

## Licencia

Uso académico / educativo
