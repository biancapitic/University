go
use MountainTrails
go
/*Regions*/
INSERT INTO Region (name) VALUES ('Transilvania')
INSERT INTO Region (name) VALUES ('Maramures')
INSERT INTO Region (name) VALUES ('Bucovina')
INSERT INTO Region (name) VALUES ('Crisana')
INSERT INTO Region (name) VALUES ('Moldova')
INSERT INTO Region (name) VALUES ('Banat')
INSERT INTO Region (name) VALUES ('Oltenia')
INSERT INTO Region (name) VALUES ('Muntenia')
INSERT INTO Region (name) VALUES ('Dobrogea')

/*Counties*/
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Salaj', 0, 1)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Bistrita-Nasaud', 0, 1)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Cluj', 0, 1)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Mures', 0, 1)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Harghita', 0, 1)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Hunedoara', 0, 1)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Alba', 0, 1)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Sibiu', 0, 1)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Brasov', 0, 1)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Covasna', 0, 1)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Satu-Mare', 0, 3)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Maramures', 0, 3)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Suceava', 0, 4)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Botosani', 0, 4)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Bihor', 0, 5)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Arad', 0, 5)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Neamt', 0, 6)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Iasi', 0, 6)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Bacau', 0, 6)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Vaslui', 0, 6)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Vrancea', 0, 6)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Galati', 0, 6)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Timis', 0, 7)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Caras-Severin', 0, 7)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Gorj', 0, 8)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Mehedinti', 0, 8)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Valcea', 0, 8)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Dolj', 0, 8)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Olt', 0, 8)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Arges', 0, 9)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Dambovita', 0, 9)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Prahova', 0, 9)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Buzau', 0, 9)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Braila', 0, 9)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Ilfov', 0, 9)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Ialomita', 0, 9)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Giurgiu', 0, 9)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Calarasi', 0, 9)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Tulcea', 0, 9)
INSERT INTO County (name, nrOfTrailes, regionId) VALUES ('Constanta', 0, 9)

INSERT INTO MountainRange (name, highest_altitude) VALUES ('Bihor-Padis', 1849), ('Bucegi-Leaota', 2505), ('Calimani', 2100), ('Ceahlau', 1907), ('Cernei-Mehedinti', 1928), 
										('Cindrel', 2245),('Ciucas', 1954), ('Cozia', 1668), ('Fagaras', 2544), ('Giumalau-Rarau',1858), ('Gutai', 1443), 
										('Harghitei', 1800), ('Macin', 467), ('Maramuresului', 2061),('Parang', 2519), ('Piatra Craiului', 2238), 
										('Retezat',2509), ('Rodnei', 2303), ('Trascau', 1369), ('Vladeasa', 1836) 

INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (15,1) --Bihor-Padis
INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (15,1) -- Violation!!

INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (31,18)
INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (32,20)
INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (9,20)
INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (4,3)      
INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (13,3)
INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (5,3)
INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (2,3)				
INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (17, 4) 
INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (25,5) 
INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (24,5)
INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (26,5)
INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (8,6)
INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (9,7)
INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (27,8)
INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (8,9) 
INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (9,9)
INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (27,9)
INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (30,9)
INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (14,11)
INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (5,12)
INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (12,14)
INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (25,15)
INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (27,15)
INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (8,15)
INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (7,15)
INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (9,16)
INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (30,16)
INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (6,17)
INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (12,19)
INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (2,19)
INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (3,20)
INSERT INTO MountainRange_County(countyId, mountainsId) VALUES (7,20)


