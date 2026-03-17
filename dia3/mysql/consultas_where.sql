-- CONSULTAS SELECT
SELECT * FROM empleado;
SELECT nombre, pais FROM empleado;
SELECT * FROM empleado ORDER BY salario DESC;

-- FILTROS
SELECT * FROM empleado WHERE pais = 'Peru';
SELECT * FROM empleado WHERE salario > 5000;
SELECT * FROM empleado WHERE salario BETWEEN 1000 AND 3000;
SELECT * FROM empleado WHERE pais = 'Peru' OR pais = 'Chile' and salario > 5000;
SELECT * FROM empleado WHERE pais IN ('Peru','Colombia','Chile');