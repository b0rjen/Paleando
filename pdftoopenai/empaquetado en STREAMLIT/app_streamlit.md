# Resumen de la Aplicación Streamlit para Análisis de Archivos TXT con IA

Esta aplicación, desarrollada con **Streamlit** y **OpenAI**, permite cargar archivos de texto (.txt o .csv), visualizarlos y analizarlos utilizando un modelo de inteligencia artificial. A continuación, se detallan los pasos generales que sigue la aplicación:

# LIMITACIONES

**Debido a las limitaciones de tokens de la API** no es posible cargar otros archivos txt o csv por el momento. Recomiendo hacer la prueba con los archivos txt que se incluyen en la carpeta del proyecto.

1. **Carga de Archivos**:

   - El usuario puede cargar un archivo de texto o CSV que contenga información estructurada en columnas.

2. **Visualización de los Datos**:

   - Los datos del archivo cargado se muestran en una tabla interactiva dentro de la interfaz de **Streamlit**.

3. **Envío de Datos a la IA**:

   - Al presionar el botón "Enviar a IA", el contenido del archivo cargado se envía a un modelo de OpenAI (GPT-4 / 4o), junto con un **prompt** predefinido, para generar un análisis de los datos.

4. **Visualización del Análisis**:

   - La respuesta generada por la IA se muestra en un cuadro de texto en la interfaz de **Streamlit**.

5. **Generación de PDF**:
   - La aplicación genera un PDF con la respuesta de la IA y habilita un botón para que el usuario pueda descargar el PDF directamente desde la aplicación.

### Características adicionales:

- El **prompt** utilizado para dar contexto a la IA está almacenado en un archivo **`prompt.py`**.
- La interfaz permite una experiencia interactiva con la posibilidad de descargar el PDF generado.
  """
