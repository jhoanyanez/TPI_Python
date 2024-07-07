from app.database import get_db

class Usuario:
    def __init__(self, id_usuario=None, nombre=None, apellido=None, nombre_usuario=None, correo=None, contrasenia=None, telefono=None, fecha_nacimiento=None):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.nombre_usuario = nombre_usuario
        self.correo = correo
        self.contrasenia = contrasenia
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento
    
    def save_user(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_usuario:
            cursor.execute("""
                UPDATE usuarios SET nombre = %s, apellido= %s, nombre_usuario= %s, correo= %s, contrasenia= %s, telefono= %s, fecha_nacimiento= %s 
                WHERE id_usuario = %s
            """, (self.nombre, self.apellido, self.nombre_usuario, self.correo, self.contrasenia, self.telefono, self.fecha_nacimiento, self.id_usuario))
        else:
            cursor.execute("""
                INSERT INTO usuarios (nombre, apellido, nombre_usuario, correo, contrasenia, telefono, fecha_nacimiento) VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (self.nombre, self.apellido, self.nombre_usuario, self.correo, self.contrasenia, self.telefono, self.fecha_nacimiento))
            self.id_usuario = cursor.lastrowid
        db.commit()
        cursor.close()

    @staticmethod
    def get_all_users():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT id_usuario, nombre, apellido, nombre_usuario, correo, contrasenia, telefono, fecha_nacimiento FROM usuarios")
        rows = cursor.fetchall()
        usuarios = [Usuario(id_usuario=row[0], nombre=row[1], apellido=row[2], nombre_usuario=row[3], correo=row[4], contrasenia=row[5], telefono=row[6], fecha_nacimiento=row[7]) for row in rows]
        cursor.close()
        return usuarios

    @staticmethod
    def get_by_user_id(id_usuario):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT id_usuario, nombre, apellido, nombre_usuario, correo, contrasenia, telefono, fecha_nacimiento FROM usuarios WHERE id_usuario = %s", (id_usuario,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Usuario(id_usuario=row[0], nombre=row[1], apellido=row[2], nombre_usuario=row[3], correo=row[4], contrasenia=row[5], telefono=row[6], fecha_nacimiento=row[7])
        else:
            return None

    def delete_user(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id_usuario = %s", (self.id_usuario,))
        db.commit()
        cursor.close()

    def get_quantity_users():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT COUNT(id_usuario) cantidad_usuarios FROM usuarios")
        row = cursor.fetchone()
        cursor.close()

    def serialize(self):
        return {
            'id_usuario': self.id_usuario,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'nombre_usuario': self.nombre_usuario,
            'correo': self.correo,
            'contrasenia': self.contrasenia,
            'telefono': self.telefono,
            'fecha_nacimiento': self.fecha_nacimiento
        }

    def __str__(self):
        return f"usuario: {self.id_usuario} - {self.nombre}"
