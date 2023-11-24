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

### Error.

En caso de error:
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

En la consola ejecuta el siguiente comando:

```
$ python manage.py migrate
```
