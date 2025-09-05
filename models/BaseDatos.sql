-- Creación de la base de datos
CREATE DATABASE IF NOT EXISTS libreria;

-- Usar la base de datos
USE libreria;

-- Creación de tablas
-- Tabla Categoría
CREATE TABLE IF NOT EXISTS categoria(
    id INT AUTO_INCREMENT NOT NULL,
    nombre_categoria VARCHAR(100) NOT NULL,
    CONSTRAINT pk_categoria
    PRIMARY KEY (id)
);

-- Tabla Autor
CREATE TABLE IF NOT EXISTS autor (
    id INT AUTO_INCREMENT NOT NULL,
    nombre_autor VARCHAR(100) NOT NULL,
    CONSTRAINT pk_autor
    PRIMARY KEY (id)
);

-- Tabla Editorial
CREATE TABLE IF NOT EXISTS editorial(
    id INT AUTO_INCREMENT NOT NULL,
    nombre_editorial VARCHAR(100) NOT NULL,
    CONSTRAINT pk_editorial
    PRIMARY KEY(id)

);

-- Tabla libro
CREATE TABLE IF NOT EXISTS libro(
    id INT AUTO_INCREMENT NOT NULL,
    precio DOUBLE(13,2) NOT NULL,
    cantidad INT NOT NULL,
    nombre_libro VARCHAR(150) NOT NULL,
    id_autor INT NOT NULL,
    id_editorial INT NOT NULL,
    id_categoria INT NOT NULL,
    url_imagen VARCHAR(255) NOT NULL,
    activo BOOL NOT NULL,
    CONSTRAINT pk_libro PRIMARY KEY (id),
    CONSTRAINT FK_LIBRO_AUTOR FOREIGN KEY(id_autor) REFERENCES autor(id) ON DELETE CASCADE,
    CONSTRAINT fk_libro_editorial FOREIGN KEY (id_editorial) REFERENCES editorial(id) ON DELETE CASCADE,
    CONSTRAINT fk_libro_categoria FOREIGN KEY(id_categoria) REFERENCES categoria(id) ON DELETE CASCADE
);

-- Tabla Rol
CREATE TABLE IF NOT EXISTS ROL(
    ID INT AUTO_INCREMENT NOT NULL,
    NOMBRE_ROL VARCHAR(100) NOT NULL,
    ACTIVO BOOLEAN NOT NULL,
    CONSTRAINT PK_ROL PRIMARY KEY (ID)
);

-- Tabla Usuario
CREATE TABLE IF NOT EXISTS usuario(
    id INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(200) NOT NULL,
    apellidos VARCHAR(200) NOT NULL,
    correo_electronico VARCHAR(100) NOT NULL,
    contrasena VARCHAR(300) NOT NULL,
    id_rol INT NOT NULL,
    ACTIVO BOOLEAN,
    CONSTRAINT PK_USUARIO PRIMARY KEY (ID), 
    CONSTRAINT FK_USUARIO_ROL FOREIGN KEY (id_rol) REFERENCES ROL(ID) ON DELETE CASCADE
);

-- Tabla Carrito
CREATE TABLE IF NOT EXISTS CARRITO(
    ID INT AUTO_INCREMENT NOT NULL,
    ID_LIBRO INT NOT NULL,
    ID_USUARIO INT NOT NULL,
    MONTO DOUBLE(13,2) NOT NULL,
    CANTIDAD INT NOT NULL,
    FECHA DATETIME NOT NULL,
    CONSTRAINT PK_CARRITO PRIMARY KEY (ID),
    CONSTRAINT FK_CARRITO_USUARIO FOREIGN KEY (ID_USUARIO) REFERENCES USUARIO(ID) ON DELETE CASCADE,
    CONSTRAINT FK_CARRITO_LIBRO FOREIGN KEY (ID_LIBRO) REFERENCES LIBRO (ID) ON DELETE CASCADE
);

-- Inserción de datos
-- Tabla categoría
insert into libreria.categoria (nombre_categoria) values 
	('Novelas'),
	('Poesía'),
	('Economía'),
	('Nueva Era'),
	('Juvenil'),
	('Autoayuda'),
	('Ciencia Ficción'),
	('Filosofía'),
	('Psicología'),
	('Legal');

-- Tabla autores
INSERT INTO libreria.autor (nombre_autor) VALUES 
    ('Gabriel García Márquez'),
    ('Julio Cortázar'),
    ('JK Rowling'),
    ('George Orwell'),
    ('Victor Hugo'),
    ('Aristóteles'),
    ('Donald Trump'),
    ('Walter Riso'),
    ('Sigmund Freud'),
    ('Mario Benedetti');