INSERT INTO Cottage(name, accomodationNumber, raiting) VALUES ('Cabana Trei Brazi', 50, 8)
INSERT INTO Cottage(name, accomodationNumber, raiting) VALUES ('Cabana Apuseni', 60, 9)
INSERT INTO Cottage(name, accomodationNumber, raiting) VALUES ('Cabana Ursului', 30, 10)
INSERT INTO Cottage(name, accomodationNumber, raiting) VALUES ('Cabana Cetatile Ponorului', 35, 9)
INSERT INTO Cottage(name, accomodationNumber, raiting) VALUES ('Cabana Verde', 6, 8)
INSERT INTO Cottage(name, accomodationNumber, raiting) VALUES ('Cabana Cerbilor', 2, 7)
INSERT INTO Cottage(name) VALUES ('Cabana Fagaras')
INSERT INTO Cottage(name, accomodationNumber, raiting) VALUES ('Cabana Sambetei', 30, 9)
INSERT INTO Cottage(name, accomodationNumber, raiting) VALUES ('Cabana de Sus', 10, 8)
INSERT INTO Cottage(name, accomodationNumber, raiting) VALUES ('Cabana Aplin', 20, 10)
INSERT INTO Cottage(name, accomodationNumber, raiting) VALUES ('Cabana din munte', 15, 10)
INSERT INTO Cottage(name, accomodationNumber, raiting) VALUES ('Cabana Diham', 20, 9.5)
INSERT INTO Cottage(name, accomodationNumber, raiting) VALUES ('Cabana Izvoarele', 25, 9), ('Cabana Paraul Rece', 15, 8), ('Cabana Omu', 20, 7), 
															  ('Cabana Pietrele Arse', 30, 8), ('Cabana Caraiman', 22, 10)
INSERT INTO Cottage(name, accomodationNumber, raiting) VALUES ('Podragu', 10, 6), ('Malaiesti', 15, 8)
INSERT INTO Cottage(name, accomodationNumber, raiting) VALUES ('Crailor', 5, 4)



INSERT INTO Trail(name, time, difficulty, mark, mountain_range) VALUES ('Cetatile Ponorului - Balcoane', 2.0, 'medium', 'red cross', 1);
INSERT INTO Trail(name, time, difficulty, mark, mountain_range) VALUES ('Cetatile Ponorului', 5.0, 'hard', 'blue cross', 1);
INSERT INTO Trail(name, time, difficulty, mark, mountain_range) VALUES ('Cheile Galbene', 2.5, 'medium', 'yellow dot', 1);
INSERT INTO Trail(name, time, difficulty, mark, mountain_range) VALUES ('Poiana Ponorului', 1.0, 'easy', 'red dot', 1);
INSERT INTO Trail(name, time, difficulty, mark, mountain_range) VALUES ('Pestera Ghetarul Focul Viu', 2.0, 'easy', 'blue dot', 1)
INSERT INTO Trail(name, time, difficulty, mark, mountain_range) VALUES ('Lumea pierduta', 1.0, 'hard', 'orange dot', 1)
INSERT INTO Trail(name, time, difficulty, mark, mountain_range) VALUES ('Saua Capra-Fereastra Mare a Sambetei', 11.0, 'hard', 'red line', 9)
INSERT INTO Trail(name, time, difficulty, mark, mountain_range) VALUES ('Curmătura de Vest a Gârbovei - Vf. Ciortea Est', 1.5, 'medium', 'red cross', 9)
INSERT INTO Trail(name, time, difficulty, mark, mountain_range) VALUES ('Complexul Turistic Piscul Negru - Stâna Lespezi - Şaua Podeanu', 2.5, 'easy', 'red cross', 9)
INSERT INTO Trail(name, time, difficulty, mark, mountain_range) VALUES ('Focul Viu-Cheile Galbene', 7, 'hard', '',1)
INSERT INTO Trail(name, time, difficulty, mark, mountain_range) VALUES ('Valea Avrigului-Lacul Avrig', 3, 'medium', '',9)
INSERT INTO Trail(name, time, difficulty, mark, mountain_range) VALUES ('Lacul Capra - Refugiul Bâlea - Refugiul Călţun', 4, 'medium', 'blue cross',9)
INSERT INTO Trail(name, time, difficulty, mark, mountain_range) VALUES ('Cabana Capra-Lacul Capra', 3, 'medium', 'blue line', 9)
INSERT INTO Trail(name, time, difficulty, mark, mountain_range) VALUES ('Balea Lac–Saua Caprei Lacul Capra', 1, 'medium', 'red line', 9)
INSERT INTO Trail(name, time, difficulty, mark, mountain_range) VALUES ('Zarnesti – Prapastiile Zarnestiului – Zarnesti', 10, 'hard', 'blue line', 16)
INSERT INTO Trail(name, time, difficulty, mark, mountain_range) VALUES ('Sat Pestera – Dealul Munteanului – Fantana lui Botorog', 6, 'easy', 'red line', 16)
INSERT INTO Trail(name, time, difficulty, mark, mountain_range) VALUES ('Valea Vaserului – statia Paltin – punct belvedere Valea Vaserului', 0.5, 'easy', 'red dot',14)
INSERT INTO Trail(name, time, difficulty, mark, mountain_range) VALUES ('Paltinis – Poiana Gaujoara – saua Batrana', 2, 'medium', 'red cross', 6)
INSERT INTO Trail(name, time, difficulty, mark, mountain_range) VALUES ('Poiana Tapului - Cascada Urlatoarea',1, 'easy', 'blue dot', 2)
INSERT INTO Trail(name, time, difficulty, mark, mountain_range) VALUES ('Varful Parangul Mare', 10, 'hard', 'red dot',15)
INSERT INTO Trail(name, time, difficulty, mark, mountain_range) VALUES ('Balea-Moldoveanu', 14, 'hard', 'blue line', 9)



