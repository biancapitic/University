
--- -> This view shows all the trails with all their information

CREATE VIEW viewGetAllTrails
AS(
SELECT *
FROM Trail
)
GO

SELECT * FROM viewGetAllTrails
--- -> This view shows the names of the cottages and the names of the trails asscoiated with them that are in mountain range with id 1

CREATE VIEW viewGetCottagesAndTrailsFromMountainRange
AS(
SELECT C.name AS 'Cottage name', T.name AS 'Trail name'
FROM Cottage C INNER JOIN Cottage_Trail CT ON C.id = CT.cottageId 
INNER JOIN Trail T ON CT.trailId = T.id
WHERE T.mountain_range = 1
)
GO

SELECT * FROM viewGetCottagesAndTrailsFromMountainRange

--- -> This view shows all the Mountain ranges and their number of trails

CREATE VIEW viewGetMountainRangeAndNrOfTrails
AS(
SELECT MR.name, COUNT(*) AS 'Number of trails'
FROM MountainRange MR INNER JOIN Trail T ON MR.id = T.mountain_range
WHERE EXISTS (SELECT Trail.id
		      FROM Trail
			  WHERE T.mountain_range = Trail.mountain_range)
GROUP BY MR.name
)

SELECT * FROM viewGetMountainRangeAndNrOfTrails

--- Gets the list of table names as a string, the testId and the number of rows that are going to be inserted in that table

CREATE OR ALTER PROC usp_addTables @tables VARCHAR(500), @testId INT, @nrRows INT
AS
	--- The tables are given in the right order. Position starts from 1 to n.
	--- Having position = 1 it means that this is the first table from where we are going to delete data and
	---		it is the last table in which we are going to insert data
	--- Having position = n it means that this is the last table from where we are going to delete data and 
	---		it is the first table in which we are going to insert data
	DECLARE @position TINYINT
	SET @position = 1

	DECLARE @tableName VARCHAR(50)
	
	--- We parse all the table names with the help of the cursor

	DECLARE TablesCursor CURSOR FOR
		SELECT value
		FROM string_split(@tables, ',')
	OPEN TablesCursor
	FETCH TablesCursor
	INTO @tableName
	WHILE @@FETCH_STATUS = 0
	BEGIN
		DECLARE @tableId INT
		--- if the table name is not already in the Tables table we insert it
		IF (SELECT COUNT(*) FROM Tables WHERE Tables.Name = @tableName) = 0
		BEGIN
			INSERT INTO Tables VALUES (@tableName)
		END
		--- we get the table Id
		SET @tableId = (SELECT Tables.TableID FROM Tables WHERE Tables.Name = @tableName)

		--- we insert data into TestTables: testId, tableId, the number of rows to be inserted, the position of the table
		INSERT INTO TestTables VALUES (@testId, @tableId, @nrRows, @position)
		SET @position = @position + 1
		
		FETCH TablesCursor
		INTO @tableName
	END
	CLOSE TablesCursor
	DEALLOCATE TablesCursor
GO

--- Gets the list of view names as a string and the testId

CREATE OR ALTER PROC usp_addViews @views VARCHAR(500), @testId INT
AS
	--- We split the string containing the names of the views and we put them into TesViews table
	DECLARE @viewName VARCHAR(50)

	DECLARE ViewsCursor CURSOR FOR
	SELECT value
	FROM string_split(@views, ',')
	OPEN ViewsCursor
	FETCH ViewsCursor
	INTO @viewName
	WHILE @@FETCH_STATUS = 0
	BEGIN
		DECLARE @viewId INT

		IF (SELECT COUNT(*) FROM Views WHERE Views.Name = @viewName) = 0
			BEGIN
				INSERT INTO Views VALUES (@viewName)
			END

		SET @viewId = (SELECT Views.ViewID FROM Views WHERE Views.Name = @viewName)
		INSERT INTO TestViews VALUES (@testId, @viewId)
		
		FETCH ViewsCursor
		INTO @viewName
	END
	CLOSE ViewsCursor
	DEALLOCATE ViewsCursor
