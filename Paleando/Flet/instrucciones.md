# Hacer la aplicación de Flet un archivo ejecutable

Este documento describe los pasos para compilar una aplicación desarrollada con **Flet** en un archivo .exe portable para así poder ejecutarse sin necesidad de tener Python instalado en la máquina. Obviamente quien realice la compilación sí habrá de tener python y los requirements correspondientes.

## Pero... por qué FLET?

Si bien es cierto que flet es un framework que está aún muy por desarrollar (ahora mismo su versión es la 0.24) resulta interesante porque tiene el potencial de [FLUTTER](https://flutter.dev/) sin conocimientos del lenguaje DART, sino con Python, y de cara a una futura "expansión" a app móvil puede funcionar bien.
Aunque tenga ciertas limitaciones, lo que hemos hecho hasta ahora funciona correctamente.

## Requisitos previos

Antes de comenzar, asegúrate de tener los siguientes requisitos instalados en tu equipo:

1. **Python 3.x**: Asegúrate de tener Python instalado. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
2. **Pip**: Viene con Python, pero puedes verificar si está instalado con `pip --version`.
3. **Entorno virtual (recomendado)**: Es recomendable trabajar en un entorno virtual para gestionar las dependencias del proyecto.

## Pasos para compilar la aplicación

### 1. Preparar el entorno

Primero, asegúrate de que tu entorno virtual esté activo y que tienes **Flet** instalado.

- **Activar el entorno virtual** (en Windows):
- **Instalar flet** si aún no lo has hecho, con el comando:

```bash
pip install flet
```

- Recomiendo, de todas maneras, instalar el archivo requirements.txt que hay en la carpeta raíz del proyecto.
- **Instalar PyInstaller**

```bash
pip install pyinstaller
```

- **Crear el ejecutable**

```bash
pyinstaller --onefile --windowed app.py
```

**OJO**, pyinstaller tiene numerosos comandos para compilar la app.
En este ejemplo que he puesto se puede ver que está configurado para que la app sea en un solo archivo portable y que cuando se ejecute sea en una ventana.
Como se puede ver en la carpeta, hay un icono "rowing.ico" para que sea el icono de la app. Obviamente se puede cambiar por cualquier otro de las mismas características:

```bash
pyinstaller --onefile --windowed --icon=iconoquequieras.ico app.py
```

[Documentación de PyInstaller](https://pyinstaller.org/en/stable/)

- **Verificar el archivo ejecutable**
  Tras unos segundos / minutos, dependiendo de cada máquina, el archivo .exe se encontrará dentro de la subcarpeta **/dist** bajo la carpeta donde se haya guardado el proyecto. Hacer doble clic en el ejecutable para comprobar que funcione.