INSERT INTO TouristicObjective(name, description) VALUES ('Cetatile Ponorului Panorama', 'superbe'), ('Poiana Ponorului', 'foarte frumoasa')
INSERT INTO TouristicObjective(name, description) VALUES ('Pestera Ghetarul Focul Viu', '')
INSERT INTO TouristicObjective(name, description) VALUES ('Cross from Varful Gaina', 'Made out of steel')
INSERT INTO TouristicObjective(name, description) VALUES ('Lacul Avrig', 'Gorgeous')
INSERT INTO TouristicObjective(name, description) VALUES ('Lacul Capra', 'Breathtaking')
INSERT INTO TouristicObjective(name, description) VALUES ('Varful Moldoveanu', 'Incredible')
INSERT INTO TouristicObjective(name, description) VALUES ('Lacul Balea', 'Lac glaciar')


INSERT INTO Trail_Objectives(trailId, objectiveId) VALUES (1, 1), (4, 2)
INSERT INTO Trail_Objectives(trailId, objectiveId) VALUES (5,3)
INSERT INTO Trail_Objectives(trailId, objectiveId) VALUES (12, 3)
INSERT INTO Trail_Objectives(trailId, objectiveId) VALUES (13, 5)
INSERT INTO Trail_Objectives(trailId, objectiveId) VALUES (14, 6)
INSERT INTO Trail_Objectives(trailId, objectiveId) VALUES (15, 6)
INSERT INTO Trail_Objectives(trailId, objectiveId) VALUES (19, 6)
INSERT INTO Trail_Objectives(trailId, objectiveId) VALUES (22, 7)
INSERT INTO Trail_Objectives(trailId, objectiveId) VALUES (22, 8)


INSERT INTO Locality(name, countyId) VALUES ('Glavoi', 15), ('Predeal', 32), ('Vatra Dornei', 13), ('Zarnesti', 9), ('Herculane', 26)
INSERT INTO Locality(name, countyId) VALUES	('Constanta',40), ('Sulina', 39)
INSERT INTO Locality(name, countyId) VALUES ('Busteni', 32)


INSERT INTO RescueCottage(locality) VALUES (1), (2), (3), (4), (5)
INSERT INTO RescueCottage(locality) VALUES (9) -- for delete with IN

