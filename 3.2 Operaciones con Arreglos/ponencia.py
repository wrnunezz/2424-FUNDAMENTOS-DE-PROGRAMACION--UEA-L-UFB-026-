import pandas as pd

# Cargar el archivo Excel
archivo_excel = "encuesta_bien.xlsx"
df = pd.read_excel(archivo_excel)

# Mostrar las primeras filas para asegurarnos que la estructura es correcta
print(df.head())

# Calcular la media y desviación estándar para cada sección de la encuesta
# Aquí suponemos que las columnas relevantes comienzan a partir de la columna 4 (después de 'Semestre', 'Sexo', 'Región')
seccion_1 = df.iloc[:, 9:11]  # Competencias Técnicas y Familiaridad
seccion_2 = df.iloc[:, 12:15]  # Facilidad de Uso y Funcionalidades
seccion_3 = df.iloc[:, 16:]   # Impacto en la Comprensión

# Cálculo de la media y desviación estándar para cada sección
media_seccion_1 = seccion_1.mean()
desviacion_seccion_1 = seccion_1.std()

media_seccion_2 = seccion_2.mean()
desviacion_seccion_2 = seccion_2.std()

media_seccion_3 = seccion_3.mean()
desviacion_seccion_3 = seccion_3.std()

# Mostrar los resultados
print("Media - Sección 1 (Competencias Técnicas y Familiaridad):")
print(media_seccion_1)
print("\nDesviación estándar - Sección 1:")
print(desviacion_seccion_1)

print("\nMedia - Sección 2 (Facilidad de Uso y Funcionalidades):")
print(media_seccion_2)
print("\nDesviación estándar - Sección 2:")
print(desviacion_seccion_2)

print("\nMedia - Sección 3 (Impacto en la Comprensión de Programación):")
print(media_seccion_3)
print("\nDesviación estándar - Sección 3:")
print(desviacion_seccion_3)