-- Tabla editoriales
INSERT INTO libreria.editorial (nombre_editorial) VALUES
    ('Alfaguara'),
    ('Anagrama'),
    ('Alianza'),
    ('Norma'),
    ('Diana');

-- Tabla libros
INSERT INTO libreria.libro (precio, cantidad, nombre_libro, id_autor, id_editorial, id_categoria, url_imagen, activo) VALUES
    (5500, 10, 'Cien Años de Soledad',  1, 5, 1, 'img/imagen-1.jpg',1),
    (8000, 5, 'Rayuela', 2, 3, 1, 'img/imagen-2.jpg',1),
    (1000, 11, 'Harry Potter y la Piedra Filosofal', 3, 2, 1, 'img/imagen-3.jpg',1),
    (6000, 5, 'La Tregua', 10, 5, 1, 'img/imagen-4.jpg',1),
    (9000, 7, '1984', 4, 1, 1, 'img/imagen-5.jpg',1),
    (7500, 3, 'Introducción al Psicoanálisis', 9, 2, 9, 'img/imagen-6.jpg',1),
    (4500, 3, 'Los Miserables', 5, 1, 1, 'img/imagen-7.jpg',1),
    (6250, 8, 'Crónica de una Muerte anunciada', 1, 5, 1, 'img/imagen-8.jpg',1),
    (8000, 9, 'Amor en los Tiempos del Cólera', 1, 5, 1, 'img/imagen-9.jpg',1),
    (4568, 2, 'Ética a Nicomaco', 6, 2, 8, 'img/imagen-10.jpg',1);

INSERT INTO libreria.rol (nombre_rol, activo) VALUES
    ('Administrador', 1),
    ('Empleado', 1),
    ('Cliente', 1);
    
INSERT INTO usuario (nombre, apellidos, correo_electronico, contrasena, id_rol, ACTIVO) VALUES
    ('Carlos', 'Pérez', 'carlos.perez@example.com', SHA('contrasena123'), 1, TRUE),
    ('Ana', 'Gómez', 'ana.gomez@example.com', SHA('contrasena456'), 2, TRUE),
    ('Luis', 'Rodríguez', 'luis.rodriguez@example.com', SHA('contrasena789'), 3, TRUE);


-- Procedimientos almacenados
DROP PROCEDURE IF EXISTS sp_listar_categorias;

CREATE PROCEDURE libreria.sp_listar_categorias()
    SELECT id, nombre_categoria
    FROM categoria;

CREATE PROCEDURE libreria.sp_crear_categoria(p_nombre_categoria varchar(100))
    INSERT INTO categoria (nombre_categoria) VALUES (p_nombre_categoria);


DELIMITER //
CREATE PROCEDURE libreria.sp_eliminar_categoria(IN p_id INT)
BEGIN
    DELETE FROM categoria
    WHERE id = p_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE libreria.sp_actualizar_categoria(p_id int, p_categoria varchar(100))
BEGIN
    UPDATE categoria SET nombre_categoria = p_categoria
    WHERE id = p_id;
END //
DELIMITER ;

CREATE PROCEDURE libreria.sp_buscar_categoria(p_id int)
    SELECT id, nombre_categoria
    FROM categoria
    where id = p_id;


DELIMITER //
CREATE PROCEDURE libreria.sp_listar_autores()
BEGIN
    SELECT id, nombre_autor
    FROM autor;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE libreria.sp_crear_autor(p_nombre_autor varchar(100))
BEGIN
    INSERT INTO autor(nombre_autor) 
    VALUES(p_nombre_autor);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_actualizar_autor(p_id int, p_nombre_autor varchar(100))
BEGIN
    UPDATE autor SET nombre_autor = p_nombre_autor
    WHERE id = p_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE libreria.sp_buscar_autor(p_id int)
BEGIN
    SELECT id, nombre_autor
    FROM autor
    WHERE id = p_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_eliminar_autor (p_id int)
BEGIN
    DELETE FROM autor
    WHERE id = p_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE libreria.sp_listar_editoriales()
BEGIN
    SELECT id, nombre_editorial 
    FROM editorial;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE libreria.sp_crear_editorial(p_nombre_editorial VARCHAR(100))
BEGIN
    INSERT INTO editorial(nombre_editorial)
    VALUES(p_nombre_editorial);
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE libreria.sp_actualizar_editorial(p_id INT, p_nombre_editorial VARCHAR(100))
BEGIN
    UPDATE editorial 
    SET nombre_editorial = p_nombre_editorial
    WHERE id = p_id;