INSERT INTO Cottage_Trail(cottageId, trailId, trail_time) VALUES (1, 1, 1.0)
INSERT INTO Cottage_Trail(cottageId, trailId, trail_time) VALUES (1, 2, 2.0)
INSERT INTO Cottage_Trail(cottageId, trailId, trail_time) VALUES (1, 3, 1.0)
INSERT INTO Cottage_Trail(cottageId, trailId, trail_time) VALUES (1, 4, 2.0)
INSERT INTO Cottage_Trail(cottageId, trailId, trail_time) VALUES (1, 5, 3.0)
INSERT INTO Cottage_Trail(cottageId, trailId, trail_time) VALUES (3, 2, 3.0)
INSERT INTO Cottage_Trail(cottageId, trailId, trail_time) VALUES (4, 2, 2.0)
INSERT INTO Cottage_Trail(cottageId, trailId, trail_time) VALUES (8, 7, 2.0)
INSERT INTO Cottage_Trail(cottageId, trailId, trail_time) VALUES (9, 7, 1.0)
INSERT INTO Cottage_Trail(cottageId, trailId, trail_time) VALUES (10, 7, 1.5)
INSERT INTO Cottage_Trail(cottageId, trailId, trail_time) VALUES (8, 8, 1.0)
INSERT INTO Cottage_Trail(cottageId, trailId, trail_time) VALUES (9, 9, 2.0)
INSERT INTO Cottage_Trail(cottageId, trailId, trail_time) VALUES (10, 13, 3.0)
INSERT INTO Cottage_Trail(cottageId, trailId, trail_time) VALUES (10, 14, 2.0)
INSERT INTO Cottage_Trail(cottageId, trailId, trail_time) VALUES (6, 14, 3.5)
INSERT INTO Cottage_Trail(cottageId, trailId, trail_time) VALUES (8, 15, 2)
INSERT INTO Cottage_Trail(cottageId, trailId, trail_time) VALUES (6, 19, 1)
INSERT INTO Cottage_Trail(cottageId, trailId, trail_time) VALUES (9, 19, 1)
INSERT INTO Cottage_Trail(cottageId, trailId, trail_time) VALUES (8, 14, 3)
INSERT INTO Cottage_Trail(cottageId, trailId, trail_time) VALUES (11, 14, 3.5)
INSERT INTO Cottage_Trail(cottageId, trailId, trail_time) VALUES (12, 20, 9.5), (13, 20, 9), (14, 20, 8.5) 
INSERT INTO Cottage_Trail(cottageId, trailId, trail_time) VALUES (15, 19, 6), (16, 19, 8), (17, 19, 10)
INSERT INTO Cottage_Trail(cottageId, trailId, trail_time) VALUES (18, 18, 2), (19, 18, 1.5)


INSERT INTO MountainRefugee(accomodationNumber) VALUES (5), (10), (6), (7)
INSERT INTO MountainRefugee(accomodationNumber) VALUES (8), (9), (12)
INSERT INTO MountainRefugee(accomodationNumber) VALUES (7), (6)
INSERT INTO MountainRefugee(accomodationNumber) VALUES (2), (3), (4)

INSERT INTO Trail_MountainRefugee(trailId, refugeeId) VALUES (1,1), (3, 2)
INSERT INTO Trail_MountainRefugee(trailId, refugeeId) VALUES (13,3), (14, 4)
INSERT INTO Trail_MountainRefugee(trailId, refugeeId) VALUES (7, 5), (9, 6), (11, 7)
INSERT INTO Trail_MountainRefugee(trailId, refugeeId) VALUES (20,8)
INSERT INTO Trail_MountainRefugee(trailId, refugeeId) VALUES (17,9)
INSERT INTO Trail_MountainRefugee(trailId, refugeeId) VALUES (15,10), (15,11), (15,12) --- these are deleted


INSERT INTO RescueEmployee(cnp, lastName, firstName, birthdate, employementDate, rescueCottage, salary)
VALUES ('7000403123456', 'Popescu', 'Alex', '02.06.2000', '10.10.2018', 1, 100), ('6000403123456', 'Pop', 'Ana', '05.03.1999', '12.08.2019', 2, 100)
INSERT INTO RescueEmployee(cnp, lastName, firstName, birthdate, employementDate, rescueCottage, salary)
VALUES ('6000403654321', 'Balc', 'Maria', '09.11.1990', '09.02.2012', 1, 700),   ('6990302576298', 'Craineanu', 'Ioana', '03.02.1999', '19.05.2017', 1, 1000)
INSERT INTO RescueEmployee(cnp, lastName, firstName, birthdate, employementDate, rescueCottage, salary)
VALUES ('7009705181238', 'Nitescu', 'Alex', '05.15.1997', '08.03.2016', 2, 800), ('70980304234989', 'Alexandrescu', 'Alin', '04.03.1998', '02.07.2014', 2, 920),
	   ('7000008091237', 'Queen', 'Oliver', '09.08.2000', '01.09.2019', 2, 200)
INSERT INTO RescueEmployee(cnp, lastName, firstName, birthdate, employementDate, rescueCottage, salary) VALUES
	   ('6980506721828', 'Avram', 'Ana', '05.06.1998', '08.19.2019', 3, 300),    ('7970304752145', 'Grosu', 'Andrei', '08.25.1997', '09.05.2017', 3, 500)
