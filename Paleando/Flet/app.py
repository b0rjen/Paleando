import flet as ft
import pandas as pd
from io import BytesIO
from fpdf import FPDF
import os  # Para manejar los nombres y rutas de archivos

# Función para generar el PDF
def generar_pdf(df):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Añadir encabezado
    pdf.cell(40, 10, "Tiempo", border=1)
    pdf.cell(30, 10, "Fuerza", border=1)
    pdf.cell(30, 10, "Ataque", border=1)
    pdf.cell(30, 10, "Salida", border=1)
    pdf.cell(40, 10, "Verticalidad", border=1)
    pdf.ln()

    # Añadir contenido de la tabla
    for _, row in df.iterrows():
        pdf.cell(40, 10, str(row.iloc[0]), border=1)
        pdf.cell(30, 10, str(row.iloc[1]), border=1)
        pdf.cell(30, 10, str(row.iloc[2]), border=1)
        pdf.cell(30, 10, str(row.iloc[3]), border=1)
        pdf.cell(40, 10, str(row.iloc[4]), border=1)
        pdf.ln()

    buffer = BytesIO()
    pdf_output = pdf.output(dest='S').encode('latin1')  # Se genera el PDF en bytes
    buffer.write(pdf_output)
    buffer.seek(0)
    return buffer

def main(page: ft.Page):
    def on_file_upload(e):
        if e.files:
            # Validar el tipo de archivo
            file_name = e.files[0].name
            file_extension = file_name.split('.')[-1]
            if file_extension not in ['csv', 'txt']:
                page.add(ft.Text("Formato de archivo no válido. Solo se permiten archivos CSV o TXT."))
                return
            
            # Obtener la ruta del archivo cargado
            file_path = e.files[0].path

            # Obtener el nombre del archivo sin extensión para usarlo en el PDF
            base_file_name = os.path.splitext(file_name)[0]
            pdf_file_name = f"{base_file_name}.pdf"
            
            # Leer el archivo desde la ruta como DataFrame
            df = pd.read_csv(file_path, header=None, names=[
                "Tiempo", "Fuerza", "Ataque", "Salida", "Verticalidad"
            ])
            
            # Eliminar la primera fila si es incorrecta
            df = df.drop(index=0).reset_index(drop=True)
            
            # Crear el PDF
            pdf_content = generar_pdf(df)

            # Guardar el PDF en el directorio actual
            output_path = os.path.join(os.getcwd(), pdf_file_name)
            with open(output_path, "wb") as f:
                f.write(pdf_content.read())

            # Mostrar mensaje de confirmación
            page.add(ft.Text(f"PDF guardado en: {output_path}"))

            # Mostrar botón para abrir la carpeta donde se guardó el archivo
            page.add(
                ft.ElevatedButton(
                    "Abrir carpeta",
                    on_click=lambda _: os.startfile(os.getcwd()),  # Abre la carpeta actual
                    width=250
                )
            )

    # Estilo general de la página
    page.theme_mode = ft.ThemeMode.DARK  # Puedes cambiarlo a LIGHT si prefieres
    page.title = "Conversor de TXT a PDF"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLACK  # Fondo oscuro
    
    # Contenedor para la subida del archivo
    file_picker = ft.FilePicker(on_result=on_file_upload)
    page.overlay.append(file_picker)

    # Layout principal
    page.add(
        ft.Column(
            [
                ft.Text(
                    "Sube tu archivo de texto (CSV o TXT)",
                    size=24,  # Tamaño de fuente más grande
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
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=30  # Espaciado entre elementos
        )
    )

# Ejecutar la aplicación en ventana emergente
ft.app(target=main)