END //

DELIMITER ;

DELIMITER //
CREATE PROCEDURE libreria.sp_buscar_editorial(p_id int)
BEGIN
    SELECT id, nombre_editorial 
    FROM editorial
    where id = p_id;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE libreria.sp_eliminar_editorial(p_id INT)
BEGIN
    DELETE FROM editorial 
    WHERE id = p_id;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE sp_listar_libros()
BEGIN
    SELECT  L.id,
            precio,
            cantidad,
            nombre_libro,
            id_autor,
            id_editorial,
            id_categoria,
            url_imagen,
            a.nombre_autor,
            e.nombre_editorial,
            c.nombre_categoria,
            l.activo
    FROM    libro l
    INNER JOIN autor a
    ON      a.id = l.id_autor
    INNER JOIN categoria c
    ON      c.id = l.id_categoria
    INNER JOIN editorial e
    ON      e.id = l.id_editorial
    ORDER BY id;
            
    
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE libreria.sp_crear_libro(
    p_precio DOUBLE(13,2),
    p_cantidad INT,
    p_nombre_libro VARCHAR(150),
    p_id_autor INT,
    p_id_editorial INT,
    p_id_categoria INT,
    p_url_imagen VARCHAR(255)
)
BEGIN
    INSERT INTO libro
    (
        precio,
        cantidad,
        nombre_libro,
        id_autor,
        id_editorial,
        id_categoria,
        url_imagen,
        activo
    ) 

    VALUES (
        p_precio,
        p_cantidad,
        p_nombre_libro,
        p_id_autor,
        p_id_editorial,
        p_id_categoria,
        p_url_imagen,
        1
    );

END //

DELIMITER ;

DELIMITER //
CREATE PROCEDURE libreria.sp_actualizar_libro(
    p_id INT,
    p_precio DOUBLE(13,2),
    p_cantidad INT,
    p_nombre_libro VARCHAR(150),
    p_id_autor INT,
    p_id_editorial INT,
    p_id_categoria INT,
    p_url_imagen VARCHAR(255)
)
BEGIN
    UPDATE  libro SET
        precio = p_precio,
        cantidad = p_cantidad,
        nombre_libro = p_nombre_libro,
        id_autor = p_id_autor,
        id_editorial = p_id_editorial,
        id_categoria = p_id_categoria,
        url_imagen = p_url_imagen
    WHERE
        id = p_id;

END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE sp_buscar_libro(p_id int)
BEGIN
    SELECT  L.id,
            precio,
            cantidad,
            nombre_libro,
            id_autor,
            id_editorial,
            id_categoria,
            url_imagen,
            a.nombre_autor,
            e.nombre_editorial,
            c.nombre_categoria
    FROM    libro l
    INNER JOIN autor a
    ON      a.id = l.id_autor
    INNER JOIN categoria c
    ON      c.id = l.id_categoria
    INNER JOIN editorial e
    ON      e.id = l.id_editorial
    WHERE l.id = p_id;
            
    
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_eliminar_libro (p_id int)
BEGIN
	DECLARE P_ACTIVO BOOL;
    SELECT ACTIVO INTO P_ACTIVO
    FROM LIBRO
    WHERE ID = P_ID;
    
    IF P_ACTIVO = 1 THEN 
		UPDATE LIBRO SET ACTIVO = 0
        WHERE ID = P_ID;
    ELSE 
		UPDATE LIBRO SET ACTIVO =1
        WHERE ID = P_ID;
	END IF;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE libreria.sp_listar_roles()
BEGIN
    SELECT id, nombre_rol, activo
    FROM rol;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE libreria.sp_crear_rol(p_nombre_rol varchar(100))
BEGIN
    INSERT INTO rol(nombre_rol) 
    VALUES(p_nombre_rol);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_actualizar_rol(p_id int, p_nombre_rol varchar(100))
BEGIN
    UPDATE rol SET nombre_rol = p_nombre_rol
    WHERE id = p_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE libreria.sp_buscar_rol(p_id int)
BEGIN
    SELECT id, nombre_rol, activo
    FROM rol
    WHERE id = p_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_eliminar_rol (p_id int)
BEGIN
	DECLARE P_ACTIVO BOOL;
    SELECT ACTIVO INTO P_ACTIVO
    FROM ROL
    WHERE ID = P_ID;
    
    IF P_ACTIVO = 1 THEN 
		UPDATE ROL SET ACTIVO = 0
        WHERE ID = P_ID;
    ELSE 
		UPDATE ROL SET ACTIVO =1
        WHERE ID = P_ID;
	END IF;
