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

print("=========================================================================")

data = pd.read_csv("MOCK_DATA.csv")
print("===HEAD===")
print(data.head())
print("==TAIL===")
print(data.tail())
print("==INFO===")
print(data.info())
data["Precio_Total"] = data["Cantidad"] * data["Precio_Unitario"]
print(data["Precio_Total"])
promedio_total = data["Precio_Total"].mean()
suma_total = data["Precio_Total"].sum()

print(f"El promedio es , {promedio_total}:.2f")
print(f"El suma de precios es , {suma_total}:.2f")

print("=========================================================================")

data1 = pd.read_csv("MOCK_DATA_1.csv")
print("===HEAD===")
print(data1.head())
print("==TAIL===")
print(data1.tail())
print("==INFO===")
print(data1.info())
data1["Precio_Total"] = data1["Cantidad"] * data1["Precio_Unitario"]
print(data1["Precio_Total"])
promedio_total = data1["Precio_Total"].mean()
suma_total = data1["Precio_Total"].sum()
print("=========================================================================")
print(f"El promedio es , {promedio_total}:.2f")
print(f"El suma de precios es , {suma_total}:.2f")
print(data1.isna())
cant_nulos = data1.isna().sum()
print(cant_nulos)
duplicate_cant = data1.duplicated().sum()
print(duplicate_cant)
print("=========================================================================")
otra_variable = data1.dropna()
print(otra_variable.info())
print(otra_variable)
print("=========================================================================")
nueva_varibale = data1 
data1['Vendedor'] = data1['Vendedor'].fillna('n/a')
print(data1['Vendedor'])
print("=========================================================================")
nueva_varibale = data1 
data1['Ciudad'] = data1['Ciudad'].fillna('n/a')
print(data1['Ciudad'])
print("=========================================================================")

filtro_ciudades = data1[data1["Ciudad"] == "Río Alejandro"]

print(filtro_ciudades)
print("=========================================================================")
data1['Producto'] = data1['Producto'].str.upper()
print(data1['Producto'])