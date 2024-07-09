
/*Insertar Categorias*/
INSERT INTO categorias (nombre) VALUES
            ('Smartphones'), ('Notebooks'), ('Watches'), ('Tablets'), ('Games'),
            ('Accesories')
ON DUPLICATE KEY UPDATE nombre=nombre;

/*SELECT * FROM categorias;*/


/*Insertar Usuarios*/
INSERT INTO usuarios (nombre, apellido, nombre_usuario, correo, contrasenia, telefono, fecha_nacimiento)
VALUES 
('Federico', 'Ocaranza', 'fede9087', 'fede.ocaranza@misitioweb.com', 'gdgdhhsshuy3y', '+54 12345678', '2024-01-01'),
('Jhoan', 'Yanez', 'jhoanyanez', 'jhoan.yanez@misitioweb.com', 'Xgdyhhjaeu235', '+54 12345678', '2024-01-01'),
('Marcelo', 'Rodriguez', 'Marce1965', 'marcelo.rodriguez@misitioweb.com', 'Xgdyhhjaeu235', '+54 12345678', '2024-01-01'),
('Alejandro', 'Piris', 'AlePiris', 'alejandro.piris@misitioweb.com', 'Xgdyhhjaeu235', '+54 12345678', '2024-01-01'),
('Pablo', 'Masciangelo', 'PabloMasciangelo', 'pablo.masciangelo@misitioweb.com', 'Xgdyhhjaeu235', '+54 12345678', '2024-01-01'),
('Milagros', 'Martinez', 'MiliMartinez', 'milagros.martinez@misitioweb.com', 'Xgdyhhjaeu235', '+54 12345678', '2024-01-01');

/*SELECT * FROM usuarios;*/


/*Insertar Productos*/

INSERT INTO productos (nombre, descripcion, precio, cantidad, imagen)
VALUES
  ('Iphone 15 256GB', 'Producto Importado', 1000.00, 10, './img/product_1.png' ),
  ('Apple Watch', 'Producto Importado', 500.00, 15, './img/product_2.png'),
  ('DJI MiniPro 3', 'Producto Importado', 1200.50, 8, './img/product_3.png'),
  ('JBL Bluetooth', 'Producto Nacional', 119.99, 20, './img/product_4.png'),
  ('Play Station 5', 'Producto Importado', 999.99, 12, './img/product_5.png'),
  ('Macbook Pro', 'Producto Importado', 3500.50, 50, './img/product_6.png');

/*SELECT * FROM productos;*/

/*Insertar Productos por Categorias*/

INSERT INTO productos_categorias (id_producto, id_categoria)
VALUES 
(4, 5),
(5, 7),
(6, 9),
(7, 10),
(8, 9),
(9, 6),
(10, 5),
(11, 7),
(12, 9),
(13, 10),
(14, 9),
(15, 6);

/*SELECT * FROM productos_categorias;*/