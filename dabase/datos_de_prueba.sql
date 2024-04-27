use UPCTRONIX
-------------- Facturacion-----
insert into Sexo(sexo)
values
	('femenino'),
	('masculino');

insert into TipoFactura(tipo)
values
('factura'),
('boleta');

insert into Cliente(full_name, email, edad, sexo_id)
values 
	('Juan Perez', 'juan.perez@gmail.com', 30, 1),
    ('María Rodríguez', 'maria.rodriguez@gmail.com', 25, 2),
    ('Carlos García', 'carlos.garcia@gmail.com', 45, 1),
    ('Ana Torres', 'ana.torres@gmail.com', 35, 2),
    ('Luis Martínez', 'luis.martinez@gmail.com', 50, 1),
    ('Sofia Lopez', 'sofia.lopez@gmail.com', 28, 2),
    ('Pedro Gonzalez', 'pedro.gonzalez@gmail.com', 32, 1),
    ('Laura Sanchez', 'laura.sanchez@gmail.com', 22, 2),
    ('Miguel Perez', 'miguel.perez@gmail.com', 40, 1),
    ('Carmen Martínez', 'carmen.martinez@gmail.com', 38, 2);

select * from Sexo

insert into Facturacion(tipo_factura, ruc_dni, email)
values
	(1, '1234567890123', 'sofia.lopez@gmail.com'),
    (2, '75392012', 'juan.perez@gmail.com'),
    (1, '3456789012345', NULL),
    (1, '4567890123456', 'pedro.gonzales@gmail.com'),
    (2, '75322122', NULL),
	(1, '8901234567890', 'maria.rodriguez@gmail.com'),
    (2, '90123456', 'carlos.martinez@gmail.com'),
    (1, '2345678901234', 'ana.sanchez@gmail.com'),
    (2, '34567890', 'luis.garcia@gmail.com'),
    (1, '4567890123456', 'carmen.perez@gmail.com');

insert into Venta(client_id, datos_facturacion)
values 
    (1, 100),
    (2, 101),
    (3, 102),
    (4, 103),
    (5, 104),
    (6, 105),
    (7, 106),
    (8, 107),
    (9, 108),
    (10, 109);
----------------------Inventario-------------------

alter table CategoriaProducto
alter column super_categoria int NULL;

insert into CategoriaProducto(name, super_categoria)
values
    ('Electrodomesticos', NULL);   
 
insert into CategoriaProducto(name, super_categoria)
values
    ('Cocina', 1),
    ('Hogar', 1),
    ('Electrodomesticos de Oficina', 1); 

insert into CategoriaProducto(name, super_categoria)
values
    ('Refrigeradores', 2),
    ('Estufas', 2),
    ('Microondas', 2),
    ('Lavadoras', 3),
    ('Secadoras', 3),
    ('Televisores', 4);
 ; 
 select * from CategoriaProducto

insert into Producto(categoria_id, stock, sku, name, precio, descripcion, img)
values
	(5, 100, 'SKU001', 'Refrigerador Modelo A', 1500.00, 'Refrigerador de 200 litros', NULL),
    (6, 50, 'SKU002', 'Estufa Electrónica', 300.00, 'Estufa de 4 quemadores', NULL),
    (7, 200, 'SKU003', 'Microondas 600W', 250.00, 'Microondas con temporizador', NULL),
    (4, 150, 'SKU004', 'Lavadora 7kg', 1200.00, 'Lavadora de 7 kg con 12 ciclos', NULL),
    (5, 100, 'SKU005', 'Secadora 5kg', 800.00, 'Secadora de 5 kg con 8 ciclos', NULL),
    (6, 50, 'SKU006', 'Televisor LED 42"', 1000.00, 'Televisor LED de 42 pulgadas', NULL),
    (5, 150, 'SKU007', 'Refrigerador Modelo B', 1800.00, 'Refrigerador de 300 litros', NULL),
    (6, 200, 'SKU008', 'Estufa a Gas', 400.00, 'Estufa a gas de 3 quemadores', NULL),
    (4, 250, 'SKU009', 'Lavadora 8kg', 1400.00, 'Lavadora de 8 kg con 14 ciclos', NULL),
    (5, 150, 'SKU010', 'Secadora 6kg', 900.00, 'Secadora de 6 kg con 9 ciclos', NULL);

insert into ProductosVendidos(venta_id, producto_id, precio_u, cantidad)
values
    (101, 1, 1500.00, 1),
    (101, 2, 300.00, 2),
    (102, 3, 250.00, 1),
    (102, 4, 1200.00, 1),
    (103, 5, 800.00, 1),
    (104, 6, 1000.00, 3),
    (104, 7, 1800.00, 1),
    (104, 8, 400.00, 1),
    (105, 9, 1400.00, 1),
    (106, 10, 900.00, 1);