INSERT INTO RescueEmployee(cnp, lastName, firstName, birthdate, employementDate, rescueCottage, salary) VALUES
	   ('6990807123545', 'Sas', 'Anca', '09.04.1999', '12.19.2014', 4, 1300),    ('7970801565821', 'Sas', 'Matei', '08.01.1997', '19.03.2015', 4, 800)
INSERT INTO RescueEmployee(cnp, lastName, firstName, birthdate, employementDate, rescueCottage, salary) VALUES
	   ('6990912672838', 'Pop', 'Andrada', '09.12.1999', '04.07.2020', 5, 200),    ('7980319752145', 'Grigore', 'Alex', '03.29.1998', '11.18.2019', 5, 800)
INSERT INTO RescueEmployee(cnp, lastName, firstName, birthdate, employementDate, rescueCottage, salary) VALUES
	   ('6000921672438', 'Stir', 'Manu', '21.12.1999', '08.21.2018', 4, 500)

-- for delete with IN
INSERT INTO RescueEmployee(cnp, lastName, firstName, birthdate, employementDate, rescueCottage, salary) VALUES
	   ('6000722672438', 'Stir', 'Sandu', '07.22.2000', '08.29.2018', 6, 500)

-- for delete with LIKE
INSERT INTO RescueEmployee(cnp, lastName, firstName, birthdate, employementDate, rescueCottage, salary) VALUES
	   ('6000925154636', 'Bob', 'Sorin', '09.25.2000', '08.29.2021', 6, 500)

/*
SELECT*
FROM County

SELECT *
FROM MountainRange

SELECT *
FROM MountainRange_County

SELECT *
FROM Cottage_Trail

SELECT*
FROM Cottage

SELECT*
FROM Trail

SELECT*
FROM RescueEmployee

SELECT *
FROM MountainRefugee

SELECT*
FROM TouristicObjective

SELECT*
FROM Trail_MountainRefugee

SELECT*
FROM RescueCottage

SELECT*
FROM Locality

SELECT*
FROM Trail_Objectives
*/

--- OR -> Update nb of trails for Prahova and Bihor counties
UPDATE County 
SET nrOfTrailes = 30
WHERE name = 'Prahova' OR name = 'Bihor'

--- AND -> for Cottage.name='Cabana Cetatile Ponorului' & Trail.name ='Poiana Ponorului'
UPDATE Cottage_Trail
SET trail_time = 1.5
WHERE cottageId = 1 AND trailId = 4 

--- NOT -> for all cottages that have the raiting = 0 
UPDATE Cottage
SET raiting = 5
WHERE NOT(raiting <> 0)

--- < -> All employees that have the salary smaller than 100 get a raise :)
UPDATE RescueEmployee
SET salary = 100
WHERE salary < 100

--  >  -> All trails that take longer than 8 hours they enter into hard trail category
UPDATE Trail
SET difficulty = 'hard'
WHERE time > 8.0

--  <=  -> All mountain refugees that can accomadete a number of people smaller than 10, made place for another person.
UPDATE MountainRefugee
SET accomodationNumber = accomodationNumber + 1
WHERE accomodationNumber <= 10

--  =  -> Cottages must accomodate at least 5 people
UPDATE Cottage
SET accomodationNumber = accomodationNumber + 3
WHERE accomodationNumber = 2

--  >=  -> The Rescue organisation needs to lower their budget for a liitel while so they will lower the salaries that are greater than 1000
UPDATE RescueEmployee
SET salary = salary - 50
WHERE salary >= 1000


-- <>  -> The Rescue organisation is being sponsored so they will raise the salaries fro all the employeers that are not fresh hired, the people that have
--		  the salary = with 100 Ron
UPDATE RescueEmployee
SET salary = salary + 110
WHERE salary <> 100

-- NOT NULL 
UPDATE Cottage
SET raiting = raiting + 1
WHERE raiting IS NOT NULL AND raiting <= 4

-- IS NULL -> Cottages that don't have an accomodationNumber
DELETE FROM Cottage
WHERE accomodationNumber IS NULL

--- IN  -> The rescue cottage from Busteni has closed for a period so we need to fire(delete from the database) all its employees
DELETE FROM RescueEmployee
WHERE RescueEmployee.rescueCottage IN (SELECT RescueCottage.id
									   FROM RescueCottage
									   WHERE RescueCottage.locality = 9)

