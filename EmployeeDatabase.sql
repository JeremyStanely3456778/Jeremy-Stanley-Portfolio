#---------------Begining of File-----------------------
#Jeremy Stanley
# Stores employee related data  for use by managers and HR personnel for small commercial retail store.

CREATE DATABASE EmployeeDatabase;

USE EmployeeDatabase;

#-- Creating Tables

CREATE TABLE Employee
(
EmployeeKey nchar(10)   not null,

primary key (EmployeeKey),

PositionKey nchar(10)   not null,

HiredKey nchar(10) not null,

LocationKey nchar(10)   not null,

FirstName nvarchar(50) not null,

LastName nvarchar(50) not null,

PhoneNumber nvarchar(12) not null,

EmailAddress nvarchar(50),

SocialSecurityNumber nvarchar(12) not null,

DriversLicenseNumber nvarchar(20) not null

);


CREATE TABLE Hired
(
HiredKey nchar(10)  not null,

primary key (HiredKey),

EmployeeKey nchar(10) not null,

HireDate Date not null


);

CREATE TABLE Positions
(
PositionKey nchar(10) not null,

primary key (PositionKey),

PositionTitle nvarchar(50) not null


);

CREATE TABLE LeftCompany
(
LeftCompany nchar(10) not null,

primary key (LeftCompany),

 EmployeeKey nchar(10) not null,

DateLeft Date not null,

ReasonCode nchar(10)

);

CREATE TABLE PositionHistory
(
 PositionHistoryKey nchar(10) not null,
 
 primary key (PositionHistoryKey),
 
EmployeeKey nchar(10) not null,

StartDate Date not null,

EndDate Date not null

);

CREATE TABLE Location
(
LocationKey nchar(10) not null,

primary key (LocationKey),

CountryKey nchar(10) not null,

RegionKey nchar(10) not null,

StreetName nvarchar (50) not null,

HomeApartNumber nvarchar(3) not null,

ZipCode nvarchar(5) not null,

City nvarchar(50) not null

);

CREATE TABLE StateRegion
(
StateRegionKey nchar(10) not null,

primary key (StateRegionKey),


StateRegionName nvarchar(50) not null

);



CREATE TABLE Country
(
CountryKey nchar(10) not null,

primary key (CountryKey),

CountryName  nvarchar(50) not null

);


CREATE TABLE DisiplinaryAction
(
DisciplinaryActionKey nchar(10) not null,

primary key (DisciplinaryActionKey),

EmployeeKey nchar(10) not null,

OccurenceCodeKey nchar(10) not null,

ActionCodeKey nchar(10) not null,

DisaplineDate Date not null,

CommentsOnDisapline nvarchar(50) 

);

CREATE TABLE EmployeeCommendation
(
CommendationCode nchar(10) not null,

EmployeeKey nchar(10) not null,

DateReceived nchar(10) not null,

primary key (DateReceived),

CommendationNotes nvarchar(50) 

);

CREATE TABLE TrainingProgram
(
TrainingProgramKey nchar(10) not null,

primary key (TrainingProgramKey),

TrainingName  nvarchar(50) not null

);


CREATE TABLE EmployeeTraining
(
EmployeeTrainingKey nchar(10) not null,

primary key (EmployeeTrainingKey),

EmployeeKey nchar(10) not null,

TrainingProgramKey nchar(10) not null,

StartDate Date not null,

EndDate Date not null,

PerformanceNotes nvarchar(50)

);

CREATE TABLE CommendationCode
(
CommendationCode nchar(10) not null,

primary key (CommendationCode),

CommendationDescription nvarchar(50) not null

);


CREATE TABLE ReasonCode
(
ReasonCode nchar(10) not null,

primary key (ReasonCode),


ReasonDescription nvarchar(50) not null

);

CREATE TABLE OccurenceCode
(
OccurenceCode nchar(10) not null,

primary key (OccurenceCode),

OccurenceDescription nvarchar(50) not null

);

CREATE TABLE ActionCode
(
ActionCode nchar(10) not null,

primary key (ActionCode),

ActionDescription nvarchar(50) not null

);

#---------------End Of Tables------------------------------

#--------------Populate Tables----------------------------


INSERT INTO Employee VALUES ('5127','1', 'H1', 'L001', 'Mary', 'Blanch', '586-689-7011','marymaximux@hotmail.com' , '34-44-4567', 'F1233456876' );

INSERT INTO Hired VALUES ('H1', '5127', '2018-10-18');

INSERT INTO Positions VALUES ('1', 'Associate');

INSERT INTO LeftCompany VALUES ('1', '7825', '2018-09-08', 'RN');

INSERT INTO PositionHistory VALUES ('P1' ,'7825', '2018-03-08', '2018-09-08');

INSERT INTO Location VALUES ('L001', 'US', 'FL', 'Lawerence ST', '338', '32567', 'Plant City');

INSERT INTO StateRegion VALUES ('FL', 'Florida');

INSERT INTO Country VALUES ('US', 'United States');

INSERT INTO DisiplinaryAction VALUES ('1', '7825', 'CC', 'W', '2018-04-08', null);

INSERT INTO EmployeeCommendation VALUES ('GCS','5127', '2018-11-08', null);

INSERT INTO TrainingProgram VALUES ('1', 'Cashier Training');

INSERT INTO EmployeeTraining VALUES ('1', '5127', '1', '2018-10-08', '2018-08-13', 'did great');

INSERT INTO CommendationCode VALUES ('GCS', 'Great Cusotmer Service');

#tables populated with mutliple rows

INSERT INTO ReasonCode VALUES ('TD', 'Terminated');
INSERT INTO ReasonCode VALUES ('LO', 'Laid Off');
INSERT INTO ReasonCode VALUES ('RN', 'Resigned');

INSERT INTO OccurenceCode VALUES ('CC', 'Customer Complanint');
INSERT INTO OccurenceCode VALUES ('HT', 'High Till');
INSERT INTO OccurenceCode VALUES ('LT', 'Low Till');
INSERT INTO OccurenceCode VALUES ('SLD', 'Store Left in Disarray');
INSERT INTO OccurenceCode VALUES ('SLUS', 'Stone Left Unsecure');

INSERT INTO ActionCode VALUES ('W', 'Warning');
INSERT INTO ActionCode VALUES ('S', 'Suspension');
INSERT INTO ActionCode VALUES ('T', 'Termination');

#--------------------End of Populating-------------------------------

#--------------------End of File----------------------------------------