GO

--- It inserts a new test(it inserts the tables and the views recevied as parameters)

CREATE OR ALTER PROC usp_addNewTest @testName VARCHAR(50), @tables VARCHAR (500), @views VARCHAR (800), @nrRows INT
AS
	DECLARE @testId INT

	INSERT INTO Tests VALUES (@testName)
	SET @testId = (SELECT Tests.TestID FROM Tests WHERE Tests.Name = @testName)

	EXEC usp_addTables @tables, @testId, @nrRows
	EXEC usp_addViews @views, @testId
GO

----------------- RUN TEST -----------------

--- We delete all data from the tables that we use in the current test

CREATE OR ALTER PROC usp_deleteFromTables @testId INT, @testRunId INT
AS
	DECLARE @tableName VARCHAR(50)
	DECLARE @tableId INT
	
	-- We parse with a cursor the names of the tables
	DECLARE TestTablesCursor CURSOR FOR
	SELECT Tables.Name, Tables.TableID
	FROM TestTables INNER JOIN Tables ON TestTables.TableID = Tables.TableID
	WHERE TestTables.TestID = @testId
	OPEN TestTablesCursor
	FETCH TestTablesCursor
	INTO @tableName, @tableId
	WHILE @@FETCH_STATUS = 0
	BEGIN
		-- we delete all the data from the table
		DECLARE @deleteAllFromTable VARCHAR(100)
		SET @deleteAllFromTable = 'DELETE FROM ' + @tableName
		EXEC (@deleteAllFromTable)

		-- we check using system tables if the current table uses identity for any of its columns, if it does we do a reseed from 0
		
		-- we select from all the columns the ones that are in our current table and that have type identity and we count them
		-- if there is at least one column with type identity in this table we reseed the identity value
		IF (SELECT COUNT(C.is_identity)
			FROM sys.columns AS C
			INNER JOIN sys.tables AS T ON C.object_id = T.object_id
			INNER JOIN sys.types AS Typ ON C.system_type_id = Typ.system_type_id
			WHERE T.name = @tableName AND C.is_identity = 1) > 0

			DBCC CHECKIDENT (@tableName, RESEED, 0)

		FETCH TestTablesCursor
		INTO @tableName, @tableId

	END
	CLOSE TestTablesCursor
	DEALLOCATE TestTablesCursor
GO

--- we insert data into the table given as parameter

