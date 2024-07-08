from app.database import get_db

class Producto:
    def __init__(self, id_producto=None, nombre=None, descripcion=None, precio=None, cantidad=None, imagen=None, categorias=[]):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad
        self.imagen = imagen
        self.categorias = categorias

    def save_product(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_producto:
            cursor.execute("""
                UPDATE productos SET nombre = %s, descripcion = %s, precio = %s, cantidad = %s, imagen = %s
                WHERE id_producto = %s
            """, (self.nombre, self.descripcion, self.precio, self.cantidad, self.imagen, self.id_producto))
        else:
            cursor.execute("""
                INSERT INTO productos (nombre, descripcion, precio, cantidad, imagen) VALUES (%s, %s, %s, %s, %s)
            """, (self.nombre, self.descripcion, self.precio, self.cantidad, self.imagen))
            self.id_producto = cursor.lastrowid
        db.commit()
        cursor.close()

    @staticmethod
    def get_all_products():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT id_producto, nombre, descripcion, precio, cantidad, imagen FROM productos")
        rows = cursor.fetchall()

        productos = []
        for row in rows:
            producto = Producto(id_producto=row[0], nombre=row[1], descripcion=row[2], precio=row[3], cantidad=row[4], imagen=row[5])
            producto.categorias = Producto.get_categories_of_products(producto.id_producto)
            productos.append(producto)

        cursor.close()
        return productos

    @staticmethod
    def get_by_product_id(id_producto):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT id_producto, nombre, descripcion, precio, cantidad, imagen FROM productos WHERE id_producto = %s", (id_producto,))
        row = cursor.fetchone()
        cursor.close()

        if row:
            producto = Producto(id_producto=row[0], nombre=row[1], descripcion=row[2], precio=row[3], cantidad=row[4], imagen=row[5])
            producto.categorias = Producto.get_categories_of_products(id_producto)
            return producto
        else:
            return None

    @staticmethod
    def get_categories_of_products(id_producto):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            SELECT c.id_categoria, c.nombre
            FROM productos_categorias pc
            JOIN categorias c ON pc.id_categoria = c.id_categoria
            WHERE pc.id_producto = %s
        """, (id_producto,))
        categorias = cursor.fetchall()
        cursor.close()
        return categorias

    def add_category(self, id_categoria):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO productos_categorias (id_producto, id_categoria) VALUES (%s, %s)", (self.id_producto, id_categoria))
        db.commit()
        cursor.close()

    def delete_product(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM productos WHERE id_producto = %s", (self.id_producto,))
        db.commit()
        cursor.close()

    def get_quantity_products():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT COUNT(id_producto) cantidad_productos FROM productos")
        row = cursor.fetchone()
        cursor.close()

    def serialize(self):
        return {
            'id_producto': self.id_producto,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'precio': self.precio,
            'cantidad': self.cantidad,
            'imagen': self.imagen,
            'categorias': [{'id_categoria': dep[0], 'nombre': dep[1]} for dep in self.categorias]
        }

    def __str__(self):
        return f"producto: {self.id_producto} - {self.nombre} {self.descripcion}"

