IF OBJECT_ID('tempdb..#LocalTempTable') IS NOT NULL
BEGIN
    DROP TABLE #LocalTempTable;
END

IF OBJECT_ID('tempdb..##GlobalTempTable') IS NOT NULL
BEGIN
    DROP TABLE ##GlobalTempTable;
END

DECLARE @TableVar TABLE (
    ID INT, 
    Name NVARCHAR(30)
);

CREATE TABLE #LocalTempTable (
    ID INT, 
    Name NVARCHAR(30)
);

INSERT INTO #LocalTempTable VALUES (
    1, 
    'LocalTemp1'
);

CREATE TABLE ##GlobalTempTable (
    ID INT, 
    Name NVARCHAR(30)
);

INSERT INTO ##GlobalTempTable VALUES (
    1, 
    'GlobalTemp1'
);

INSERT INTO @TableVar VALUES (
    1, 
    'TableVar1'
);

SELECT * 
FROM tempdb.INFORMATION_SCHEMA.TABLES 
WHERE TABLE_NAME LIKE '#LocalTempTable%' OR TABLE_NAME LIKE '##GlobalTempTable%'OR TABLE_NAME LIKE '@TableVar';

SELECT * FROM #LocalTempTable;

SELECT * FROM ##GlobalTempTable;

SELECT * FROM @TableVar;