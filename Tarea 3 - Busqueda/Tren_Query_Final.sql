-- Tablas para Estructura de Datos y Algoritmos 2020
-- Creación de Tablas
create table lineas_tren(
lineas_id int not null primary key identity(1,1),
lineas_nombre varchar(255) not null,
lineas_lineasId int not null,
lineas_lineasEstacion int not null
)
-- Fin Creación de Tablas
--Ingreso de datos
-- Linea 1
insert into lineas_tren values ('Mirador',1,1)
insert into lineas_tren values ('Huentitlán',1,2)
insert into lineas_tren values ('Zoológico',1,3)
insert into lineas_tren values ('Independencia Norte',1,4)
insert into lineas_tren values ('San Patricio',1,5)
insert into lineas_tren values ('Igualdad',1,6)
insert into lineas_tren values ('Monumental',1,7)
insert into lineas_tren values ('Monte Olivette',1,8)
insert into lineas_tren values ('Circunvalación 2',1,9)
insert into lineas_tren values ('Facultad de Medicina',1,10)
insert into lineas_tren values ('Juan Álvarez',1,11)
insert into lineas_tren values ('Alameda',1,12)
insert into lineas_tren values ('San Juan de Dios',1,13)
insert into lineas_tren values ('Bicentenario',1,14)
insert into lineas_tren values ('La Paz',1,15)
insert into lineas_tren values ('Niños Héroes',1,16)
insert into lineas_tren values ('Agua Azul',1,17)
insert into lineas_tren values ('Ciprés',1,18)
insert into lineas_tren values ('Héroe de Nacozari',1,19)
insert into lineas_tren values ('Lázaro Cárdenas',1,20)
insert into lineas_tren values ('El Dean',1,21)
insert into lineas_tren values ('Zona Industrial',1,22)
insert into lineas_tren values ('López de Legazpi',1,23)
insert into lineas_tren values ('Clemente Orozco',1,24)
insert into lineas_tren values ('Artes Plásticas',1,25)
insert into lineas_tren values ('Escultura',1,26)
insert into lineas_tren values ('Fray Angélico',1,27)

--Linea 2
insert into lineas_tren values ('Central Sur',2,1)
insert into lineas_tren values ('Concentro',2,2)
insert into lineas_tren values ('Jardines de la Paz',2,3)
insert into lineas_tren values ('Panamericana',2,4)
insert into lineas_tren values ('Juan Palomar',2,5)
insert into lineas_tren values ('Seminario',2,6)
insert into lineas_tren values ('Cámara de Comercio',2,7)
insert into lineas_tren values ('Minerva',2,8)
insert into lineas_tren values ('Centro Magno',2,9)
insert into lineas_tren values ('Américas',2,10)
insert into lineas_tren values ('Chapultepec',2,11)
insert into lineas_tren values ('Paraninfo',2,12)
insert into lineas_tren values ('Plaza Universidad',2,13)
insert into lineas_tren values ('San Juan de Dios',2,14)
insert into lineas_tren values ('Belisario Domínguez',2,15)
insert into lineas_tren values ('Oblatos 2',2,16)
insert into lineas_tren values ('Cristobal de Oñate',2,17)
insert into lineas_tren values ('San Andrés',2,18)
insert into lineas_tren values ('San Jacinto',2,19)
insert into lineas_tren values ('La Aurora',2,20)
insert into lineas_tren values ('Tetlán',2,21)

--Linea 3
insert into lineas_tren values ('Periférico Norte',3,1)
insert into lineas_tren values ('Demartológico',3,2)
insert into lineas_tren values ('División de Norte',3,3)
insert into lineas_tren values ('Ávila Camacho',3,4)
insert into lineas_tren values ('Mezquitán',3,5)
insert into lineas_tren values ('Refugio',3,6)
insert into lineas_tren values ('Juárez',3,7)
insert into lineas_tren values ('Mexicaltzingo',3,8)
insert into lineas_tren values ('Washington',3,9)
insert into lineas_tren values ('Santa Filomena',3,10)
insert into lineas_tren values ('Unidad Deportiva',3,11)
insert into lineas_tren values ('Urdaneta',3,12)
insert into lineas_tren values ('18 de Marzo',3,13)
insert into lineas_tren values ('Isla Raza',3,14)
insert into lineas_tren values ('Patria Sur',3,15)
insert into lineas_tren values ('España',3,16)
insert into lineas_tren values ('Tesoro',3,17)
insert into lineas_tren values ('Periférico Sur',3,18)

--Linea 4
insert into lineas_tren values ('Basílica',4,1)
insert into lineas_tren values ('Sanatorio',4,2)
insert into lineas_tren values ('Colegio Victoria',4,3)
insert into lineas_tren values ('Country Club',4,4)
insert into lineas_tren values ('Colón',4,5)
insert into lineas_tren values ('Lienzo Charro',4,6)
insert into lineas_tren values ('Mezquitán',4,7)
insert into lineas_tren values ('Panteón de Belén',4,8)
insert into lineas_tren values ('Procuraduria',4,9)
insert into lineas_tren values ('Facultad de Medicina',4,10)
insert into lineas_tren values ('Obrero',4,11)
insert into lineas_tren values ('Talpita',4,12)
insert into lineas_tren values ('El Jaraz',4,13)
insert into lineas_tren values ('Plutarco Elías Calles',4,14)
insert into lineas_tren values ('Haciendas',4,15)
insert into lineas_tren values ('Oblatos 1',4,16)
insert into lineas_tren values ('Bethel',4,17)

