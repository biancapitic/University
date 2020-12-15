--- a) modify the type of a column tinyint to int -> V1
CREATE PROCEDURE uspModifyAccomodationNumberTypeToTinyint
AS
	ALTER TABLE MountainRefugee
	ALTER COLUMN accomodationNumber TINYINT
GO

EXEC uspModifyAccomodationNumberTypeToTinyint

CREATE PROCEDURE uspModifyAccomodationNumberTypeToTinyintReverse
AS
	ALTER TABLE MountainRefugee
	ALTER COLUMN accomodationNumber INT
GO

EXEC uspModifyAccomodationNumberTypeToTinyintReverse

--- b) add a column  -> V2

CREATE PROCEDURE uspAddColumn_OpeningYear_to_Cottage
AS
ALTER TABLE Cottage
ADD openingYear INT
GO

EXEC uspAddColumn_OpeningYear_to_Cottage

CREATE PROCEDURE uspAddColumn_OpeningYear_to_Cottage_Reverse
AS
ALTER TABLE Cottage
DROP COLUMN openingYear
GO

EXEC uspAddColumn_OpeningYear_to_Cottage_Reverse


--- c) add a DEFAULT constraint -> V3
CREATE PROCEDURE uspAddDefaultCottageAccNumber
AS
	ALTER TABLE Cottage
	ADD CONSTRAINT df_AccNumber DEFAULT 0 FOR accomodationNumber
GO

EXEC uspAddDefaultCottageAccNumber


CREATE PROCEDURE uspAddDefaultCottageAccNumberReverse
AS
	ALTER TABLE Cottage
	DROP CONSTRAINT df_AccNumber
GO

EXEC uspAddDefaultCottageAccNumberReverse


--- d) add a primary key  -> V4
CREATE PROCEDURE uspRemovePrimaryKeyRescueEmployee
AS
	ALTER TABLE RescueEmployee
	DROP CONSTRAINT PK_RescueEmployeeId
GO

EXEC uspRemovePrimaryKeyRescueEmployee


CREATE PROCEDURE uspRemovePrimaryKeyRescueEmployeeReverse
AS
	ALTER TABLE RescueEmployee
	ADD CONSTRAINT PK_RescueEmployeeId PRIMARY KEY(id)
GO

EXEC uspRemovePrimaryKeyRescueEmployeeReverse

--- e) add a candidate key -> V5
CREATE PROCEDURE uspAddCandidateKeyTrailName
AS
	ALTER TABLE Trail
	ADD CONSTRAINT UQ_Name UNIQUE (name)
GO

EXEC uspAddCandidateKeyTrailName


CREATE PROCEDURE uspAddCandidateKeyTrailNameRemove
AS
	ALTER TABLE Trail
	DROP CONSTRAINT UQ_Name
GO

EXEC uspAddCandidateKeyTrailNameRemove


--- f) remove a foreign key -> V6
CREATE PROCEDURE uspRemoveForeignKeyRescueCottageId
AS
	ALTER TABLE RescueEmployee
	DROP CONSTRAINT Fk_RescueCottageId
GO

EXEC uspRemoveForeignKeyRescueCottageId

CREATE PROCEDURE uspRemoveForeignKeyRescueCottageIdReverse
AS
	ALTER TABLE RescueEmployee
	ADD CONSTRAINT Fk_RescueCottageId FOREIGN KEY(rescueCottage) REFERENCES RescueCottage(id)
GO

EXEC uspRemoveForeignKeyRescueCottageIdReverse

--- g) create a table -> V7
CREATE PROCEDURE uspCreateTableAnimal
AS
	CREATE TABLE Animal(id TINYINT IDENTITY (1,1), name VARCHAR(50), PRIMARY KEY(id))
GO

EXEC uspCreateTableAnimal

CREATE PROCEDURE uspCreateTableAnimalReverse
AS
	DROP TABLE Animal
GO

EXEC uspCreateTableAnimalReverse

--- Create a new table that holds the current version of the database schema. Simplifying assumption: the version is an integer number.

CREATE TABLE Version(
version TINYINT 
PRIMARY KEY (version))

INSERT INTO Version(version) VALUES (7)

UPDATE Version
SET version = 0

SELECT*
FROM Version


CREATE TABLE DBProcedures(
version TINYINT IDENTITY(1,1),
uspProcedure VARCHAR(80),
uspReverseProcedure VARCHAR(80))

SELECT *
FROM DBProcedures

SELECT*
FROM Animal

INSERT INTO DBProcedures(uspProcedure, uspReverseProcedure) 
		VALUES ('uspModifyAccomodationNumberTypeToTinyint','uspModifyAccomodationNumberTypeToTinyintReverse'),
			   ('uspAddColumn_OpeningYear_to_Cottage','uspAddColumn_OpeningYear_to_Cottage_Reverse'),
			   ('uspAddDefaultCottageAccNumber','uspAddDefaultCottageAccNumberReverse'),
			   ('uspRemovePrimaryKeyRescueEmployee','uspRemovePrimaryKeyRescueEmployeeReverse'),
			   ('uspAddCandidateKeyTrailName','uspAddCandidateKeyTrailNameRemove'),
			   ('uspRemoveForeignKeyRescueCottageId','uspRemoveForeignKeyRescueCottageIdReverse'),
			   ('uspCreateTableAnimal','uspCreateTableAnimalReverse')

CREATE PROCEDURE changeVersion @updatedVersion INT
AS
	UPDATE Version
	SET version = @updatedVersion
GO


CREATE PROCEDURE changeVersionOfDb @version INT
AS
	DECLARE @currentVersion INT
	SET @currentVersion = (SELECT version FROM Version)
	IF (@currentVersion > @version)
		WHILE (@currentVersion > @version)
		BEGIN
			PRINT @currentVersion
			DECLARE @reverseCmd VARCHAR(80) 
			SET @reverseCmd = (SELECT uspReverseProcedure FROM DBProcedures WHERE @currentVersion = version)
			EXEC @reverseCmd
			PRINT @reverseCmd
		SET @currentVersion = @currentVersion - 1
		END
	ELSE IF (@currentVersion < @version)
		WHILE (@currentVersion < @version)
		BEGIN
			SET @currentVersion = @currentVersion + 1
			PRINT @currentVersion
			DECLARE @cmd VARCHAR(80) 
			SET @cmd = (SELECT uspProcedure FROM DBProcedures WHERE version = @currentVersion)
			EXEC @cmd
			PRINT @cmd
		END
	EXEC changeVersion @currentVersion
GO

EXEC changeVersionOfDb 2

DROP PROCEDURE changeVersionOfDb
