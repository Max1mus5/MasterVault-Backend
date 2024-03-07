
# Gestor de Contraseñas

Este proyecto es un gestor de contraseñas que permite a los usuarios administrar de manera segura y eficiente sus credenciales. Está desarrollado en Python y utiliza tecnologías como FastAPI, SQLAlchemy y PyJWT para proporcionar una experiencia segura y modular.

## Estructura del Proyecto

La estructura del incial del proyecto es la siguiente:

```
backend/
├── main.py
├── requirements.txt
├── config/
│   ├── config.py
│   ├── database.py
│   └── encryption.py
├── models/
│   ├── user.py
│   └── password.py
├── routes/
│   ├── auth.py
│   └── passwords.py
├── middleware/
│   ├── auth_middleware.py
│   └── error_handler_middleware.py
├── services/
│   ├── auth_service.py
│   └── password_service.py
├── repositories/
│   ├── user_repository.py
│   └── password_repository.py
└── utils/
    └── validation.py
```

## Funcionalidades

### Autenticación y Seguridad

- Implementación de un sistema de autenticación utilizando PyJWT.
- Algoritmo de hasheo de contraseñas Master Password de Maarten Billemont para asegurar la integridad de las credenciales.

### Base de Datos

- Utilización de SQLAlchemy para gestionar una base de datos local.
- Almacenamiento cifrado de contraseñas según el algoritmo Master Password de Maarten Billemont.

### Generación de Contraseñas

- Creación de contraseñas basadas en información proporcionada por el usuario (longitud, combinación de letras, caracteres especiales y números).
- Posibilidad de generar contraseñas completamente aleatorias.

### Funcionalidades Adicionales

- Gestión de inicio de sesión, modificación de datos de usuario y manejo de contraseñas almacenadas.

## Instalación y Ejecución

Para ejecutar el proyecto, sigue estos pasos:

1. Clona este repositorio
2. Instala las dependencias: `pip install -r requirements.txt`
3. Ejecuta la aplicación: `uvicorn main:app --reload`

Asegúrate de configurar las variables de entorno y la base de datos según sea necesario antes de iniciar la aplicación.

## Contribuciones

Las contribuciones son bienvenidas. Si tienes alguna sugerencia o mejora, no dudes en abrir un issue o enviar un pull request.
