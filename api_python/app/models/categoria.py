from app.database import get_db

class Categoria:
    def __init__(self, id_categoria=None, nombre=None):
        self.id_categoria = id_categoria
        self.nombre = nombre

    def save_category(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_categoria:
            cursor.execute("UPDATE categorias SET nombre = %s WHERE id_categoria = %s", (self.nombre, self.id_categoria))
        else:
            cursor.execute("INSERT INTO categorias (nombre) VALUES (%s)", (self.nombre,))
            self.id_categoria = cursor.lastrowid
        db.commit()
        cursor.close()

    @staticmethod
    def get_all_categories():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT id_categoria, nombre FROM categorias")
        rows = cursor.fetchall()
        categorias = [Categoria(id_categoria=row[0], nombre=row[1]) for row in rows]
        cursor.close()
        return categorias

    @staticmethod
    def get_by_category_id(id_categoria):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT id_categoria, nombre FROM categorias WHERE id_categoria = %s", (id_categoria,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Categoria(id_categoria=row[0], nombre=row[1])
        else:
            return None

    def delete_category(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM categorias WHERE id_categoria = %s", (self.id_categoria,))
        db.commit()
        cursor.close()

    def serialize(self):
        return {
            'id_categoria': self.id_categoria,
            'nombre': self.nombre
        }

    def __str__(self):
        return f"Categoria: {self.id_categoria} - {self.nombre}"
