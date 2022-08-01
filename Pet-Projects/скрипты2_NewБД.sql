CREATE TABLE Staff (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    position VARCHAR(30),
    birthday DATE NOT NULL,
    has_child BOOLEAN DEFAULT(0) NOT NULL,
    phone VARCHAR(20) UNIQUE NOT NULL
);
DROP TABLE staff;
SELECT * FROM staff;
SELECT * FROM february;
DROP TABLE march_sql;
DROP TABLE check2_sql;

ALTER TABLE check2_sql DROP COLUMN ABC_XYZ;

ALTER TABLE check2_sql ADD COLUMN ABC_XYZ TEXT NOT NULL;

UPDATE check2_sql SET ABC_XYZ = CONCAT(ABC, " ", XYZ);
SELECT * FROM check2_sql;

-- SELECT CONCAT(ABC, " ", XYZ) AS ABC_XYZ FROM check2_sql;

CREATE TABLE `march` (
  `id_tov_cl` int DEFAULT NULL,
  `BaseSum` double DEFAULT NULL,
  `name_gr2` text,
  `ABC` text,
  `XYZ` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOAD DATA INFILE 'C:\mysql_dump\March_SQL.csv' 
INTO TABLE february  
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY 'n'
IGNORE 1 ROWS;

TRUNCATE march;