#main.py
import pandas as pd
import os
from datetime import datetime
import csv


# Ruta de los archivos
ruta_proveedores = 'Proveedores/Proveedores.xlsx'
carpeta_productos = 'Productos/'
carpeta_precios = 'Precios/'
carpeta_facturas = 'Facturas/'
carpeta_boletas = 'Boletas/'

# Diccionario para mapear nombres de meses en español a inglés
meses_espanol_a_ingles = {'enero': 'January','febrero': 'February','marzo': 'March',
    'abril': 'April','mayo': 'May','junio': 'June','julio': 'July','agosto': 'August',
    'septiembre': 'September','octubre': 'October','noviembre': 'November','diciembre': 'December'
}


def cargar_datos_proveedores(ruta_proveedores):
    df_proveedores = pd.read_excel(ruta_proveedores)
    df_proveedores = df_proveedores.rename(columns={
        'ID': 'ID_Proveedor',
        'Contacto comercial': 'Contacto_Comercial',
        'Teléfono': 'Telefono'
    })
    return df_proveedores


# Funcion para extraer datos 
def cargar_datos_productos(carpeta_productos):
    dataframes_pro = []

    for archivo in os.listdir(carpeta_productos):
        if archivo.endswith('.xlsx'):
            ruta_archivo = os.path.join(carpeta_productos, archivo)
            df_producto = pd.read_excel(ruta_archivo)
            df_producto = df_producto.rename(columns={
                'ID': 'ID_Producto',
                'Categoría': 'Categoria',
                'Sub-categoría': 'Subcategoria'
            })
            dataframes_pro.append(df_producto)

    df_total_productos = pd.concat(dataframes_pro, ignore_index=True)
    return df_total_productos

def cargar_datos_precios(carpeta_precios):
    dataframes_pre = []

    for anio in os.listdir(carpeta_precios):
        ruta_anio = os.path.join(carpeta_precios, anio)
        
        if os.path.isdir(ruta_anio):
            for mes in os.listdir(ruta_anio):
                ruta_mes = os.path.join(ruta_anio, mes)
                
                if os.path.isdir(ruta_mes):
                    for archivo in os.listdir(ruta_mes):
                        if archivo.endswith('.csv'):
                            ruta_archivo = os.path.join(ruta_mes, archivo)

                            df_precio = pd.read_csv(ruta_archivo)
                            df_precio = df_precio.rename(columns={'Identificador': 'ID_Precio'})
                            df_precio['Anio'] = anio
                            df_precio['Mes'] = mes
                            dataframes_pre.append(df_precio)

    df_total_precios = pd.concat(dataframes_pre, ignore_index=True)
    return df_total_precios

def cargar_datos_facturas(carpeta_facturas, meses_espanol_a_ingles):
    dataframes_fac = []

    for año in os.listdir(carpeta_facturas):
        ruta_año = os.path.join(carpeta_facturas, año)
        
        if os.path.isdir(ruta_año):
            for mes in os.listdir(ruta_año):
                ruta_mes = os.path.join(ruta_año, mes)
                
                if os.path.isdir(ruta_mes):
                    for archivo in os.listdir(ruta_mes):
                        if archivo.endswith('.csv'):
                            ruta_archivo = os.path.join(ruta_mes, archivo)

                            filas_procesadas = []

                            with open(ruta_archivo, 'r') as archivo_csv:
                                lector_csv = csv.reader(archivo_csv)
                                next(lector_csv)

                                for fila in lector_csv:
                                    boleta = fila[0]
                                    total = fila[-1]
                                    productos = fila[1:-1]
                                    filas_procesadas.append([boleta, ','.join(productos), total])

                            df_factura = pd.DataFrame(filas_procesadas, columns=['ID_Boleta', 'Productos', 'PrecioTotal'])
                            partes_nombre = archivo.lower().replace("facturas", "").replace(".csv", "").split('-')
                            dia_archivo = partes_nombre[0]
                            nombre_mes = partes_nombre[1]
                            año_archivo = partes_nombre[-1]
                            df_factura['Anio'] = año_archivo
                            df_factura['Mes'] = nombre_mes
                            df_factura['Dia'] = dia_archivo
                            dataframes_fac.append(df_factura)

    df_total_facturas = pd.concat(dataframes_fac, ignore_index=True)
    return df_total_facturas

