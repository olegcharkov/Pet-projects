use csv_export;

select * from february f;

ALTER TABLE march  ADD COLUMN ABC_XYZ TEXT NOT NULL;
alter table may_sql  rename to may; 
alter table location drop column format;

UPDATE march SET ABC_XYZ = CONCAT(ABC, " ", XYZ);

SELECT * from march;


CREATE TABLE february(
  id_tov_cl INT NOT NULL AUTO_INCREMENT,
  BaseSum VARCHAR(255) NOT NULL,
  name_gr2 TEXT NOT NULL,
  ABC TEXT NOT NULL,
  XYZ TEXT NOT NULL,
  PRIMARY KEY (id_tov_cl)
);

drop table april_sql ;
select * from location l ; 

SET GLOBAL local_infile=1;
show variables like "local_infile";

LOAD DATA LOCAL INFILE 'C:/mysql_dump/March_SQL.csv' 
INTO TABLE march  
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 rows;

show variables like "local_infile";