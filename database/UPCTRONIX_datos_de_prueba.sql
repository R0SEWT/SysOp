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
	('Juan Pérez', 'juan.perez@gmail.com', 30, 1),
    ('María Rodríguez', 'maria.rodriguez@gmail.com', 25, 2),
    ('Carlos García', 'carlos.garcia@gmail.com', 45, 1),
    ('Ana Torres', 'ana.torres@gmail.com', 35, 2),
    ('Luis Martínez', 'luis.martinez@gmail.com', 50, 1),
    ('Sofía López', 'sofia.lopez@gmail.com', 28, 2),
    ('Pedro González', 'pedro.gonzalez@gmail.com', 32, 1),
    ('Laura Sánchez', 'laura.sanchez@gmail.com', 22, 2),
    ('Miguel Pérez', 'miguel.perez@gmail.com', 40, 1),
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
    ('Electrodomésticos', NULL);   
 
insert into CategoriaProducto(name, super_categoria)
values
    ('Cocina', 1),
    ('Hogar', 1),
    ('Electrodomésticos de Oficina', 1); 

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




