CREATE DATABASE IF NOT EXISTS zillowData;
use zillowData;

create table IF NOT EXISTS tblZillowImport
(
    ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    house text,
    Car_Garage int null,
    Living_Space_sq_ft int null,
	Beds int null,
	Baths NUMERIC null,
	Zip int null,
	Year int null,
	List_Price int null
);

INSERT INTO tblZillowImport (house,Car_Garage, Living_Space_sq_ft, Beds, Baths, Zip, Year, List_Price) VALUES
    ('James',1,2222,3,3.5,32312,1981,250000),
    ('Ryder',2,1628,3,2,32308,2009,185000),
    ('Artesian',1,3824,5,4,32312,1954,399000),
    ('Mauritania',3,1137,3,2,32309,1993,150000),
    ('Synecologically',1,3560,6,4,32309,1973,315000),
    ('Joinable',5,2893,4,3,32312,1994,699000),
    ('Questioning',0,3631,4,3,32309,1996,649000),
    ('Doubtingly',3,2483,4,3,32312,2016,399000),
    ('Moity',1,2400,4,4,32312,2002,613000),
    ('Resolvedly',0,1997,3,3,32311,2006,295000),
    ('Defeasibility',1,2097,4,3,32311,2016,290000),
    ('Zotation',1,3200,5,4,32312,1964,465000),
    ('Handloader',3,4892,5,6,32311,2005,799900),
    ('Staumeral',0,1128,2,1,32303,1955,89000),
    ('Qverambitioned',1,1381,3,2,32301,2006,143000),
    ('Unpercussive',3,4242,4,5,32303,2007,569000),
    ('Emasculate',2,2533,3,2,32310,1991,365000),
    ('Lumined',1,158,3,2,32303,1993,155000),
    ('Boobialla',2,2497,4,4,32309, 1990,289000),
    ('Landsmaal',2,4010,5,3,32309,2002,549900);


