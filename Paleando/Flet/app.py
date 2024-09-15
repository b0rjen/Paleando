import flet as ft 
import pandas as pd
from io import BytesIO # Para manejar el PDF en memoria
from fpdf import FPDF # Para generar el PDF
import os  # Para manejar los nombres y rutas de archivos

# Función para generar el PDF
def generar_pdf(df):
    pdf = FPDF() # Crear instancia de FPDF
    pdf.add_page() # Añadir una página al PDF
    pdf.set_font("Arial", size=12) # Establecer la fuente y tamaño del texto
    
    # Añadimos encabezado
    pdf.cell(40, 10, "Tiempo", border=1) # Anchura, altura, texto, borde
    pdf.cell(30, 10, "Fuerza", border=1)
    pdf.cell(30, 10, "Ataque", border=1)
    pdf.cell(30, 10, "Salida", border=1)
    pdf.cell(40, 10, "Verticalidad", border=1)
    pdf.ln() # Salto de línea

    # Añadiendo contenido de la tabla
    for _, row in df.iterrows(): # Iterar sobre las filas del DataFrame
        pdf.cell(40, 10, str(row.iloc[0]), border=1) # Anchura, altura, texto, borde
        pdf.cell(30, 10, str(row.iloc[1]), border=1)
        pdf.cell(30, 10, str(row.iloc[2]), border=1)
        pdf.cell(30, 10, str(row.iloc[3]), border=1)
        pdf.cell(40, 10, str(row.iloc[4]), border=1)
        pdf.ln()

    buffer = BytesIO() # Crear un buffer en memoria para guardar el PDF generado
    pdf_output = pdf.output(dest='S').encode('latin1')  # Se genera el PDF en bytes y se codifica en latin1
    buffer.write(pdf_output) # Escribir el contenido del PDF en el buffer en memoria
    buffer.seek(0) # Mover el puntero al inicio del buffer para que pueda ser leído correctamente por el usuario
    return buffer # Devolver el buffer con el contenido del PDF generado

def main(page: ft.Page): # Función principal de la aplicación
    def on_file_upload(e): # Función que se ejecuta al subir un archivo
        if e.files: # Si se ha subido un archivo correctamente 
            # Validamos el tipo de archivo
            file_name = e.files[0].name # Nombre del archivo
            file_extension = file_name.split('.')[-1] # Extensión del archivo
            if file_extension not in ['csv', 'txt']: # Solo permitimos archivos CSV o TXT 
                page.add(ft.Text("Formato de archivo no válido. Solo se permiten archivos CSV o TXT.")) # Mostrar mensaje de error
                return # Salir de la función si el archivo no es válido 
            
            # Obtenemos la ruta del archivo cargado
            file_path = e.files[0].path 

            # Obtenemos el nombre del archivo sin extensión para usarlo en el PDF
            base_file_name = os.path.splitext(file_name)[0] 
            pdf_file_name = f"{base_file_name}.pdf"
            
            # Leemos el archivo desde la ruta como DataFrame
            df = pd.read_csv(file_path, header=None, names=[
                "Tiempo", "Fuerza", "Ataque", "Salida", "Verticalidad"
            ])
            
            # Eliminamos la primera fila si es incorrecta
            df = df.drop(index=0).reset_index(drop=True)
            
            # Creamos el PDF a partir del DataFrame y lo guardamos en memoria
            pdf_content = generar_pdf(df)

            # Guardamos el PDF en el directorio actual
            output_path = os.path.join(os.getcwd(), pdf_file_name)
            with open(output_path, "wb") as f:
                f.write(pdf_content.read())

            # Mostramos mensaje de confirmación
            page.add(ft.Text(f"PDF guardado en: {output_path}")) 

            # Botón para abrir la carpeta donde se guardó el archivo
            page.add(
                ft.ElevatedButton(
                    "Abrir carpeta",
                    on_click=lambda _: os.startfile(os.getcwd()),  # Abre la carpeta donde está el archivo
                    width=250
                )
            )

    # Estilo general de la página
    page.theme_mode = ft.ThemeMode.DARK  # Puedes cambiarlo a LIGHT si prefieres? pero queda bien así
    page.title = "Conversor de TXT a PDF" # Título de la página
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER # Alineación horizontal
    page.vertical_alignment = ft.MainAxisAlignment.CENTER # Alineación vertical
    page.bgcolor = ft.colors.BLACK  # Fondo oscuro
    
    # Contenedor para la subida del archivo
    file_picker = ft.FilePicker(on_result=on_file_upload) # Crear un componente FilePicker
    page.overlay.append(file_picker) # Añadir el FilePicker a la página para que se muestre

    # Layout principal
    page.add(
        ft.Column(
            [
                ft.Text(
                    "Sube tu archivo de texto (CSV o TXT)",
                    size=24,  # Tamaño de fuente más grande que el predeterminado (20)
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.WHITE
                ),
                ft.ElevatedButton(
                    "Seleccionar archivo",
                    on_click=lambda _: file_picker.pick_files(),
                    width=250,
                    style=ft.ButtonStyle(
                        bgcolor=ft.colors.BLUE,
                        shape=ft.RoundedRectangleBorder(radius=8),
                        color=ft.colors.WHITE,
                        padding=15
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER, # Alineación de los elementos del Column 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=30  # Espaciado entre elementos del Column 
        )
    )

# Ejecución de la aplicación en ventana emergente
ft.app(target=main) # Lanzar la aplicación con la función main como punto de entrada
