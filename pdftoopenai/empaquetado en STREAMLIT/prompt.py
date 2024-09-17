prompt = '''Por favor, analiza los datos de sensores proporcionados que corresponden a una sesión de entrenamiento de remo de un deportista profesional. Los datos consisten en registros de tiempo y lecturas de varios sensores, estructurados en cinco columnas:
 
Hora (formato HH:MM)
Fuerza: Representa la fuerza aplicada.
Ataque: Información adicional del sensor.
Salida: Ángulo de la pala.
Verticalidad: Aceleración de la pala.
Tu tarea es realizar el siguiente análisis y generar un informe completo, agrupado por ciclo de paladas:
 
1. Identificación de Ciclos de Palada
Criterio: Un ciclo de palada comienza cuando el valor de Fuerza supera las 15 unidades y termina cuando desciende por debajo de este valor.
Acción: Lista cada palada identificada con su hora de inicio y fin.
 
2. Análisis Detallado de Cada Palada
Para cada palada identificada, extrae y presenta:
 
Fuerza Máxima (Fuerza): El valor máximo de Fuerza durante la palada.
Ángulo Promedio (Salida): El promedio de los valores de Salida durante la palada.
Aceleración Máxima (Verticalidad): El valor máximo de Verticalidad durante la palada.
 
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
Asegúrate de que el informe sea coherente y fácil de seguir. 
Estos son los datos:
'''

prompt_2 ='''Te paso datos de sensores, las columnas corresponden a :"Tiempo,Fuerza,Ataque,Salida,Verticalidad" y analiza los ciclos de palada de un remero profesional. Los datos representan lecturas de sensores durante un entrenamiento de remo.
 
Por favor, realiza los siguientes análisis:
 
1. **Identificación de Ciclos de Palada**: Identifica los ciclos de palada, especificando las marcas de tiempo de inicio y fin de cada ciclo. Ten en cuenta que la columna "Verticalidad" es la que determina el ciclo de la palada. Lo más cercano a 0 será el inicio y el final del ciclo.
2. **Fuerza Máxima por Palada**: Extrae la fuerza máxima aplicada durante cada ciclo, basándote en los datos del sensor correspondiente de la columna "Fuerza".
3. **Ángulos y Aceleración**: Calcula el ángulo promedio  y la aceleración máxima para cada ciclo, teniendo en cuenta que "Ataque" es el ángulo de ataque y "Salida", el ángulo de salida.
4. **Observaciones Generales**: Proporciona observaciones sobre la variabilidad de la fuerza, la consistencia de los ángulos, y cualquier otro patrón relevante que puedas identificar.
5. **Puntos de mejora**: Identifica los puntos de mejora según
 
Genera un informe estructurado con los resultados de estos análisis, agrupado por ciclo de paladas.
 
(Cargar y procesar el contenido para realizar el análisis)
'''