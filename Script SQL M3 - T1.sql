create database usuarios;
use usuarios;

select * from usuario;
truncate table usuario;
drop table usuario;


INSERT INTO Guarderias (id, nombre, direccion, telefono) VALUES
(1, 'Patitas Felices', 'Av. Siempre Viva 123', '555-1234'),
(2, 'Huellitas', 'Calle Luna 45', '555-5678'),
(3, 'Dog Paradise', 'Carrera 10 #5-33', '555-9101'),
(4, 'Mundo Canino', 'Calle Sol 89', '555-1213'),
(5, 'Amigos Peludos', 'Av. Central 22', '555-1415'),
(6, 'Cuatro Patas', 'Callejón Bonito 7', '555-1617'),
(7, 'Happy Paws', 'Cra 12 #45-78', '555-1819'),
(8, 'Puppy Love', 'Av. Jardín 99', '555-2021'),
(9, 'PerroLandia', 'Calle Brisa 77', '555-2223'),
(10, 'Guardería Canina VIP', 'Av. Elite 5', '555-2425');


INSERT INTO Cuidadores (id, nombre, telefono, id_guarderia) VALUES
(1, 'Carlos Pérez', '320-111-2233', 1),
(2, 'María López', '310-222-3344', 2),
(3, 'José Rodríguez', '315-333-4455', 3),
(4, 'Ana González', '312-444-5566', 4),
(5, 'Diego Martínez', '318-555-6677', 5),
(6, 'Laura Sánchez', '319-666-7788', 6),
(7, 'Ricardo Torres', '313-777-8899', 7),
(8, 'Elena Ramírez', '316-888-9900', 8),
(9, 'Javier Castillo', '317-999-0011', 9),
(10, 'Sofía Herrera', '321-000-1122', 10),
(11, 'Fernando Gómez', '322-123-4567', 1),
(12, 'Gabriela Muñoz', '323-234-5678', 2),
(13, 'Andrés Silva', '324-345-6789', 3),
(14, 'Patricia Vargas', '325-456-7890', 4),
(15, 'Martín Herrera', '326-567-8901', 1),
(16, 'Rosa Fernández', '327-678-9012', 2),
(17, 'Hugo Navarro', '328-789-0123', 3),
(18, 'Camila Ríos', '329-890-1234', 4),
(19, 'Daniel Ortega', '330-901-2345', 1),
(20, 'Natalia Paredes', '331-012-3456', 2);


INSERT INTO Perros (id, nombre, raza, edad, peso, id_guarderia, id_cuidador) VALUES
(1, 'Rufo', 'Labrador', 7, 22, 1, 1),
(2, 'Bingo', 'Pug', 2, 6, 2, 2),
(3, 'Lassie', 'Collie', 5, 27, 3, 3),
(4, 'Max', 'Pastor Alemán', 4, 30, 4, 4),
(5, 'Bella', 'Golden Retriver', 3, 25, 3, 5),
(6, 'Rocky', 'Bulldog', 6, 28, 2, 6),
(7, 'Toby', 'Dálmata', 2, 20, 4, 7),
(8, 'Maya', 'Beagle', 5, 18, 1, 8),
(9, 'Simba', 'Chihuahua', 3, 4, 4, 9),
(10, 'Bruno', 'San Bernardo', 6, 50, 1, 10),
(11, 'Luna', 'Husky Siberiano', 3, 21, 1, 11),
(12, 'Duke', 'Boxer', 5, 29, 2, 12),
(13, 'Nala', 'Cocker Spaniel', 4, 14, 3, 13),
(14, 'Zeus', 'Doberman', 6, 35, 4, 14),
(15, 'Tina', 'Shih Tzu', 2, 7, 1, 15),
(16, 'Rocky', 'Border Collie', 4, 19, 2, 16),
(17, 'Chico', 'Pinscher', 3, 5, 3, 17),
(18, 'Milo', 'Caniche', 5, 8, 4, 18),
(19, 'Coco', 'Bichón Frisé', 3, 6, 1, 19),
(20, 'Rex', 'Gran Danés', 7, 55, 2, 20),
(21, 'Mini', 'Yorkshire', 2, 2, 1, 5),
(22, 'Pipo', 'Chihuahua', 3, 1, 2, 6),
(23, 'Lily', 'Pomerania', 4, 2, 3, 7);

select * from guarderias;
select * from perros;
select * from cuidadores;
