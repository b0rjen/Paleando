# 🌟 Proyecto: Paleando con José 🚣‍♂️

En este repo se incluyen las aplicaciones que utilizaremos para realizar el entrenamiento de la IA para el proyecto de sensor de las palas de José.

Estas aplicaciones incluyen de momento:

- Aplicación para transformar texto y csv por pdf transformado para entrenamiento.
- Aplicación pdftoopenai que transforma el texto subido y lo promptea con OpenAI. **Tiene limitaciones de tokens por la API.**

También hay un pequeño cuaderno de jupyter notebook que contiene un análisis muy básico que comenté con José en su día para poder aprender un poco sobre qué datos mostraban los sensores.

Aunque la lógica es la misma básicamente en todas las apps, puede variar alguna funcionalidad, sobre todo teniendo en cuenta las limitaciones propias de los frameworks que se han utilizado.

## 📄 Frameworks empleados

- **[Streamlit](https://streamlit.io/)**
- **[Flet](https.flet.dev)**
- **[Django](https://www.djangoproject.com/) (coming VERY soon)**
- **[Reflex](https://reflex.dev/) (coming soon)**

## Instrucciones de uso 📄

Dentro de cada carpeta se incluye un archivo .md que te guiará para el proceso de instalación o ejecución de la aplicación.

## 🚀 Funcionalidades

- **Subida de archivos**: Permite a los usuarios subir archivos en formato `.txt` o `.csv` directamente a la aplicación. 👨‍💻
- **Conversión a PDF**: Una vez subidos, los archivos son procesados y convertidos en un documento **PDF** con formato de tabla. 📄✨
- **Soporte para múltiples archivos**: Puedes subir varios archivos a la vez, y la app los convierte y los descarga en un archivo ZIP que contiene todos los PDFs generados. 📂📑
- **Generación de tablas**: Cada archivo es procesado y presentado en una tabla con encabezados fijos: **Tiempo, Fuerza, Ataque, Salida y Verticalidad**. 📊
- **Encabezados repetidos**: El archivo PDF generado incluye los encabezados en cada nueva página, asegurando que la tabla sea fácil de leer en documentos largos. 📝

- ✅ Subida de archivos CSV o TXT.
- ✅ Conversión directa a PDF.
- ✅ Descarga en formato ZIP de todos los PDFs generados.
- ✅ Interface amigable utilizando Streamlit.
- ✅ Soporte para múltiples archivos y tablas formateadas.

## 💡 ¿Cómo usar la app?

1. Abre la aplicación en Streamlit.
2. Sube uno o varios archivos `.csv` o `.txt`.
3. Haz clic en **Generar PDF**.
4. Descarga tus archivos en formato PDF, individualmente o como un ZIP que contiene todos los PDFs generados. 🎉

## 🔧 Requisitos

- **Python 3.x**
- **Streamlit**
- **fpdf** (para la generación de PDFs)
- **pandas** (para la manipulación de datos)
- **flet**

## 🛠️ Instalación

Para usar la app, clona este repositorio e instala los requisitos:

```bash
git clone git@github.com:b0rjen/Paleando.git
cd paleando
pip install -r requirements.txt
```

## Contribuciones 🤝

Si deseas contribuir a este proyecto, siéntete libre de hacer un fork y enviar un pull request con tus mejoras o sugerencias. ¡Estamos abiertos a colaboraciones!

## 🛡️ Licencia

Este proyecto está licenciado bajo la **Licencia Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International**. Esto significa que eres libre de compartir el material en cualquier medio o formato, pero debes dar el crédito adecuado, no puedes usarlo con fines comerciales y no puedes distribuir trabajos derivados.

🔗 [Ver la licencia completa](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode)

[![Licencia CC BY-NC-ND 4.0](https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

🔗 [Mi perfil de GitHub](https://github.com/b0rjen)

## Contacto 📬

Si tienes preguntas o comentarios, no dudes en contactar en borja@borja.app.

🎉Visita pronto mi [portfolio](https://borjen.dev), estoy trabajando en él ahora mismo!🎉
