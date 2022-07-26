# Archinonproyecto
Archinon es un proyecto basado en AnonFiles. Donde puedes subir archivos, imagenes y videos de forma anonima. Tambien cuenta con la funcionalidad de que pasado 5 minutos de hacer una carga a la base de datos el archivo se eliminara automaticamente

# Algunos errores o cosas a mejorar: 
Error - Carga de archivos pesados: Estos al ser muy pesados se quedan cargando y se cae la pagina(En produccion)

Link del proyecto desplegado: https://archinon.herokuapp.com/

# ¿Como funciona?
1. Ingresa al link del proyecto 

2. Elije el tipo de archivo que deseas subir

3. Seleccionalo y dale en cargar

4. Una vez cargado el archivo lo llevara a una pagina con un link unico, este link sera la unica forma de acceder a descargar el archivo. 

Sin el link no podra acceder a descargar el archivo que subio asi que no olvide guardarlo

5. Pasado 5 minutos despues de la carga del archivo a la base de datos esta se eliminara

# Descargue e instale Archinon
Antes de descarga el repositorio es necesario que tenga redis instalado en su maquina:  https://github.com/tporadowski/redis/releases

Descargue el repositorio

```
$ git clone https://github.com/JsonAndrx/archinonproyecto.git
```

Ingrese al proyecto

```
$ cd archinonproyecto
```

Despues cree una maquina virtual o puede saltarse esta parte si lo desea, y active el entorno
```
$ python3 -m venv env
$ ./env/Scripts/activate
```
Una vez activado el entorno intale los requerimientos
```
(venv)$ pip install -r requirements.txt
```
Ahora que tiene casi listo el proyecto solo queda crear y configurar la base de datos.
Para crear la base de datos necesitar descar Postgres y crearla manualmente, utilice las siguientes credenciales cuando cree su BD:
```
Nombre DB : archinon
Password : 1234
```
Ahora que tiene listo el proyecto y su base de datos, pase a hacer las migraciones
```
(venv)$ python manage.py makemigrations
(venv)$ python manage.py migrate
```
Una vez hechas las migraciones cree el usuario administrador 
```
(venv)$ python manage.py createsuperuser
Username:
Email address:
Password:
Password(again):
```
Con esto ya estaria listo el proyecto y el usuario administrado para correr el proyecto, para correr el proyecto use el siguiente comando:
```
(venv)$ python manage.py runserver
```
Para ingresar al panel de administrador ingrese admin al link que se ejectuo al iniciar el proyecto
```
http://127.0.0.1:8000/admin/
```
