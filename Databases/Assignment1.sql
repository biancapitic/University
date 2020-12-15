drop database MountainTrails

create database MountainTrails

go
use MountainTrails
go

CREATE TABLE Region
(id TINYINT IDENTITY(1,1),
 name VARCHAR(50) NOT NULL,
 PRIMARY KEY(id))

CREATE TABLE County
(id TINYINT IDENTITY(1,1),
 name VARCHAR(50) NOT NULL,
 nrOfTrailes INT,
 regionId TINYINT,
 PRIMARY KEY(id),
 FOREIGN KEY(regionId) REFERENCES Region(id))

 CREATE TABLE Locality
 (id TINYINT IDENTITY(1,1),
  name VARCHAR(50) NOT NULL,
  countyId TINYINT,
  PRIMARY KEY(id),
  FOREIGN KEY(countyId) REFERENCES County(id))

 CREATE TABLE MountainRange
 (id TINYINT IDENTITY(1,1),
  name VARCHAR(50) NOT NULL,
  highest_altitude DECIMAL(7,2),
  PRIMARY KEY(id))

  CREATE TABLE MountainRange_County
  (countyId TINYINT REFERENCES County(id),
   mountainsId TINYINT REFERENCES MountainRange(id),
   PRIMARY KEY(countyId, mountainsId))

 CREATE TABLE Trail
 (id TINYINT IDENTITY(1,1),
  name VARCHAR(200) NOT NULL,
  time DECIMAL(5,2),
  difficulty VARCHAR(10),
  mark VARCHAR(10),
  mountain_range TINYINT,
  PRIMARY KEY(id),
  FOREIGN KEY(mountain_range) REFERENCES MountainRange(id))

  CREATE TABLE Cottage
 (id TINYINT IDENTITY(1,1),
  name VARCHAR(40) NOT NULL,
  accomodationNumber INT,
  raiting TINYINT DEFAULT 0,
  PRIMARY KEY(id),
  CHECK (raiting <= 10))

  CREATE TABLE Cottage_Trail
  (cottageId TINYINT REFERENCES Cottage(id),
   trailId TINYINT REFERENCES Trail(id),
   trail_time DECIMAL (5,2),
   PRIMARY KEY(cottageId, trailId))

 CREATE TABLE TouristicObjective
 (id TINYINT IDENTITY(1,1),
  name VARCHAR(50),
  description VARCHAR(100),
  PRIMARY KEY(id))

 CREATE TABLE Trail_Objectives
 (trailId TINYINT REFERENCES Trail(id),
  objectiveId TINYINT REFERENCES TouristicObjective(id),
  PRIMARY KEY(trailId, objectiveId))

  CREATE TABLE MountainRefugee
   (id TINYINT IDENTITY(1,1),
    accomodationNumber INT NOT NULL,
	PRIMARY KEY(id))

  CREATE TABLE Trail_MountainRefugee
	(trailId TINYINT REFERENCES Trail(id),
	 refugeeId TINYINT REFERENCES MountainRefugee(id),
	 PRIMARY KEY(trailId, refugeeId))

  CREATE TABLE RescueCottage
   (id TINYINT IDENTITY(1,1),
    locality TINYINT NOT NULL,
    PRIMARY KEY(id),
	FOREIGN KEY(locality) REFERENCES Locality(id))

  CREATE TABLE RescueEmployee
  (id TINYINT IDENTITY(1,1),
   cnp CHAR(14) UNIQUE NOT NULL,
   firstName VARCHAR(20) NOT NULL,
   lastName VARCHAR(20) NOT NULL,
   birthdate CHAR(10) NOT NULL,
   employementDate CHAR(10) NOT NULL,
   rescueCottage TINYINT NOT NULL,
   salary INTEGER DEFAULT 0,
   PRIMARY KEY(id),
   CONSTRAINT FK_RescueCottageId FOREIGN KEY(rescueCottage) REFERENCES RescueCottage(id))
