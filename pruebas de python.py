import pandas as pd

edades = [25, 30, 35, 40]
print("SERIES") 
series_edades = pd.Series(edades)
print(series_edades)

datos = {     "Nombre": ["Ana", "Luis", "Carlos", "Sara"],     "Edad": [25, 30, 22, 28],     "Ciudad": ["Bogotá", "Medellín", "Cali", "Bogotá"] }
print("\nDATAFRAME")
df = pd.DataFrame(datos)
print("FUNCIONES PANDAS")
print("===============")
print("=====HEAD=====")
print(df.head()) #Muestra las primeras 5 filas del DataFrame
print("===============")
print(df.head(2)) #Muestra las primeras 2 filas del DataFrame
print("=====TAIL=====")
print(df.tail()) #Muestra las últimas 5 filas del DataFrame
print("===============")
print(df.tail(2)) #Muestra las últimas 2 filas del DataFrame
print("========INFO=======")
print(df.info()) #Información sobre el DataFrame
print("=======DESCRIBE========")
print(df.describe()) #Estadísticas descriptivas del DataFrame como conteo, media, desviación estándar, etc. para columnas numéricas
print("=======COLUMNA NOMBRE========")
print(df.columns)
print(df["Nombre"]) #Accede a la columna "Nombre" del DataFrame
print("=======SHAPE========")
print(df.shape) #Muestra el número de filas y columnas del DataFrame
print("=======ACCESO A DATOS========")
resumen = df[["Nombre", "Edad"]] #Accede a las columnas "Nombre" y "Edad" del DataFrame
print(resumen)
print("=======FILAS========")
lista = [1, 2, 3, 4, 5]
lista2 = lista[::] #Crea una copia de la lista original
lista2.append(6)
print(lista)

print("=======MODIFICACIÓN DE DATAFRAME========")
resumen["Correo"] = ["test@cesde.net", "correo@prueba.com",None,None] #Agrega una nueva columna "Correo" al DataFrame con los valores proporcionados
print(resumen)
print(df)