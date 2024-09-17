import flet as ft
import pandas as pd
import openai
from fpdf import FPDF
import os

# Configura la API Key desde las variables de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

# Función para leer el archivo .txt y convertirlo en un DataFrame
def leer_txt_a_dataframe(file_path):
    df = pd.read_csv(file_path, header=None, names=["Tiempo", "Fuerza", "Ataque", "Salida", "Verticalidad"])
    return df

# Función para enviar el contenido a la IA
def enviar_a_ia(dataframe, prompt):
    contenido = dataframe.to_string(index=False)  # Convierte el DataFrame a string
    mensaje_completo = f"{prompt}\n\n{contenido}"
    
    messages = [
        {"role": "system", "content": "Eres un asistente útil que analiza datos de entrenamiento."},
        {"role": "user", "content": mensaje_completo}
    ]
    
    completion = openai.chat.completions.create(
        model="gpt-4o-2024-08-06",  # Usa el modelo que prefieras
        messages=messages
    )
    
    return completion.choices[0].message.content

# Función para generar el PDF con la respuesta de la IA
def generar_pdf_con_respuesta(respuesta, output_pdf_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Definir el ancho de la celda para justificar el texto
    ancho_celda = 190  # Ancho en milímetros para ajustarse a la página
    pdf.multi_cell(ancho_celda, 10, respuesta)  # Ajustar el texto al ancho
    
    pdf.output(output_pdf_path)

# Función principal de la aplicación Flet
def main(page: ft.Page):
    def on_file_upload(e):
        if e.files:
            # Ruta del archivo cargado
            file_path = e.files[0].path

            # Leer archivo y generar DataFrame
            df = leer_txt_a_dataframe(file_path)
            prompt = "Por favor, analiza los datos siguientes:"
            
            # Enviar contenido a la IA
            respuesta_ia = enviar_a_ia(df, prompt)
            
            # Generar el PDF
            base_file_name = os.path.splitext(file_path)[0]
            output_pdf_path = f"{base_file_name}_ia_respuesta.pdf"
            generar_pdf_con_respuesta(respuesta_ia, output_pdf_path)
            
            # Mostrar mensaje de éxito y botón para descargar PDF
            page.add(ft.Text(f"PDF generado exitosamente: {output_pdf_path}"))
            page.add(ft.ElevatedButton("Abrir carpeta", on_click=lambda _: os.startfile(os.path.dirname(output_pdf_path))))
    
    # Estilo de la página
    page.title = "Conversor TXT a PDF con IA"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Contenedor de carga de archivo
    file_picker = ft.FilePicker(on_result=on_file_upload)
    page.overlay.append(file_picker)
    
    # Estructura de la interfaz
    page.add(
        ft.Column(
            [
                ft.Text("Sube tu archivo de texto (CSV o TXT)", size=20, weight=ft.FontWeight.BOLD),
                ft.ElevatedButton("Seleccionar archivo", on_click=lambda _: file_picker.pick_files(), width=200)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

# Ejecutar la aplicación Flet
ft.app(target=main)
