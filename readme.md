# Prueba técnica backend - Gutierrez Juan Tomás

API backend desarrollada con **Django**, **Django REST Framework** y **JWT**, que permite autentificar usuarios por plataforma y gestionar dispositivos asociados a cada una.  

---

## Tecnologías utilizadas

- Python
- Django
- Django REST Framework (drf)
- SimpleJWT  
- drf-yasg (swagger)  
- SQLite (por defecto)

---

## Instalación
pip install -r requirements.txt

Aplicar migraciones:
python manage.py migrate

Crear un usuario admin:
python manage.py createsuperuser

Iniciar servidor:
python manage.py runserver


---

## Creación de usuarios y plataformas de prueba
Ingresar al panel de administración:
http://localhost:8000/admin/

1. Crear plataforma
Ir a: Platforms → Add Platform
Ejemplos:
Netflix (id 1)
HBO (id 2)

2. Crear usuario
Ir a: Users → Add User
Ejemplo:
email: user1@gmail.com
password: pass2590

3. Asociar usuario a plataforma
Ir a: User platforms → Add User platform
Ejemplo:
user: user1@gmail.com  
platform: Netflix (id 1)

---

## Endpoints y pruebas
Las pruebas en los endpoints pueden realizarse facilmente mediante swagger, el cual incluye breve documentacion de los servicios creados:
http://localhost:8000/swagger/

#### 1. Inicio de sesión

POST /auth/login/

Ejemplo de petición:
```
{
  "email": "user1@gmail.com",
  "password": "pass2590",
  "platform": 1
}
```
Ejemplo de respuesta:
```
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "platform": "Netflix"
}
```
access es el token que se envia como respuesta, el mismo es unico para ese usuario en la plataforma indicada.

#### 2. Crear un dispositivo
POST /devices/

Ejemplo de petición:
```
Headers: Authorization: Bearer <ACCESS_TOKEN>
Body:
{
  "name": "Smart TV",
  "ip_address": "192.168.0.55",
  "active": true
}
```
Ejemplo de respuesta:
```
{
  "id": 1,
  "name": "Smart TV",
  "ip_address": "192.168.0.55",
  "active": true
}
```

#### 3. Listar dispositivos del usuario por plataforma
GET /devices/

Ejemplo de petición:
```
Headers: Authorization: Bearer <ACCESS_TOKEN>
```
Ejemplo de respuesta:
```
[
  {
    "id": 1,
    "name": "Smart TV",
    "ip_address": "192.168.0.55",
    "active": true
  }
]
```
Este endpoint devuelve únicamente los dispositivos asociados:

- Al usuario autentificado
- A la plataforma incluida en el JWT
