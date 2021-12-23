#PROYECTO FINAL CODERHOUSE

-Descripcion del proyecto
Este es un proyecto fue creado como presentacion de proyecto final al curso de Python. Para ello se creo un proyecto web compuesto basicamente por Python y HTML. El proyecto web trata de una sitio web de venta de pasteles y reposteria.

-Construido con:
 -HTML (templates)
 -Bootstrap(navbar)
 -Python(proyecto, aplicacion, BD)

-Pasos para probar el proyecto:
 -Descargar o clonar  el repositorio https://github.com/Alejandrojlealr/ProyectoFinalCoder.git
 -En el editor de codigo por medio de la terminal activar el entorno virtual pipenv usando el comando ---> pipenv shell. Si no tiene instalado el entorno virtual pip se debe instalar usando el comando ---> pip install pipenv
 -Si no tiene instalado Django, ir a la pagina de Django www.djangoproject.com y descargar la ultima version, luego desde la terminal del editor o CMD instalarlo con el comando --->pip install Django. Luego de culminada la instalacion verificar con el comando --->python
 --->import django
 --->django.VERSION
 -Luego activar el servidor de prueba en django. Una vez dentro del proyecto debemos asegurarnos que nos encontramos en el mismo nivel que el archivo manage.py para poder correr el servidor de prueba, para ello usamos el comando ls en la terminal. Una vez verificado que esta estamos a nivel del archivo manage.py activamos el servidor local con el comando ---> py manage.py runserver
 -Crear el superuser para el admin de django usando la terminal ---> py manage.py createsuperuser (asignar username y password)
 -Ir al admin con la url http://127.0.0.1:8000/admin/login/?next=/admin/   para ver y administrar el proyecto desde el administrador de django.  Desde aca tambien se puede crear y autorizar otros user.
 -Desde el navbar de home se puede dirigir hacia cualquier otro template por medio de los links y viceversa.

Autor:
Alejandro Leal
Python developer trainee



