import os 
# pip install mysql-connector-python
import mysql.connector  # Importa el conector MySQL para conectar con la base de datos
from flask import g  # Importa g de Flask para almacenar datos durante la petición
# pip install python-dotenv
from dotenv import load_dotenv  

d = os.path.dirname(__file__)
os.chdir(d)

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la base de datos usando variables de entorno
# DATABASE_CONFIG = {
#     'user': os.getenv('DB_USERNAME'),  
#     'password': os.getenv('DB_PASSWORD'),  
#     'host': os.getenv('DB_HOST'),  
#     'database': os.getenv('DB_NAME'),  
#     'port': os.getenv('DB_PORT', 3306)  # Puerto del servidor de la base de datos, por defecto es 3306 si no se especifica
# }

DATABASE_CONFIG = {
    'user':"root",  
    'password': "admin",  
    'host': "127.0.0.1",  
    'database': "ecommerce",  
    'port': 3306  # Puerto del servidor de la base de datos, por defecto es 3306 si no se especifica
}


# Función para obtener la conexión de la base de datos
def get_db():
    # Si no hay una conexión a la base de datos en g, la creamos
    # g, que es un objeto de Flask que se usa para almacenar datos durante la vida útil de una solicitud.
    if 'db' not in g:
        print("···· Abriendo conexion a DB ····",DATABASE_CONFIG['database']," ---- ",DATABASE_CONFIG['user'])
        g.db = mysql.connector.connect(**DATABASE_CONFIG)
    # Retorna la conexión a la base de datos
    return g.db

# Función para cerrar la conexión a la base de datos
def close_db(e=None):
    # Intenta obtener la conexión de la base de datos desde g
    db = g.pop('db', None)
    # Si hay una conexión, la cerramos
    if db is not None:
        print("···· Cerrando conexion a DB ····")
        db.close()
# Función para inicializar la base de datos
def init_db():
    db = get_db()
    cursor = db.cursor()

    # Crear tablas si no existen con todas las claves e índices incluidos
    sql_commands = [
    """CREATE TABLE `productos` (
    `id_producto` int NOT NULL AUTO_INCREMENT,
        `nombre` varchar(50) NOT NULL,
        `descripcion` varchar(500) NOT NULL,
        `precio` decimal(8,2) NOT NULL,
        `cantidad` int(10) NOT NULL,
        `imagen` varchar(500) NOT NULL,
        PRIMARY KEY (`id_producto`)
    );""",
     """CREATE TABLE categorias (
        `id_categoria` int NOT NULL AUTO_INCREMENT,
        `nombre` varchar(50) NOT NULL,
        PRIMARY KEY (`id_categoria`),
        UNIQUE INDEX `name_UNIQUE` (`nombre` ASC) VISIBLE
    );""",
    
    """CREATE TABLE `productos_categorias` (
        `id_producto_categoria` int NOT NULL AUTO_INCREMENT,
        `id_producto` int DEFAULT NULL,
        `id_categoria` int DEFAULT NULL,
        PRIMARY KEY (`id_producto_categoria`),
        KEY `id_productos_idx` (`id_producto`),
        KEY `id_categorias_idx` (`id_categoria`),
        CONSTRAINT `id_categorias` FOREIGN KEY (`id_categoria`) REFERENCES `categorias` (`id_categoria`),
        CONSTRAINT `id_productos` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`id_producto`)
    );""",

    """CREATE TABLE `usuarios` (
        `id_usuario` int NOT NULL AUTO_INCREMENT,
        `nombre` varchar(50) NOT NULL,
        `apellido` varchar(50) NOT NULL,
        `nombre_usuario` varchar(50) NOT NULL,
        `correo` varchar(50) NOT NULL,
        `contrasenia` varchar(50) NOT NULL,
        `telefono` varchar(50) NOT NULL,
        `fecha_nacimiento` datetime NOT NULL,
        PRIMARY KEY (`id_usuario`),
        UNIQUE KEY `nombre_usuario_UNIQUE` (`nombre_usuario`),
        UNIQUE KEY `correo_UNIQUE` (`correo`)
    );"""
]

    for command in sql_commands:
        cursor.execute(command)

    db.commit()

    # Inserciones de categorias si no existen
    cursor.execute("""
        INSERT INTO categorias (nombre) VALUES
            ('Smartphones'), ('Notebooks'), ('Watches'), ('Tablets'), ('Games'),
            ('Accesories')
        ON DUPLICATE KEY UPDATE nombre=nombre;
    """)

    db.commit()
    cursor.close()

# Función para inicializar la aplicación con el cierre automático de la conexión a la base de datos
def init_app(app):
    # Registrar la función close_db para que se llame automáticamente
    # cuando el contexto de la aplicación se destruye
    app.teardown_appcontext(close_db)
