CREATE TABLE empresa (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    ruc VARCHAR(11) NOT NULL,
    razon_social VARCHAR(255) NOT NULL,
    direccion VARCHAR(255)
);

INSERT INTO empresa(ruc,razon_social,direccion)
VALUES
('20124561789', 'AndES S.A.', 'Av. Larco 123, Lima'),
('20451234567', 'ServiSur E.I.R.L.', 'Jr. Mollendo 456, Arequipa'),
('20567845145', 'TECNITEC SAC', 'Calle Arequipa 789, Cusco'),
('20214587845', 'REPISUR S.A.C.', 'Av. Balta 321, Moquegua'),
('20457878751', 'Consultoria Gonzales SRL', 'Av. Rosales 124, Puno');

SELECT * FROM empresa;