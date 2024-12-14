# Diario con Django

## Proceso de Instalación
1. Descarga Python: [Link Descarga](https://www.python.org/downloads/)
2. Crea un ambiente virtual:
```
python3 -m venv env
```
3. Activa el ambiente virtual:
```
# Activación en Unix
source env/bin/activate

# Activación en Windows
env\Scripts\activate
```
4. Instala Django:
```
pip install django
```
5. Crea un nuevo proyecto en Django:
```
django-admin startproject diary_project
```
6. Crea una nueva aplicación en Django:
```
cd diary_project
python manage.py startapp diary
```
7. Agrega esta aplicación en el archivo de `settings.py`:
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'diary'
]
```
7. Genera las migraciones y ejeculatas:
```
python manage.py makemigrations
python manage.py migrate 
```
8. Crea un super usuario:
```
python manage.py createsuperuser
```
9. Corre la aplicación:
```
python manage.py runserver
```
