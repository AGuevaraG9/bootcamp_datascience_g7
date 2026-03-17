use db_matriculas;
-- SENTENCIAS DML
-- CRUD
-- C - INSERT
-- R - SELECT
-- U - UPDATE
-- D - DELETE

-- INSERT
insert into alumno(nro_documento,nombre) values('100','cesar');

INSERT INTO alumno(nro_documento,nombre,nota)
VALUES
('200','ana',15),
('300','luis',20),
('400','jose',11),
('500','raul',10),
('600','carmen',13),
('700','jorge',16),
('800','daniel',20),
('900','luisa',17),
('1000','pedro',5);

-- SELECT READ O LEER DATOS
SELECT * FROM alumno;
SELECT nombre, nota FROM alumno;
-- select con where

SELECT nombre, nota FROM alumno WHERE nota > 10;
SELECT nombre, nota FROM alumno WHERE nombre LIKE '%L%';

-- ACTUALIZAR Y ELIMINAR DATOS
UPDATE alumno SET email = 'codigo@gmail.com';
-- ACTUALIZAR CON CONDICIONAL WHERE
UPDATE alumno SET email = 'cesar@gmail.com' WHERE id = 1;
-- ACTUALIZAR CON FUNCIONES
UPDATE alumno SET email = CONCAT(nombre,'@gmail.com') WHERE id != 1;

-- ELIMINAR ALUMNO
DELETE from alumno where id = 10;