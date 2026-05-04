import os
	import psycopg2
from dotenv import load_dotenv

load_dotenv() 

def obtener_conexion():
    url = os.getenv("DB_URL")
    
    if not url:
        print("Error: No se pudo leer DB_URL del archivo .env")
        return None
        
    try:
        # Forzamos la conexión externa usando la URL
        conn = psycopg2.connect(url)
        return conn
    except Exception as e:
        print(f"❌ Error de conexión a la nube: {e}")
        return None
