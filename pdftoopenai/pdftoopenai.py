import pandas as pd
from fpdf import FPDF
import openai
import os

# Configurar la API Key desde las variables de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

# Función para leer el archivo .txt y convertirlo en un DataFrame
def leer_txt_a_dataframe(file_path):
    """Lee un archivo .txt y lo convierte en un DataFrame de pandas."""
    df = pd.read_csv(file_path, header=None, names=["Tiempo", "Fuerza", "Ataque", "Salida", "Verticalidad"]) # Cambia los nombres según tu archivo
    return df 

# Función para enviar el contenido a la IA con el nuevo formato de la API
def enviar_a_ia(dataframe, prompt):
    """Envía el DataFrame a la IA y devuelve la respuesta. Hay que indicar el modelo que se va a usar, también se puede cambiar el prompt."""
    contenido = dataframe.to_string(index=False)  # Convierte el DataFrame a string
    mensaje_completo = f"{prompt}\n\n{contenido}" # Combina el prompt con el contenido del DataFrame
    
    # Mensajes de entrada para la IA
    messages = [
        {"role": "system", "content": "Eres un asistente útil que analiza datos de entrenamiento."}, # Mensaje del sistema que define el rol de la IA
        {"role": "user", "content": mensaje_completo} # Mensaje del usuario que incluye el prompt y el contenido
    ]
    
    # Realizar la solicitud a la IA
    completion = openai.chat.completions.create(
        model="gpt-4o-2024-08-06",  # según veo en la documentación de la api, este es el modelo más barato, siendo superior al 4.
        messages=messages
    )
    
    # Extraer la respuesta de la IA
    respuesta_ia = completion.choices[0].message.content # Extrae la respuesta de la IA
    
    return respuesta_ia

# Función para generar el PDF con la respuesta de la IA
def generar_pdf_con_respuesta(respuesta, output_pdf_path):
    pdf = FPDF() # Crea un objeto PDF 
    pdf.add_page() # Añade una página al PDF (añadir salto de linea)
    pdf.set_font("Arial", size=12)
    
    # Definir el ancho de la celda para justificar el texto
    ancho_celda = 190  # Ancho en milímetros para ajustarse a la página
    
    # Añadir contenido de la respuesta al PDF
    for linea in respuesta.split('\n'):
        pdf.multi_cell(ancho_celda, 10, linea)  # Usa multi_cell para ajustar el texto al ancho de la celda (justificado)
    
    pdf.output(output_pdf_path) # Guarda el PDF en la ruta especificada, en este caso, en donde está almacenado el archivo .py


def procesar_txt_y_generar_pdf(txt_file_path, prompt):
    """Procesa el archivo .txt y genera un PDF con la respuesta de la IA."""
    # Leer el archivo .txt como DataFrame
    df = leer_txt_a_dataframe(txt_file_path)
    
    # Enviar el contenido del DataFrame a la IA junto con el prompt
    respuesta_ia = enviar_a_ia(df, prompt)
    
    # Nombre del archivo PDF basado en el archivo de entrada
    output_pdf_path = f"{os.path.splitext(txt_file_path)[0]}_ia_respuesta.pdf"
    
    # Generar el PDF con la respuesta de la IA
    generar_pdf_con_respuesta(respuesta_ia, output_pdf_path)
    
    return output_pdf_path

# Ejemplo de uso
if __name__ == "__main__":
    txt_file_path = "archivo_formateado.txt"  # El archivo .txt formateado
    prompt = "Por favor, analiza los datos siguientes:"  # prompt personalizado

    # Verificar si el archivo existe
    if not os.path.exists(txt_file_path):
        raise FileNotFoundError(f"No se encuentra el archivo: {txt_file_path}")
    
    pdf_generado = procesar_txt_y_generar_pdf(txt_file_path, prompt)
    
    print(f"El PDF generado se encuentra en: {pdf_generado}")
