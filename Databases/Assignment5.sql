CREATE TABLE Ta(
aid INT IDENTITY,
a2 INT UNIQUE,
a3 INT,
a4 varchar(50),
PRIMARY KEY(aid))

CREATE TABLE Tb(
bid INT IDENTITY,
b2 INT,
b3 VARCHAR(50),
b4 VARCHAR(50),
PRIMARY KEY(bid))

CREATE TABLE Tc(
cid INT IDENTITY,
aid INT,
bid INT,
PRIMARY KEY (cid),
FOREIGN KEY(aid) REFERENCES Ta(aid),
FOREIGN KEY(bid) REFERENCES Tb(bid))

CREATE OR ALTER VIEW view_selectAllTa
AS
SELECT *
FROM Ta
GO

EXEC usp_addNewTest 'test5', 'Tc,Tb,Ta', 'view_selectAllTa', 200

EXEC usp_testRun 'test5'

SELECT * FROM Ta
SELECT * FROM Tb
SELECT * FROM Tc

-- -> a)
---- Clustered index scan 
SELECT *
FROM Ta
WHERE a3 > 100
-- -> 0.042196

---- Clustered index seek 
SELECT * 
FROM Ta
WHERE aid > 20 and aid < 100
-- -> 0.0033651

---- NonClustered index scan
SELECT a2
FROM Ta
-- -> 0.0034789

---- NonClustered index seek
SELECT a2
FROM Ta
WHERE a2 < 200
-- -> 0.0033172

---- Key lookup 
SELECT *
FROM Ta
WHERE a2 = 942


-- -> b)
SELECT b2, b3
FROM Tb

--- before 
--- I/O Cost - 0.0038
--- Operator Cost - 0.0042
--- Subtree Cost - 0.0042
--- CPU Cost - 0.00035

CREATE NONCLUSTERED INDEX NCIDX_Tb ON dbo.Tb(b2) INCLUDE(b3)
GO
--- after 
--- I/O Cost - 0.0031
--- Operator Cost - 0.0034
--- Subtree Cost - 0.0034
--- CPU Cost - 0.00035

-- -> c)

CREATE OR ALTER VIEW view_TaAndTb
AS
SELECT Tb.b2, Tb.b3, Tc.cid
FROM Tb INNER JOIN Tc ON Tc.bid = Tb.bid
WHERE Tc.bid > 50
GO

SELECT * FROM view_TaAndTb

-- Clustered Index Tb - 0.0042427 - operator cost
-- Sort input of Tc   - 0.0127854 - operator cost
-- Clustered Index Tc - 0.003425 - operator cost

DROP INDEX index_Tc_bid ON Tc

CREATE NONCLUSTERED INDEX index_Tc_bid ON dbo.Tc(bid)

-- Clustered Index Tb - 0.0042427 - operator cost
-- NonClustered Index Tc - 0.0034778 - operator cost