--Linea 5
insert into lineas_tren values ('San Isidro',5,1)
insert into lineas_tren values ('CUCEA',5,2)
insert into lineas_tren values ('Parque Zapopan',5,3)
insert into lineas_tren values ('Zoquipan',5,4)
insert into lineas_tren values ('Plaza Patria',5,5)
insert into lineas_tren values ('Colomos',5,6)
insert into lineas_tren values ('Plaza Pabellón',5,7)
insert into lineas_tren values ('San Javier',5,8)
insert into lineas_tren values ('3 de Marzo',5,9)
insert into lineas_tren values ('Jardines Universidad',5,10)
insert into lineas_tren values ('Ferrocarril',5,11)
insert into lineas_tren values ('Seminario',5,12)
insert into lineas_tren values ('La Gran Plaza',5,13)
insert into lineas_tren values ('San Ignacio',5,14)
insert into lineas_tren values ('Estampida',5,15)
insert into lineas_tren values ('Chapalita',5,16)
insert into lineas_tren values ('Abastos',5,17)
insert into lineas_tren values ('Mandarina',5,18)
insert into lineas_tren values ('Ruiseñor',5,19)
insert into lineas_tren values ('Unidad Deportiva',5,20)
insert into lineas_tren values ('Plaza las Torres',5,21)
insert into lineas_tren values ('Cristo Rey',5,22)
insert into lineas_tren values ('El Dean',5,23)
insert into lineas_tren values ('Nogalera',5,24)
insert into lineas_tren values ('Álamo',5,25)
insert into lineas_tren values ('Textiles',5,26)

--Linea 6
insert into lineas_tren values ('Tabachines',6,1)
insert into lineas_tren values ('Centro Cultural Tabachines',6,2)
insert into lineas_tren values ('Zoquipan',6,3)
insert into lineas_tren values ('Patria',6,4)
insert into lineas_tren values ('División del Norte',6,5)
insert into lineas_tren values ('Lomas',6,6)
insert into lineas_tren values ('Plan de San Luis',6,7)
insert into lineas_tren values ('Colón',6,8)
insert into lineas_tren values ('José María Vigil',6,9)
insert into lineas_tren values ('Zarco',6,10)
insert into lineas_tren values ('Avenida México',6,11)
insert into lineas_tren values ('Ladrón de Guevara',6,12)
insert into lineas_tren values ('Américas',6,13)
insert into lineas_tren values ('Lafayette',6,14)
insert into lineas_tren values ('Monumento a los Niños Héroes',6,15)
insert into lineas_tren values ('Santa Eduwiges',6,16)
insert into lineas_tren values ('Día',6,17)
insert into lineas_tren values ('Abastos',6,18)
insert into lineas_tren values ('Parque de las Estrellas',6,19)
insert into lineas_tren values ('Expo',6,20)
insert into lineas_tren values ('Plaza del Sol',6,21)

--Linea 7
insert into lineas_tren values ('Arco del Triunfo',7,1)
insert into lineas_tren values ('Belenes',7,2)
insert into lineas_tren values ('Mercado del Mar',7,3)
insert into lineas_tren values ('Zapopan Centro',7,4)
insert into lineas_tren values ('Plaza Patria',7,5)
insert into lineas_tren values ('Circunvalación',7,6)
insert into lineas_tren values ('División del Norte',7,7)
insert into lineas_tren values ('Normal',7,8)
insert into lineas_tren values ('Santuario',7,9)
insert into lineas_tren values ('San Juan de Dios',7,10)
insert into lineas_tren values ('Independencia Sur',7,11)
insert into lineas_tren values ('Plaza de la Bandera',7,12)
insert into lineas_tren values ('CUCEI',7,13)
insert into lineas_tren values ('Plaza Revolución',7,14)
insert into lineas_tren values ('Río Nilo',7,15)
insert into lineas_tren values ('Tlaquepaque Centro',7,16)
insert into lineas_tren values ('Nodo Revolución',7,17)
insert into lineas_tren values ('Central Camionera',7,18)

--Linea 8
insert into lineas_tren values ('Metropolitano',8,1)
insert into lineas_tren values ('La Estancia',8,2)
insert into lineas_tren values ('Guadalupe',8,3)
insert into lineas_tren values ('UNIVA',8,4)
insert into lineas_tren values ('Juan Diego',8,5)
insert into lineas_tren values ('Estampida',8,6)
insert into lineas_tren values ('Inglaterra',8,7)
insert into lineas_tren values ('Embajada',8,8)
insert into lineas_tren values ('Monumento',8,9)
insert into lineas_tren values ('Argentina',8,10)
insert into lineas_tren values ('Washington',8,11)
insert into lineas_tren values ('Agua Azul',8,12)
insert into lineas_tren values ('González Gallo',8,13)
insert into lineas_tren values ('CUCEI',8,14)
insert into lineas_tren values ('Medrano',8,15)
insert into lineas_tren values ('San Rafael',8,16)
insert into lineas_tren values ('Poetas',8,17)

-- Fin Ingresado de Datos