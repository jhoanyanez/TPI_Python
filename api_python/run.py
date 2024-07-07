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
        return jsonify({'message': 'producto no encontrado'}), 404
    data = request.json
    producto.nombre = data.get('nombre', producto.nombre)
    producto.descripcion = data.get('descripcion', producto.descripcion)
    producto.precio = data.get('precio', producto.precio)
    producto.cantidad = data.get('cantidad', producto.cantidad)
    producto.save_product()
    return jsonify({'message': 'producto actualizado correctamente'})

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

# Ejecutar la aplicación si este archivo es el punto de entrada principal
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
