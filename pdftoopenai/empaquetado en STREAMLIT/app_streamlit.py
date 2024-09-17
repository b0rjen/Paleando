import streamlit as st
import pandas as pd
import openai
import os
from prompt import prompt # Asegúrate de que el archivo prompt.py esté en el mismo directorio

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
        model="gpt-4-turbo",  # Usa el modelo que prefieras
        messages=messages
    )
    
    return completion.choices[0].message.content

# Interfaz Streamlit
st.title("Análisis de archivos TXT con IA")

# Cargar archivo .txt
txt_file = st.file_uploader("Sube tu archivo de texto (CSV o TXT)", type=["txt", "csv"])

if txt_file is not None:
    # Guardar temporalmente el archivo subido en el directorio actual
    file_path = txt_file.name  # Guardar con el mismo nombre del archivo
    with open(file_path, "wb") as f:
        f.write(txt_file.getbuffer())
    
    # Leer el archivo como DataFrame
    df = leer_txt_a_dataframe(file_path)
    st.write("Contenido del archivo cargado:")
    st.dataframe(df)

    # Enviar contenido a la IA
    if st.button("Enviar a IA"):
        prompt = prompt
        respuesta_ia = enviar_a_ia(df, prompt)
        
        # Mostrar la respuesta de la IA en una caja de texto
        st.text_area("Respuesta de la IA:", respuesta_ia, height=300)
