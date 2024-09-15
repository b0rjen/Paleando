import streamlit as st 
import pandas as pd     
from io import BytesIO # librería ara trabajar con archivos en memoria
from fpdf import FPDF # librería para generar PDFs
import os 
import zipfile 

# Creamos esta clase PDF personalizada para tener encabezado en cada página (añadido en la versión 3)
class PDF(FPDF): 
    def header(self): # método encabezado, para que se ejecute en cada página
        self.set_font("Arial", size=12) # comprobar con José si cambiamos el tipo de letra o se ve bien así. A mi se me ve bien
        self.cell(40, 10, "Tiempo", border=1)  # comprobar también con José si el tamaño de la celda, grosor etc es el adecuado
        self.cell(30, 10, "Fuerza", border=1)
        self.cell(30, 10, "Ataque", border=1)
        self.cell(30, 10, "Salida", border=1)
        self.cell(40, 10, "Verticalidad", border=1)
        self.ln() # salto de línea necesario para que no se solapen los encabezados con los datos de la tabla (añadido desde la versión 2)

# Función para generar el PDF
def generar_pdf(df):
    """
    Genera un archivo PDF a partir de un DataFrame de pandas.
    Este método toma un DataFrame de pandas y genera un archivo PDF que contiene los datos del DataFrame, con un formato de tabla. 
    El PDF es devuelto como un objeto `BytesIO` para que pueda ser descargado o manipulado sin necesidad de almacenarlo en disco.

    Args:
        df (pandas.DataFrame): El DataFrame que contiene los datos a convertir en PDF. 
            Se espera que el DataFrame tenga 5 columnas que representen las categorías:
            "Tiempo", "Fuerza", "Ataque", "Salida" y "Verticalidad".
    Returns:
        BytesIO: Un buffer en memoria que contiene el archivo PDF generado en formato binario (secuencia de bytes).
    
    """
        
    pdf = PDF() # instanciamos la clase PDF
    pdf.add_page() # añadimos una página nueva al PDF
    pdf.set_font("Arial", size=12) # lo comentado en la línea 13

    # añadimos contenido de la tabla
    for _, row in df.iterrows(): # iteramos por cada fila del DataFrame
        pdf.cell(40, 10, str(row[0]), border=1)
        pdf.cell(30, 10, str(row[1]), border=1)
        pdf.cell(30, 10, str(row[2]), border=1)
        pdf.cell(30, 10, str(row[3]), border=1)
        pdf.cell(40, 10, str(row[4]), border=1)
        pdf.ln() 

    # generando el PDF en un buffer
    buffer = BytesIO() # creamos un buffer en memoria para almacenar el pdf
    pdf_output = pdf.output(dest='S').encode('latin1')  # generamos el PDF en bytes y lo codificamos en latin1 (dejo utf-8 por si acaso?) dest='S' es para que se devuelva el PDF como un string)
    buffer.write(pdf_output) # escribimos el CONTENIDO del PDF que está en el buffer de memoria
    buffer.seek(0) # movemos el cursor al principio del buffer. Si no se hace esto, el buffer estará al final y no se podrá leer o descargar el PDF
    return buffer # devolvemos el buffer con el PDF para poder descargarlo

# Función para crear un archivo ZIP con múltiples PDFs (añadido en la versión 3, en versiones anteriores se generaba un único PDF por archivo subido)
def crear_zip(files):
    """
    Crea un archivo ZIP en memoria que contiene múltiples archivos PDF.
    Esta función toma un diccionario de archivos PDF, donde las claves son los nombres
    de los archivos y los valores son objetos `BytesIO` con el contenido del PDF en binario.
    A partir de estos datos, se genera un archivo ZIP que agrupa todos los PDFs, permitiendo
    que se descarguen juntos en un solo archivo comprimido.

    Args:
        files (dict): Un diccionario donde:
            - La clave (key) es un string que representa el nombre del archivo (sin extensión).
            - El valor (value) es un objeto `BytesIO` que contiene los datos binarios del PDF.
    Returns:
        BytesIO: Un buffer en memoria que contiene el archivo ZIP generado.
    """
    zip_buffer = BytesIO() # creamos un buffer en memoria para almacenar el archivo ZIP
    with zipfile.ZipFile(zip_buffer, 'w') as zf: # abrimos el archivo ZIP en modo escritura (w) y lo asignamos a la variable zf (zip file) 
        for file_name, pdf_data in files.items(): # iteramos por cada PDF generado y lo añadimos al archivo ZIP
            zf.writestr(f"{file_name}.pdf", pdf_data.getvalue()) # añadimos el PDF al archivo ZIP con el nombre del archivo original
    zip_buffer.seek(0) # movemos el cursor al principio del buffer como en la función anterior
    return zip_buffer # devolvemos el buffer con el archivo ZIP para poder descargarlo

# Titulamos la aplicación
st.title("TXT2PDF")

# Creamos el file uploader para la subida de archivos con posibilidad de múltiples (añadido en la versión 3):
uploaded_files = st.file_uploader("Arrastra aquí tu archivo en txt o csv. Puedes subir varios a la vez", type=["txt", "csv"], accept_multiple_files=True) 

# Creamos diccionario para almacenar los PDFs generados
pdf_files = {}

if uploaded_files is not None: # si se han subido archivos (no es None)
    for uploaded_file in uploaded_files: # iteramos por cada archivo subido
        # Obtenemos el nombre del archivo original sin la extensión:
        file_name = os.path.splitext(uploaded_file.name)[0] 
        # Leemos el archivo como DataFrame con los encabezados corregidos
        df = pd.read_csv(uploaded_file, header=None, names=[ 
            "Tiempo", "Fuerza", "Ataque", "Salida", "Verticalidad"
        ])
        
        # Eliminamos la primera fila si es incorrecta (la F esa rara que aparece en la primera fila)
        df = df.drop(index=0).reset_index(drop=True) 
        
        # Mostramos en pantalla los datos subidos
        st.write(f"Contenido del archivo '{uploaded_file.name}': ")
        st.dataframe(df) 
        
        # Generamos el PDF y lo almacenamos en el diccionario vacío
        pdf = generar_pdf(df)
        pdf_files[file_name] = pdf

        # Botón para descargar cada PDF individualmente
        st.download_button(
            label=f"Descarga el PDF de {uploaded_file.name}",
            data=pdf,
            file_name=f"{file_name}.pdf",
            mime="application/pdf" # especificamos el tipo MIME para que se descargue como PDF, aquí se podría poner también "application/octet-stream" para que se descargue como archivo genérico
            # pero no es necesario porque ya hemos especificado que es un PDF. depende de si queremos que se descargue como PDF o como archivo genérico, y de cada usuario
        )

    # Si se han generado PDFs, permitimos la descarga del ZIP
    if len(pdf_files) > 0: 
        zip_file = crear_zip(pdf_files)
        
        # Botón para descargar el archivo ZIP
        st.download_button(
            label="Descargar los PDFs generados en un archivo ZIP",
            data=zip_file, # pasamos el archivo ZIP generado
            file_name="pdfs_generados.zip", # nombre del archivo ZIP, consultar con José si se puede poner un nombre más descriptivo. 
            mime="application/zip", # especificamos el tipo MIME para que se descargue como ZIP, como hemos hecho con los PDFs
            use_container_width=True # añadido en la versión 3 para que el botón se ajuste al ancho del contenedor
        )