END//
DELIMITER ;


-- Trigger
DELIMITER //

CREATE TRIGGER tgr_actualizar_usuarios
AFTER UPDATE ON ROL
FOR EACH ROW
BEGIN
    -- Verificamos si el campo 'activo' ha cambiado
    IF OLD.activo != NEW.activo THEN
        -- Actualizamos el campo 'activo' de todos los usuarios con el rol modificado
        UPDATE USUARIO
        SET activo = NEW.activo
        WHERE id_rol = NEW.id;
    END IF;
END //

DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_crear_usuario(
    P_NOMBRE VARCHAR(200),
    P_APELLIDOS VARCHAR(200),
    P_CORREO_ELECTRONICO VARCHAR(100),
    P_CONTRASENA VARCHAR(300),
    P_ID_ROL INT
)
BEGIN
    DECLARE P_ACTIVO BOOL ;
    SET P_ACTIVO = 1;

    INSERT INTO USUARIO  (
        NOMBRE,
        APELLIDOS,
        CORREO_ELECTRONICO,
        CONTRASENA,
        ID_ROL,
        ACTIVO
    ) VALUES (
        P_NOMBRE,
        P_APELLIDOS,
        P_CORREO_ELECTRONICO,
        SHA(P_CONTRASENA),
        P_ID_ROL,
        P_ACTIVO
    );
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_listar_usuarios()
BEGIN
    SELECT u.id, nombre,  apellidos,correo_electronico, nombre_rol,id_rol, U.activo 
    FROM usuario u
    INNER JOIN rol r
    ON u.id_rol = r.id
    ORDER BY id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_buscar_usuario(p_id INT)
BEGIN
    SELECT u.id, nombre, apellidos,correo_electronico, nombre_rol,id_rol, U.activo 
    FROM usuario u
    INNER JOIN rol r
    ON u.id_rol = r.id
    WHERE U.id = p_id
    ORDER BY U.id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_actualizar_usuario(
    P_ID INT,
    P_NOMBRE VARCHAR(200),
    P_APELLIDOS VARCHAR(200),
    P_CORREO_ELECTRONICO VARCHAR(100),
    P_ID_ROL INT
)
BEGIN
    UPDATE usuario 
    SET NOMBRE = P_NOMBRE,
        APELLIDOS = P_APELLIDOS,
        CORREO_ELECTRONICO = P_CORREO_ELECTRONICO,
        P_ID_ROL = ID_ROL
    WHERE ID = P_ID;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_eliminar_usuario (p_id int)
BEGIN
	DECLARE P_ACTIVO BOOL;
    SELECT ACTIVO INTO P_ACTIVO
    FROM USUARIO
    WHERE ID = P_ID;
    
    IF P_ACTIVO = 1 THEN 
		UPDATE USUARIO SET ACTIVO = 0
        WHERE ID = P_ID;
    ELSE 
		UPDATE USUARIO SET ACTIVO =1
        WHERE ID = P_ID;
	END IF;
END//
DELIMITER ;


DELIMITER //
CREATE PROCEDURE sp_registro_usuario(
    P_NOMBRE VARCHAR(200),
    P_APELLIDOS VARCHAR(200),
    P_CORREO_ELECTRONICO VARCHAR(100),
    P_CONTRASENA VARCHAR(300)
)
BEGIN
    DECLARE P_ACTIVO BOOL ;
    DECLARE P_ID_ROL INT;
    SET P_ACTIVO = 1;
    SET P_ID_ROL = 3;

    INSERT INTO USUARIO  (
        NOMBRE,
        APELLIDOS,
        CORREO_ELECTRONICO,
        CONTRASENA,
        ID_ROL,
        ACTIVO
    ) VALUES (
        P_NOMBRE,
        P_APELLIDOS,
        P_CORREO_ELECTRONICO,
        SHA(P_CONTRASENA),
        P_ID_ROL,
        P_ACTIVO
    );
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE libreria.sp_login(p_correo_electronico VARCHAR(100),
                          p_contrasena VARCHAR(300)
                         )
BEGIN
    SELECT u.id, u.nombre, u.apellidos, u.correo_electronico, u.id_rol, r.nombre_rol
    FROM usuario u
    INNER JOIN rol r 
    ON u.id_rol = r.id
    WHERE correo_electronico = p_correo_electronico 
    AND contrasena = SHA(p_contrasena) 
    AND u.activo = 1;
END //
DELIMITER //