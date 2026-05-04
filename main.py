from database import obtener_conexion

def probar_conexion():
    print("--- Iniciando prueba de conexión a la nube de Omferza ---")
    conn = obtener_conexion()
    
    if conn:
        print("¡Conexión exitosa a Supabase!")
        cur = conn.cursor()
        # Una consulta simple para verificar la versión de la base de datos
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        print(f"Servidor: {db_version[0]}")
        
        cur.close()
        conn.close()
        print("--- Prueba finalizada con éxito ---")
    else:
        print("Subiste el código pero la base de datos no respondió.")

if __name__ == "__main__":
    probar_conexion()
