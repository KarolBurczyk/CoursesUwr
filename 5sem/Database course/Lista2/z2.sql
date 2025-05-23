DROP TABLE IF EXISTS fldata;
DROP TABLE IF EXISTS firstnames;
DROP TABLE IF EXISTS lastnames;

CREATE TABLE firstnames
(
    id INT IDENTITY(1,1) PRIMARY KEY,
    firstname VARCHAR(50) NOT NULL
);

CREATE TABLE lastnames
(
    id INT IDENTITY(1,1) PRIMARY KEY,
    lastname VARCHAR(50) NOT NULL
);

CREATE TABLE fldata
(
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    PRIMARY KEY (firstname, lastname)
);

INSERT INTO firstnames (firstname) VALUES 
('Paweł'), ('Jan'), ('Anna'), ('Jolanta'), ('Michałek');

INSERT INTO lastnames (lastname) VALUES 
('Kowaski'), ('Pawłowicz'), ('Chełmnowski'), ('Rajba'), ('Lewandowski');

CREATE PROCEDURE GenerateRandomPairs
    @n INT
AS
BEGIN
    DECLARE @totalPairs INT;
    
    SELECT @totalPairs = COUNT(*) 
    FROM firstnames f
    CROSS JOIN lastnames l;
    
    IF @n > @totalPairs
    BEGIN
        THROW 30001, 'The requested number of pairs exceeds the number of available unique pairs.', 1;
    END
    
    DELETE FROM fldata;

    INSERT INTO fldata (firstname, lastname)
    SELECT TOP (@n) f.firstname, l.lastname
    FROM firstnames f
    CROSS JOIN lastnames l
    ORDER BY NEWID();
END;
GO

EXEC GenerateRandomPairs @n = 5;

SELECT * FROM fldata;