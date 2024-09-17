prompt = '''Por favor, analiza los datos de sensores proporcionados que corresponden a una sesión de entrenamiento de remo de un deportista profesional. Los datos consisten en registros de tiempo y lecturas de varios sensores, estructurados en cinco columnas:
 
Hora (formato HH:MM)
Sensor1: Representa la fuerza aplicada.
Sensor2: Información adicional del sensor.
Sensor3: Ángulo de la pala.
Sensor4: Aceleración de la pala.
Tu tarea es realizar el siguiente análisis y generar un informe completo:
 
1. Identificación de Ciclos de Palada
Criterio: Un ciclo de palada comienza cuando el valor de Sensor1 supera las 15 unidades y termina cuando desciende por debajo de este valor.
Acción: Lista cada palada identificada con su hora de inicio y fin.
 
2. Análisis Detallado de Cada Palada
Para cada palada identificada, extrae y presenta:
 
Fuerza Máxima (Sensor1): El valor máximo de Sensor1 durante la palada.
Ángulo Promedio (Sensor3): El promedio de los valores de Sensor3 durante la palada.
Aceleración Máxima (Sensor4): El valor máximo de Sensor4 durante la palada.
 
3. Observaciones Generales
Comenta sobre patrones observados en los datos, como incrementos o decrementos en la fuerza aplicada, consistencia en los ángulos y variabilidad en la aceleración.
Las observaciones deben basarse únicamente en la información extraída de este entrenamiento específico.
 
4. Recomendaciones Técnicas Basadas en el Entrenamiento
Proporciona recomendaciones técnicas para mejorar el rendimiento del remero, basadas exclusivamente en los datos analizados de este entrenamiento.
Enfócate en aspectos técnicos como la aplicación de fuerza, ángulos de remo, aceleración, ritmo y cadencia.
 
5. Presentación del Informe
Organiza la información en un informe estructurado con los siguientes apartados:
 
Introducción
Análisis de los Datos
Identificación de Ciclos de Palada
Detalles de los Ciclos de Palada
Observaciones Generales
Recomendaciones Técnicas Basadas en el Entrenamiento
Conclusiones
 
6. Formato y Estilo
Utiliza encabezados y subencabezados claros.
Presenta los datos de manera ordenada y legible.
Redacta el informe en español con un tono profesional y técnico.
Asegúrate de que el informe sea coherente y fácil de seguir.'''