--- BETWEEN -> Delete the mountain refugees that have the accomodation number between 1 and 4 because they are too small
DELETE  
FROM MountainRefugee
WHERE accomodationNumber BETWEEN 1 AND 4

--- LIKE -> Delete all employees that were hired in 2021 because we are in the middle of a pandemic
DELETE FROM RescueEmployee
WHERE RescueEmployee.employementDate LIKE '%.2021'

------------ a) -------------------
--- UNION -> Show all trails that are easy or that pass by a mountain refugee(their id appears in Trail_MountainRefugee table) 
SELECT Trail.id
FROM Trail
WHERE difficulty = 'easy'
UNION
SELECT TM.trailId
FROM Trail_MountainRefugee TM

--- UNION ALL  ->  Show all the Trails that are of medium difficulty OR that are close to a Cottage in Bihor-Padis mountain range
SELECT Trail.id
FROM Trail
WHERE mountain_range = 11 AND difficulty = 'medium'
UNION ALL
SELECT DISTINCT T.id
FROM Trail T, Cottage_Trail CT
WHERE T.id = CT.trailid AND T.mountain_range = 1

--- OR  -> Show all the trails that are easy OR that don't take longer than 1 hour
SELECT Trail.id, Trail.name
FROM Trail
WHERE difficulty = 'easy' OR time <= 2.0 

------------ b) -------------------
--- INTERSECT  -> Show all trails that pass near Cottage Cabana Trei Brazi and also near Cottage Cabana Ursului
SELECT T.name
From Trail T, Cottage_Trail
WHERE T.id = Cottage_Trail.trailId and cottageId = 1
INTERSECT
SELECT T2.name
From Trail T2, Cottage_Trail
WHERE T2.id = Cottage_Trail.trailId and cottageId = 3

--- IN	-> Show top 2 rated Cottages name and their raiting, that are close to Trail Cetatile Ponorului
SELECT C.name, C.raiting
FROM Cottage C
WHERE C.id IN (SELECT TOP 2 CT.cottageId
			   FROM Cottage_Trail CT, Cottage
			   WHERE CT.trailId = 2 and Cottage.id = CT.cottageId
			   ORDER BY Cottage.raiting DESC)


------------ c) -------------------
--- NOT IN  -> Show the touristic objectives that are on the route of medium trails but not on easy trails, from mountain range 'Bihor-Padis'
SELECT TObj.name
FROM TouristicObjective TObj INNER JOIN Trail_Objectives TrObj ON TObj.id = TrObj.objectiveId
INNER JOIN Trail T ON TrObj.trailId = T.id
WHERE T.mountain_range = 1 AND T.difficulty = 'medium' AND
	T.id NOT IN (SELECT T.id
				 FROM Trail T
				 WHERE T.difficulty = 'easy')

--- EXCEPT -> Show all trails except the easy ones
SELECT T.name
From Trail T
EXCEPT
SELECT T2.name
FROM Trail T2
WHERE T2.difficulty = 'easy'


------------ d) -------------------
--- INNER JOIN + at least 2 m To m -> Show the names of the cottages, the names of the trails asscoiated 
---									  with touristic objectives that are in mountain range Bihor-Padis
SELECT C.name AS 'Cottage name', T.name AS 'Trail name', ToObj.name AS 'Touristic Objective' 
FROM Cottage C INNER JOIN Cottage_Trail CT ON C.id = CT.cottageId 
INNER JOIN Trail T ON CT.trailId = T.id
INNER JOIN Trail_Objectives TrObj ON T.id = TrObj.trailId
INNER JOIN TouristicObjective ToObj ON ToObj.id = TrObj.objectiveId
WHERE T.mountain_range = 1

--- LEFT JOIN -> Show the list of localities and the id's of their rescue cottage if they have one
SELECT L.name, RC.id
FROM Locality L LEFT JOIN RescueCottage RC ON L.id = RC.locality

--- RIGHT JOIN -> Show all the names of the touristic objectives and the names of the trails that get you there (if there are any)
SELECT T.name AS 'Trail name', TuObj.name As 'Touristic objective name'
FROM Trail T RIGHT JOIN Trail_Objectives TrObj ON T.id = TrObj.trailId
RIGHT JOIN TouristicObjective TuObj ON TrObj.objectiveId = TuObj.id

