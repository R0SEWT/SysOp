create database UPCTRONIX;
use UPCTRONIX;

-------------------------------------------DATABASE CREATION------------------------------
-----------FACTURACION---------------
create table TipoFactura(
	id int primary key identity(1,1),
	tipo varchar(255) not null
);

create table Facturacion(
	id int primary key identity(100,1),
	tipo_factura int not null,
	ruc_dni varchar(63) not null,
	email varchar(255) null,
	constraint fk_Factura_Facturacion foreign key (tipo_factura) references TipoFactura(id)
);

create table Venta(
	id int primary key identity(100,1),
	client_id int not null,
	datos_facturacion int not null,
	constraint fk_facturacion_venta foreign key (datos_facturacion) references Facturacion(id)
);

create table Sexo(
	id int primary key identity(1,1),
	sexo varchar(63) not null
);

create table Cliente(
	id int primary key identity(1000,1),
	full_name varchar(255)not null,
	email varchar(255)not null,
	edad int not null,
	sexo_id int not null
	constraint fk_sexo_cliente foreign key (sexo_id) references Sexo(id)
);

-----------INVENTARIO------------

create table CategoriaProducto(
	id int primary key identity(1,1),
	name varchar(255) not null,
	super_categoria int null,
	constraint fk_recursed_super_category foreign key (super_categoria) references CategoriaProducto(id)
);

create table Producto(
	id int primary key identity(1,1),
	categoria_id int not null,
	stock int not null,
	sku varchar(31) not null,
	name varchar(255) not null,
	precio decimal(12,2) not null,
	descripcion varchar(2047) not null,
	img image,
	constraint fk_categoria_producto foreign key (categoria_id) references CategoriaProducto(id)
);

create table ProductosVendidos(
	id int primary key identity(1,1),
	venta_id int,
	producto_id int,
	precio_u decimal(12,2),
	cantidad int,
	constraint fk_venta_productosVendidos foreign key (venta_id) references Venta(id),
	constraint fk_producto_productosVendidos foreign key (producto_id) references Producto(id)
);