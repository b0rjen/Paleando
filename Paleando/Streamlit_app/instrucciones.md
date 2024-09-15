# Instrucciones de uso: Deploy de la aplicación Streamlit en un equipo local

Este documento describe los pasos para ejecutar la aplicación **Streamlit** (`app.py`) en tu equipo local.

**Podrás observar** que también hay una carpeta en el repositorio llamada sencillamente **"Streamlit"**

El contenido de esa carpeta está subido a HEROKU para comprobar que el deploy de la aplicación funciona. Puedes usarla en este enlace:

**https://txt2pdfstreamlitapp-9bbfb8e1c417.herokuapp.com/**

## Requisitos previos

Antes de comenzar, asegúrate de tener los siguientes requisitos instalados en tu equipo:

1. **Python 3.x**: Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
2. **Pip**: Viene incluido con Python, pero puedes verificar si está instalado ejecutando `pip --version` en tu terminal.
3. **Virtualenv** (opcional pero recomendado): Para crear un entorno virtual y aislar las dependencias del proyecto.

## Pasos para el deploy local

### 1. Clonar el repositorio

Primero, debes clonar el repositorio que contiene la aplicación Streamlit.

```bash
git clone https://github.com/b0rjen/Paleando.git
cd Paleando
```

### 2. Instala dependencias

Las encontrarás en el archivo "requirements.txt" que hay en la carpeta raíz del repositorio.

```bash
pip install -r requirements.txt
```

### 3. Ejecuta la app

Mediante la terminal:

```bash
streamlit run app.py
```

Esto te debería abrir en el navegador el sitio **http://localhost:8501/**
donde poder arrastrar o seleccionar los archivos para la conversión