--- FULL JOIN -> Show all the counties and all the mountain ranges, all at once
SELECT C.name AS 'County', MR.name AS 'Mountain Range'
FROM County C FULL JOIN MountainRange_County MRC ON C.id = MRC.countyId
FULL JOIN MountainRange MR ON MRC.mountainsId = MR.id


------------ e) -------------------
--- IN with WHERE with suquery -> Show top 3 cottages that are close to trails that go to Lacul Capra
SELECT TOP 3 C.name, C.raiting
FROM Cottage C
WHERE C.id IN (SELECT CT.cottageId 
			   FROM Cottage_Trail CT
			   WHERE CT.trailId IN (SELECT T.id
									FROM Trail T
									WHERE T.id IN (SELECT TrObj.trailId
												   FROM Trail_Objectives TrObj
												   WHERE TrObj.objectiveId IN (SELECT ToObj.id
																			   FROM TouristicObjective ToObj
																			   WHERE ToObj.name = 'Lacul Capra'))))
ORDER BY C.raiting DESC

--- IN with WHERE with subquery -> Show all id's of mountain refugees that are in mountain range Fagaras and have the accomodation number greater or equal with 7
SELECT MR.id, MR.accomodationNumber
FROM MountainRefugee MR
WHERE NOT(MR.accomodationNumber < 7) AND MR.id IN (SELECT TMR.refugeeId
												   FROM Trail_MountainRefugee TMR
												   WHERE TMR.trailId IN (SELECT T.id
												   FROM Trail T
												   WHERE mountain_range = 9))

------------ f) -------------------
--- EXISTS -> Show all cottages from Bihor-Padis mountain range that have trails that take less time if you start them from one of that cottages
SELECT C.id, C.name
FROM Cottage C
WHERE EXISTS (SELECT CT.cottageId
			  FROM Cottage_Trail CT INNER JOIN Trail T ON CT.trailId = T.id
			  WHERE C.id = CT.cottageId AND mountain_range = 1 AND CT.trail_time < T.time)

--- EXISTS -> Show all mountain ranges that have the highest altitude > 2000 and that have at least one hard trail
SELECT MR.name
FROM MountainRange MR
WHERE MR.highest_altitude > 2000 AND EXISTS (SELECT T.id
											 FROM Trail T
											 WHERE MR.id = T.mountain_range AND T.difficulty = 'hard')

------------ g) -------------------	 
--- Query with subquery in FROM -> Show the name of the trails that go to touristic objectives
SELECT DISTINCT CTO.TrailName
FROM (SELECT T.name AS 'TrailName', T.time AS 'Time', ToObj.name AS 'TouristicObjectiveName'
	  FROM Trail T INNER JOIN Trail_Objectives TrObj ON T.id = TrObj.trailId
		   INNER JOIN TouristicObjective ToObj ON ToObj.id = TrObj.objectiveId
		   WHERE T.mountain_range = 9) AS CTO

--- Query with subquery in FROM -> Show the names of mountain ranges that have refugees with accomodation number > 6
SELECT DISTINCT MRangeMRefugee.MounainRangeName
FROM (SELECT MR.name AS 'MounainRangeName', MountainRefugee.id AS 'MountsinRefugeeId', MountainRefugee.accomodationNumber AS 'AccomodationNb'
	  FROM MountainRange MR 
	  INNER JOIN Trail T on MR.id = T.mountain_range
	  INNER JOIN Trail_MountainRefugee TMR ON T.id = TMR.trailId
	  INNER JOIN MountainRefugee ON TMR.refugeeId = MountainRefugee.id) AS MRangeMRefugee
WHERE MRangeMRefugee.AccomodationNb > 6


------------ h) -------------------	 
--- COUNT -> Show all mountain ranges and their number of trails
SELECT MR.name, COUNT(*) AS 'Number of trails'
FROM MountainRange MR INNER JOIN Trail T ON MR.id = T.mountain_range
WHERE EXISTS (SELECT Trail.id
		      FROM Trail
			  WHERE T.mountain_range = Trail.mountain_range AND difficulty = 'easy')
GROUP BY MR.name

