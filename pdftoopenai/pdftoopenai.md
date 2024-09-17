# Descripción del Proyecto - Análisis y Generación de PDF con IA

Este proyecto utiliza **Python**, **pandas**, **FPDF**, y **OpenAI** para procesar archivos de texto (.txt) con datos estructurados, analizarlos mediante una IA y generar un informe en formato PDF. El flujo del proyecto es el siguiente:

## Funcionalidades Principales

1. **Carga de archivo TXT**:

   - El proyecto toma un archivo de texto con columnas de datos (Tiempo, Fuerza, Ataque, Salida, Verticalidad) y lo convierte en un DataFrame de pandas.

2. **Envío del contenido a la IA**:

   - Utilizando la API de **OpenAI**, el contenido del archivo se envía junto con un **prompt** personalizado para que la IA analice los datos. El modelo de IA utilizado es **GPT-4**, conocido por su capacidad de procesamiento avanzado de lenguaje natural.

3. **Generación de un informe en PDF**:

   - La respuesta de la IA se captura y se convierte en un archivo **PDF**. El PDF contiene el análisis detallado proporcionado por la IA y se justifica adecuadamente.

4. **Generación automática del nombre del PDF**:
   - El nombre del archivo PDF generado se basa en el nombre del archivo de texto cargado, añadiendo el sufijo `_ia_respuesta.pdf`.

# LIMITACIONES

Puesto que hace llamadas a la API de openai, con limitaciones de tokens, se recomienda que la prueba se haga con los archivos txt que se incluyen en la carpeta

## Interfaz Gráfica

- Se incluyen carpetas con proyectos en Streamlit y en Flet

## Uso

El archivo principal se puede ejecutar como un script de Python. Solo necesita un archivo de texto y un **prompt** personalizado para ejecutar el análisis y generar el PDF.

## Tecnologías Utilizadas

- **Python** para la lógica del proyecto.
- **pandas** para manipulación y lectura de datos en formato tabular.
- **FPDF** para la generación de archivos PDF.
- **OpenAI API** para analizar los datos mediante el modelo GPT-4.

## Requisitos

- Tener la API Key de OpenAI configurada en las variables de entorno para el acceso a la API.
- Tener instaladas las bibliotecas necesarias: `pandas`, `fpdf`, y `openai`.

## Ejemplo de Uso

1. Se carga un archivo `.txt` con los datos.
2. Se genera un DataFrame con esos datos.
3. Se envían los datos a la IA con un prompt definido.
4. Se genera y guarda un PDF con la respuesta de la IA en la misma carpeta del archivo original.

**Para ejecutarlo sin interfaz gráfica**

```bash
python pdftoopenai.py
```

Esto devolverá un mensaje en consola que indicará dónde está el informe
