import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
from app.models.usuario import Usuario
from app.models.producto import Producto
from app.models.categoria import Categoria
from app.database import init_app, init_db

d = os.path.dirname(__file__)
os.chdir(d)

# Configuración inicial
app = Flask(__name__)
CORS(app)
init_app(app)


# Ruta para inicializar la base de datos
@app.route('/init-db')
def init_db_route():
    init_db()
    return "Base de datos inicializada correctamente."

# Ruta principal
@app.route('/')
def principal():
    return "¡Hola! Esta es la API para gestionar productos y categorias."

### Gestión de productos ###

# Crear un producto
@app.route('/productos', methods=['POST'])
def create_producto():
    data = request.json
    nuevo_producto = Producto(nombre=data['nombre'], descripcion=data['descripcion'], precio=data['precio'], cantidad=data['cantidad'], imagen=data['imagen'])
    nuevo_producto.save_product()

    # Asociar las categorias al producto en la tabla productos_categorias
    categorias = data.get('categorias', [])  # Lista de IDs de categorias para el producto
    for categoria_id in categorias:
        nuevo_producto.add_category(categoria_id)
    return jsonify({'message': 'producto creado correctamente'}), 201

# Obtener todos los productos
@app.route('/productos', methods=['GET'])
def get_all_productos():
    productos = Producto.get_all_products()
    return jsonify([producto.serialize() for producto in productos])

# Obtener un producto por su ID
@app.route('/productos/<int:id_producto>', methods=['GET'])
def get_by_id_producto(id_producto):
    producto = Producto.get_by_product_id(id_producto)
    if producto:
        return jsonify(producto.serialize())
    else:
        return jsonify({'message': 'producto no encontrado'}), 404

# Eliminar un producto por su ID
@app.route('/productos/<int:id_producto>', methods=['DELETE'])
def delete_producto(id_producto):
    producto = Producto.get_by_product_id(id_producto)
    if not producto:
        return jsonify({'message': 'producto no encontrado'}), 404
    producto.delete_product()
    return jsonify({'message': 'El producto fue eliminado correctamente'})

# Actualizar un producto por su ID
@app.route('/productos/<int:id_producto>', methods=['PUT'])
def update_producto(id_producto):
    producto = Producto.get_by_product_id(id_producto)
    if not producto:
        return jsonify({'message': 'Producto no encontrado'}), 404

    data = request.json
    producto.nombre = data.get('nombre', producto.nombre)
    producto.descripcion = data.get('descripcion', producto.descripcion)
    producto.precio = data.get('precio', producto.precio)
    producto.cantidad = data.get('cantidad', producto.cantidad)
    producto.imagen = data.get('imagen', producto.imagen)

    # Actualizar las categorías asociadas al producto
    nuevas_categorias = data.get('categorias', [])
    producto.update_categories(nuevas_categorias)

    producto.save_product()
    return jsonify({'message': 'Producto actualizado correctamente'})

### Gestión de categorias ###
# Crear un categoria
@app.route('/categorias', methods=['POST'])
def create_categoria():
    data = request.json
    nuevo_categoria = Categoria(nombre=data['nombre'])
    nuevo_categoria.save_category()
    return jsonify({'message': 'Categoria creada correctamente'}), 201

# Obtener todos los categorias
@app.route('/categorias', methods=['GET'])
def get_all_categorias():
    categorias = Categoria.get_all_categories()
    return jsonify([categoria.serialize() for categoria in categorias])

# Obtener un categoria por su ID
@app.route('/categorias/<int:id_categoria>', methods=['GET'])
def get_by_id_categoria(id_categoria):
    categoria = Categoria.get_by_category_id(id_categoria)
    if categoria:
        return jsonify(categoria.serialize())
    else:
        return jsonify({'message': 'categoria no encontrada'}), 404

# Eliminar un categoria por su ID
@app.route('/categorias/<int:id_categoria>', methods=['DELETE'])
def delete_categoria(id_categoria):
    categoria = Categoria.get_by_category_id(id_categoria)
    if not categoria:
        return jsonify({'message': 'categoria no encontrada'}), 404
    categoria.delete_category()
    return jsonify({'message': 'El categoria fue eliminada correctamente'})

# Actualizar un categoria por su ID
@app.route('/categorias/<int:id_categoria>', methods=['PUT'])
def update_categoria(id_categoria):
    categoria = Categoria.get_by_category_id(id_categoria)
    if not categoria:
        return jsonify({'message': 'categoria no encontrada'}), 404
    data = request.json
    categoria.nombre = data.get('nombre', categoria.nombre)
    categoria.save_category()
    return jsonify({'message': 'categoria actualizada correctamente'})


### Gestión de usuarios ###
# Crear un usuario
@app.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.json
    nuevo_usuario = Usuario(nombre=data['nombre'], apellido=data['apellido'], nombre_usuario=data['nombre_usuario'], correo=data['correo'], contrasenia=data['contrasenia'], telefono=data['telefono'], fecha_nacimiento=data['fecha_nacimiento']) 
    nuevo_usuario.save_user()
    return jsonify({'message': 'Usuario creado correctamente'}), 201

# Obtener todos los usuarios
@app.route('/usuarios', methods=['GET'])
def get_all_usuarios():
    usuarios = Usuario.get_all_users()
    return jsonify([usuario.serialize() for usuario in usuarios])

# Obtener un usuario por su ID
@app.route('/usuarios/<int:id_usuario>', methods=['GET'])
def get_by_id_usuario(id_usuario):
    usuario = Usuario.get_by_user_id(id_usuario)
    if usuario:
        return jsonify(usuario.serialize())
    else:
        return jsonify({'message': 'usuario no encontrado'}), 404

# Eliminar un usuario por su ID
@app.route('/usuarios/<int:id_usuario>', methods=['DELETE'])
def delete_usuario(id_usuario):
    usuario = Usuario.get_by_user_id(id_usuario)
    if not usuario:
        return jsonify({'message': 'usuario no encontrado'}), 404
    usuario.delete_user()
    return jsonify({'message': 'El usuario fue eliminado correctamente'})

# Actualizar un usuario por su ID
@app.route('/usuarios/<int:id_usuario>', methods=['PUT'])
def update_usuario(id_usuario):
    usuario = Usuario.get_by_user_id(id_usuario)
    if not usuario:
        return jsonify({'message': 'usuario no encontrad0'}), 404
    data = request.json
    usuario.nombre = data.get('nombre', usuario.nombre)
    usuario.apellido = data.get('apellido', usuario.apellido)
    usuario.nombre_usuario = data.get('nombre_usuario', usuario.nombre_usuario)
    usuario.correo = data.get('correo', usuario.correo)
    usuario.contrasenia = data.get('contrasenia', usuario.contrasenia)
    usuario.telefono = data.get('telefono', usuario.telefono)
    usuario.fecha_nacimiento = data.get('fecha_nacimiento', usuario.fecha_nacimiento)
    usuario.save_user()
    return jsonify({'message': 'usuario actualizado correctamente'})


# Obtener los datos estadisticos de usuarios, productos y categorias
@app.route('/dashboard', methods=['GET'])
def get_statistics():
    cantidad_usuarios = Usuario.get_quantity_users()
    cantidad_categorias = Categoria.get_quantity_categories()
    cantidad_productos = Producto.get_quantity_products()
    return jsonify({'message': 'Estadisticas'})


# Ejecutar la aplicación si este archivo es el punto de entrada principal
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