--- SUM -> Show the rescue cottages id and their total budget for salaries for a month
SELECT RE.rescueCottage, SUM(RE.salary) AS 'TotalMoney / Month'
FROM RescueEmployee RE
GROUP BY RE.rescueCottage
HAVING COUNT(*) > 2

--- MIN, MAX, AVG -> Show for the mountain ranges that have cottages, the min cottage raiting, max cottage raiting and avg raiting of the cottages from that mountain range
---				where the avg of the raiting is greater or equal than the avg raiting of all cottages from our country
SELECT CMR.MountainRange_name, MIN(CMR.Cottage_raiting) AS 'Minimum cottage raiting', MAX(CMR.Cottage_raiting) AS 'Maximum cottage raiting', 
	   AVG(CMR.Cottage_raiting) AS 'Average Raiting'
FROM (SELECT C.name AS 'Cottage_name', C.raiting AS 'Cottage_raiting', MR.name AS 'MountainRange_name'
	  FROM MountainRange MR, Cottage C 
	  INNER JOIN Cottage_Trail CT ON C.id = CT.cottageId
	  INNER JOIN Trail T ON CT.trailId = T.id
	  WHERE MR.id = T.mountain_range) AS CMR
GROUP BY CMR.MountainRange_name
HAVING AVG(CMR.Cottage_raiting) >= (SELECT AVG(C.raiting) AS 'Total raiting average'
								   FROM MountainRange MR, Cottage C 
								   INNER JOIN Cottage_Trail CT ON C.id = CT.cottageId
								   INNER JOIN Trail T ON CT.trailId = T.id
								   WHERE MR.id = T.mountain_range)

--- MAX, SUM -> Show the rescue cottage id and greatest employee salary, where the greatest salary is greater than a half of the budget for that rescue cottage
SELECT RE.rescueCottage AS 'RescueCottageID', MAX(RE.salary) AS 'Greatest salary'
FROM RescueEmployee RE
GROUP BY RE.rescueCottage
HAVING MAX(RE.salary) > (SELECT (SUM(RescueEmployee.salary) / 2) AS 'Half of total budget'
						 FROM RescueEmployee
						 WHERE RE.rescueCottage = RescueEmployee.rescueCottage)

------------ i) -------------------
--- ALL -> Show the rescue employee that has the greatest salary out of all employees from all counties
SELECT RE.lastName, RE.firstName, RE.salary
FROM RescueEmployee RE
WHERE RE.salary > ALL (SELECT RescueEmployee.salary
					   FROM RescueEmployee
					   WHERE RescueEmployee.id <> RE.id)

--- Alternative with MAX
SELECT RE.lastName, RE.firstName, RE.salary
FROM RescueEmployee RE
WHERE RE.salary = (SELECT MAX(RescueEmployee.salary)
				   FROM RescueEmployee)

 
 --- ALL -> Show the mountain range with the smallest highest altitude 
SELECT MR.name AS 'Mountain Range Name', MR.highest_altitude
FROM MountainRange MR
WHERE MR.highest_altitude < ALL (SELECT MountainRange.highest_altitude
								 FROM MountainRange
								 WHERE MR.id <> MountainRange.id)

--- Alternative with MIN
SELECT MR.name AS 'Mountain Range Name', MR.highest_altitude
FROM MountainRange MR
WHERE MR.highest_altitude = (SELECT MIN(MountainRange.highest_altitude)
						     FROM MountainRange)


--- ANY -> Show all trails that have at least one cottage near them
SELECT *
FROM Cottage C
WHERE C.id = ANY (SELECT CT.cottageId
				  FROM Cottage_Trail CT)

--- Alternative with NOT IN
SELECT *
FROM Cottage C
WHERE C.id NOT IN (SELECT Cottage.id
					 FROM Cottage
					 WHERE  Cottage.id NOT IN (SELECT CT.cottageId
											   FROM Cottage_Trail CT))


--- ANY -> Show all counties that have at least one mountain range related to them
SELECT C.id, C.name AS 'County Name'
FROM County C
WHERE C.id = ANY  (SELECT MRC.countyId
				   FROM MountainRange_County MRC)

--- Alternative with IN
SELECT C.id, C.name AS 'County Name'
FROM County C
WHERE C.id IN (SELECT MRC.countyId
			   FROM MountainRange_County MRC)
