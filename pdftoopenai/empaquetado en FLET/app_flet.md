# Resumen de la Aplicación Flet para Análisis de Archivos TXT con IA

Esta aplicación, desarrollada con **Flet** permite cargar archivos de texto (.txt o .csv) que contienen datos estructurados y analizarlos utilizando un modelo de inteligencia artificial (IA), en este caso con el código adaptado para OpenAI. Los pasos generales de la aplicación son:

# LIMITACIONES

**Debido a las limitaciones de tokens de la API** no es posible cargar otros archivos txt o csv por el momento. Recomiendo hacer la prueba con los archivos txt que se incluyen en la carpeta del proyecto.

1. **Carga de Archivos**:
   - El usuario puede cargar archivos de texto o CSV que contienen información estructurada en columnas (por ejemplo, tiempo, fuerza, ataque, etc.).
2. **Visualización de los Datos**:
   - Los datos cargados se muestran en una tabla en la primera columna de la interfaz. Si el archivo es muy grande, los datos se limitan a las primeras filas o se presenta un contenedor con scroll para ver todo el contenido.
3. **Envío a la IA**:

   - Al presionar el botón "Enviar a IA", los datos se envían a un modelo de OpenAI (GPT-4 o similar), junto con un **prompt** predefinido, para generar un análisis basado en los datos proporcionados.

4. **Visualización del Análisis**:

   - La respuesta generada por la IA se muestra en la segunda columna en un cuadro de texto que contiene el análisis detallado.

5. **Generación de PDF**:
   - Después de recibir la respuesta de la IA, se genera un archivo PDF con el contenido del análisis y se habilita un botón para descargar dicho PDF.

### Características adicionales:

- La app utiliza un **prompt** predefinido, almacenado en un archivo **`prompt.py`**, que le proporciona contexto a la IA sobre cómo analizar los datos. Para cambiar el prompt, modificar el texto que se incluye (en la variable prompt)

- El PDF generado se descarga directamente desde la interfaz de la aplicación.
