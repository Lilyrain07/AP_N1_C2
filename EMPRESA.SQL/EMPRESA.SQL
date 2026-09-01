-- hola
/*
koni
shi
wa
*/

-- SIRVE PARA CREAR UNA clase
CREATE DATABASE empresa;

-- SELECCIONA ESTA clase DE AHORA EN ADELANTE
USE empresa;

-- SIRVE PARA ELIMINAR UNA clase
DROP DATABASE empresa;

-- para crear una tabla
CREATE TABLE t_personal
(id INT PRIMARY KEY,
nombre VARCHAR(100) NOT NULL, -- 
apellido VARCHAR(100) NOT NULL,
email VARCHAR(100)UNIQUE,
ciudad VARCHAR(100),
salario INT,
departamento VARCHAR(50),
fecharegistro DATE
);

-- not null : es obligatorio llenar con alguna informacion


-- otra tabla pero de productos y sus atributos
CREATE TABLE t_producto
(
id INT PRIMARY KEY,
nombre VARCHAR (255) NOT NULL,
precio DECIMAL (10,2) NOT NULL,
stock INT DEFAULT 0,
fechacreacion DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- datetime default current_timestamps : es para registrar con la hora que tiene el dispositivo

-- alter : es para modificar algo que ya existe

/* sirve para añadir una nueva columna
ALTER TABLE nombre_tabla
ADD nombre_tabla tipo_dato;
*/

/* modificar 
ALTER TABLE nombre_tabla
ALTER COLUMN nombre_tabla tipo_dato;
*/

/* eliminar 
ALTER TABLE nombre_tabla
Drop COLUMN nombre_tabla tipo_dato;
*/

--vamos a añadir algo a la tabla
ALTER TABLE t_personal
ADD telefono VARCHAR(20);

--a borrar aglo de la tabla DX
ALTER TABLE t_personal
DROP COLUMN fecharegistro;

/* con esto es eliminar la tabla JAAJAJ
DROP TABLE nombre_tabla;
*/
--  a eliminar 
DROP TABLE t_producto;

insert into nombre_tabla(columna1,columna2,columna3)
    values (valor1,valor2,valor3);
    -- se usa para agregar nuevos registros a una tabla


--para insertar varios datos:

insert into t_personal (id,nombre,apellido,salario,departamento)
    values(2,'maria', 'garcia', 650000,'marketing'),
          (3,'carlos','lopez',680000,'IT'),
          (4,'ana','martin',620000,'ventas');


--insertar sin especificacion de columnas

insert into t_personal
    values (5,'ana','santos','as@gmail.com','temuco',900000, 'gerencia', '2025-08-21');

    
insert into t_producto
    values (1,'cuaderno',4500,20,'2025-08-21'),
            (2,'lapiz',2800,35,'2024-09-11'),
            (9,'goma',1200,15,'2023-10-31');