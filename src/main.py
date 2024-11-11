import mysql.connector
from traductor import TraductorUSQL  # Importa el parser que convierte de USQL a SQL

def ejecutar_consulta_sql(sql_query):
    # Conexión a la base de datos MySQL
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pr0gramacion!",
        database="base_de_datos_entregable3"
    )
    
    cursor = conexion.cursor()
    cursor.execute(sql_query)
    
    # Obtén todos los resultados
    resultados = cursor.fetchall()
    
    # Cierra la conexión
    cursor.close()
    conexion.close()
    
    return resultados

def main():
    # Ejemplo de consulta en USQL
    while True:
        consulta_usql = input("Ingresa la consulta en USQL o escribe 'salir' para terminar: ")

        if consulta_usql.lower() == 'salir':
            print("Finalizando el programa.")
            break
    
    # Traducir la consulta de USQL a SQL usando el traductor
        traductor = TraductorUSQL()
        consulta_sql = traductor.parse(consulta_usql)
        print(consulta_sql)
    
    # Ejecutar la consulta SQL y obtener resultados
        resultados = ejecutar_consulta_sql(consulta_sql)
    
    # Mostrar los resultados
        for fila in resultados:
            print(fila)

if __name__ == "__main__":
    main()
