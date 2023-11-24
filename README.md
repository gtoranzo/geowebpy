# geowebpy

_GeoApp desarrollada con Python._

## Corriendo el Proyecto.

### Instalación

1. Clone el proyecto [download it](https://github.com/gtoranzo/geowebpy) en tu pc.
2. Asegurate que tienes instalado [Django and folium](https://pypi.org/project/Django/).
   Vaya hasta a la consola y ejecuta el siguientes comandos:

```
$ pip install Django
```

```
$ pip install folium
```

3. En la consola ejecuta el siguiente comando:

```
$ python manage.py runserver
```

4. Ya en localhost se debería poder ver la siguiente interfaz en el puerto 8000:

```
$ http://127.0.0.1:8000/
```

### Migraciones no aplicadas

Migraciones no aplicadas. Es posible que su proyecto no funcione correctamente hasta que aplique las migraciones para aplicaciones: administrador, autenticación, tipos de contenido, sesiones.

Ejecute en la consola el siguiente comando:

```
$ python manage.py migrate
```