CREATE OR ALTER PROC usp_insertIntoTable @tableName VARCHAR(50), @testId INT, @tableId INT
AS
	DECLARE @nrRows INT

	-- we get the nb of rows that we need to insert for this table
	SET @nrRows = (SELECT TestTables.NoOfRows FROM TestTables WHERE TestTables.TestID = @testId AND TestTables.TableID = @tableId)
	DECLARE @index INT
	SET @index = 1

	DECLARE @columnName VARCHAR(50)
	DECLARE @columnType VARCHAR(50)
	DECLARE @isIdentity BIT

	-- on each iteration we declare a new query and use a cursor to iterate through each column
	WHILE @index <= @nrRows
	BEGIN
		DECLARE @query NVARCHAR(200)
		SET @query = 'INSERT INTO ' + @tableName + '('
		DECLARE @queryValues NVARCHAR(200)
		SET @queryValues = ' VALUES('
		DECLARE @randNb INT

		--- we parse with a cursor a table containing this infromation for each column in the table: 
		--- column name, column type, idnetity(1 if it uses identity, 0 otherwise)

		DECLARE ColumnsCursor CURSOR FOR
		SELECT DISTINCT C.name AS 'ColumnName', Typ.name AS 'Type', C.is_identity AS 'Identity'
		FROM sys.columns AS C
		INNER JOIN sys.tables AS T ON C.object_id = T.object_id
		INNER JOIN sys.types AS Typ ON C.system_type_id = Typ.system_type_id
		WHERE T.name = @tableName
		OPEN ColumnsCursor
		FETCH ColumnsCursor
		INTO @columnName, @columnType, @isIdentity
		WHILE @@FETCH_STATUS = 0
		BEGIN

			-- we check if it's a foreign key
		  IF(SELECT COUNT(*)
			FROM sys.foreign_key_columns fkc
			INNER JOIN sys.objects obj ON obj.object_id = fkc.constraint_object_id
			INNER JOIN sys.tables tab ON tab.object_id = fkc.parent_object_id
			INNER JOIN sys.columns col ON col.column_id = parent_column_id AND col.object_id = tab.object_id
			WHERE tab.name = @tableName AND col.name = @columnName) > 0
			BEGIN
				-- if it's a foreign key we simply put the value of the index(current row nb) because we know that that value exists in the parent table
				SET @queryValues = @queryValues + (SELECT CAST(@index AS NVARCHAR)) + ', '
				SET @query = @query + @columnName + ','
			END
		  ELSE 
			BEGIN
				-- check for identity constraint
				IF @isIdentity = 0
					BEGIN
						SET @query = @query + @columnName + ','
						-- check column type
						IF @columnType = 'int' OR @columnType = 'decimal'
							BEGIN
								-- generate random nb
								SET @randNb = (SELECT RAND() * 1000)
								SET @queryValues = @queryValues + (SELECT CAST(@randNb AS NVARCHAR)) + ','
							END
						IF @columnType = 'tinyint'
							BEGIN
								-- generate random nb
								SET @randNb = (SELECT RAND() * 10) -- it must be < 10
								SET @queryValues = @queryValues + (SELECT CAST(@randNb AS NVARCHAR)) + ','
							END
						IF @columnType = 'varchar' OR @columnType = 'char'
							BEGIN
								-- generate random string
								SET @randNb = (SELECT RAND() * 1000)
								SET @queryValues = @queryValues + ' ''Random string number: ' + (SELECT CAST(@randNb AS NVARCHAR)) + ''','
							END
					END
			END	
			FETCH ColumnsCursor
			INTO @columnName, @columnType, @isIdentity
		END
		CLOSE ColumnsCursor
		DEALLOCATE ColumnsCursor

		-- we add queryValues to the query and we execute the query
		SET @queryValues =  SUBSTRING(@queryValues, 1, (len(@queryValues) - 1))
		SET @queryValues = @queryValues + ')'
		SET @query =  SUBSTRING(@query, 1, (len(@query) - 1))
		SET @query = @query + ')' + @queryValues
		EXEC (@query)
		SET @index = @index + 1
	END
GO

--- we insert data into tables

CREATE OR ALTER PROC usp_insertDataToTables @testId INT, @testRunId INT
AS
	DECLARE @tableName VARCHAR(50)
	DECLARE @tableId INT

	-- parse the table names with a cursor 
	DECLARE TablesCursor CURSOR FOR
	SELECT Tables.Name, Tables.TableID
	FROM TestTables INNER JOIN Tables ON TestTables.TableID = Tables.TableID
	WHERE TestTables.TestID = @testId
	ORDER BY TestTables.Position DESC
	OPEN TablesCursor
	FETCH TablesCursor
	INTO @tableName, @tableId
	WHILE @@FETCH_STATUS = 0
	BEGIN
		-- get start date and time
		DECLARE @startAt datetime2
		SET @startAt = (SELECT CURRENT_TIMESTAMP)

		EXEC usp_insertIntoTable @tableName, @testId, @tableId

		-- get end date and time
		DECLARE @endAt datetime2
		SET @endAt = (SELECT CURRENT_TIMESTAMP)
		
		INSERT INTO TestRunTables VALUES(@testRunId, @tableId, @startAt, @endAt)

		FETCH TablesCursor
		INTO @tableName, @tableId

	END
	CLOSE TablesCursor
	DEALLOCATE TablesCursor
GO


--- we execute the views from the table TestViews
CREATE OR ALTER PROC usp_execViews @testId INT, @testRunId INT
AS
	DECLARE @viewName NVARCHAR(50)
	DECLARE @selectView NVARCHAR(200)
	DECLARE @viewId INT
	
	--- We get the name and the id of each view for the current test
	DECLARE ViewsCursor CURSOR FOR
	SELECT V.Name, V.ViewID
	FROM TestViews TV INNER JOIN Views V ON TV.ViewID = V.ViewID
	WHERE TV.TestID = @testId
	OPEN ViewsCursor
	FETCH ViewsCursor
	INTO @viewName, @viewId
	WHILE @@FETCH_STATUS = 0
	BEGIN
		
		-- get start date and time
		DECLARE @startAt datetime2
		SET @startAt = (SELECT CURRENT_TIMESTAMP)

		-- get results of the view
		SET @selectView = 'SELECT * FROM ' + @viewName
		EXEC (@selectView)

		-- get end date and time
		DECLARE @endAt datetime2
		SET @endAt = (SELECT CURRENT_TIMESTAMP)

		INSERT INTO TestRunViews VALUES (@testRunId, @viewId, @startAt, @endAt)

		FETCH ViewsCursor
		INTO @viewName, @viewId
	END
	CLOSE ViewsCursor
	DEALLOCATE ViewsCursor
GO

--- ths is the procedure that does a test run
CREATE OR ALTER PROC usp_testRun @testName VARCHAR(50)
AS
	DECLARE @testId INT
	SET @testId = (SELECT Tests.TestID FROM Tests WHERE Tests.Name = @testName)

	-- get the start date and time and we insert it into TestRuns table
	DECLARE @startAt datetime2
	SET @startAt = (SELECT CURRENT_TIMESTAMP)
	INSERT INTO TestRuns(Description, StartAt) VALUES(@testName, @startAt)

	-- declare and initialize an id for the test, we get it from the current value of identity
	DECLARE @testRunId INT
	SET @testRunId = @@IDENTITY

	-- delete all data from the table used in this test run
	EXEC usp_deleteFromTables @testID, @testRunId

	-- insert data into tables used in this test run
	EXEC usp_insertDataToTables @testID, @testRunId

	-- get results of the views of this test
	EXEC usp_execViews @testID, @testRunId

	-- get end date and time of the test run
	DECLARE @endAt datetime2
	SET @endAt = (SELECT CURRENT_TIMESTAMP)

	-- insert the end date and time into the TestRuns table
	UPDATE TestRuns
	SET TestRuns.EndAt = @endAt
	WHERE TestRuns.TestRunID = @testRunId
GO


SELECT * FROM Trail
SELECT * FROM Cottage
SELECT * FROM Cottage_Trail
SELECT * FROM MountainRange

EXEC usp_testRun 'test1'

EXEC usp_addNewTest 'test1', 'Cottage_Trail,Cottage,Trail,MountainRange', 
					'viewGetMountainRangeAndNrOfTrails,viewGetCottagesAndTrailsFromMountainRange,viewGetAllTrails', 500


EXEC usp_addNewTest 'test2', 'Cottage_Trail,Cottage,Trail,MountainRange', 
					'viewGetMountainRangeAndNrOfTrails,viewGetCottagesAndTrailsFromMountainRange,viewGetAllTrails', 700

EXEC usp_testRun 'test2'

EXEC usp_addNewTest 'test3', 'Cottage_Trail,Cottage,Trail,MountainRange', 
					'viewGetMountainRangeAndNrOfTrails,viewGetCottagesAndTrailsFromMountainRange,viewGetAllTrails', 200

EXEC usp_testRun 'test3'



SELECT * FROM Tables
SELECT * FROM Tests
SELECT * FROM Views
SELECT * FROM TestTables
SELECT * FROM TestViews
SELECT * FROM TestRuns
SELECT * FROM TestRunTables
SELECT * FROM TestRunViews