def cargar_datos_boletas(carpeta_boletas, meses_espanol_a_ingles):
    dataframes_bol = []

    for año in os.listdir(carpeta_boletas):
        ruta_año = os.path.join(carpeta_boletas, año)
        
        if os.path.isdir(ruta_año):
            for mes in os.listdir(ruta_año):
                ruta_mes = os.path.join(ruta_año, mes)
                
                if os.path.isdir(ruta_mes):
                    for archivo in os.listdir(ruta_mes):
                        if archivo.endswith('.csv'):
                            ruta_archivo = os.path.join(ruta_mes, archivo)

                            filas_procesadas = []

                            with open(ruta_archivo, 'r') as archivo_csv:
                                lector_csv = csv.reader(archivo_csv)
                                next(lector_csv)

                                for fila in lector_csv:
                                    boleta = fila[0]
                                    total = fila[-1]
                                    productos = fila[1:-1]
                                    filas_procesadas.append([boleta, ','.join(productos), total])

                            df_boleta = pd.DataFrame(filas_procesadas, columns=['ID_Boleta', 'Productos', 'PrecioTotal'])
                            partes_nombre = archivo.lower().replace("boletas", "").replace(".csv", "").split('-')
                            día_archivo = partes_nombre[0]
                            nombre_mes = partes_nombre[1]
                            año_archivo = partes_nombre[-1]
                            df_boleta['Anio'] = año_archivo
                            df_boleta['Mes'] = nombre_mes
                            df_boleta['Dia'] = día_archivo
                            dataframes_bol.append(df_boleta)

    df_total_boletas = pd.concat(dataframes_bol, ignore_index=True)
    return df_total_boletas




df_proveedores = cargar_datos_proveedores(ruta_proveedores)
df_total_productos = cargar_datos_productos(carpeta_productos)
df_total_precios = cargar_datos_precios(carpeta_precios)
df_total_facturas = cargar_datos_facturas(carpeta_facturas, meses_espanol_a_ingles)
df_total_boletas = cargar_datos_boletas(carpeta_boletas, meses_espanol_a_ingles)




# Mostrar las primeras filas del DataFrame (head)
#print(df_proveedores.head(5))
#println("")
#print(df_total_productos.head(5))
#println("")
#print(df_total_precios.head(5))
#print(df_total_precios.iloc[10000:20000].to_string(index=False))
#println("")
#print(df_total_facturas.head(5))
#println("")
#print(df_total_boletas.head(5))
#println("")


from sqlalchemy import create_engine

# Ajusta estas variables según tus configuraciones de PostgreSQL
nombre_bd = 'IDD_DB'
usuario_bd = 'postgres'
contraseña_bd = '1234'
host_bd = 'localhost'  # Por ejemplo, 'localhost'
puerto_bd = '5433'  # Por ejemplo, 5432

# Crear una conexión a la base de datos PostgreSQL
engine = create_engine(f'postgresql://{usuario_bd}:{contraseña_bd}@{host_bd}:{puerto_bd}/{nombre_bd}', echo=True)

# Cargar los DataFrames en la base de datos
df_proveedores.to_sql('dim_proveedores', con=engine, index=False, if_exists='replace', schema='public')
df_total_productos.to_sql('dim_productos', con=engine, index=False, if_exists='replace', schema='public')
df_total_precios.to_sql('dim_precios', con=engine, index=False, if_exists='replace', schema='public')
df_total_boletas.to_sql('dim_boletas', con=engine, index=False, if_exists='replace', schema='public')
df_total_facturas.to_sql('fact_table', con=engine, index=False, if_exists='replace', schema='public')

# Imprimir mensaje de éxito
print("Datos cargados en la base de datos PostgreSQL con éxito.")
