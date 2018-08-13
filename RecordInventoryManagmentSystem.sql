
#---------------Beginning of File----------------------------
#Jeremy Stanley

#-- Creating Database
CREATE DATABASE RecordManagmentSystem;



USE RecordManagmentSystem;





#--create tables
CREATE TABLE Customer
(
CustomerKey nchar(10)   not null,

primary key (CustomerKey),

SaleKey nchar(10)  not null,

PurchaseKey nchar(10)   not null,


CustomerFirstName nvarchar(50),

CustomerLastName nvarchar(50),

CustomerPhoneNumber nvarchar(10),

CustomerHouseNumber nvarchar(3),

CustomerStreetName nvarchar(50),

CustomerCity nvarchar(50),

CustomerState nvarchar(50),

CustomerZipCode nvarchar(5),

CustomerEmail nvarchar(50)


);

#--create table 

#stores sales data
CREATE TABLE Sale
(
Salekey nchar(10)   not null,

primary key (SaleKey),

AlbumKey nchar(10)   not null,


CustomerKey nchar(10)   not null,

SaleDate Date not null,

SaleTax decimal(10,2) not null,

SaleTotal decimal(10,2) not null

);

#stores transactions data
CREATE TABLE Transactions
(
TransactionsKey nchar(10)   not null,

primary key (TransactionsKey),

CustomerKey nchar(10)   not null

);

# stores customer requests for records
CREATE TABLE Request
(
Requestkey nchar(10)   not null,

primary key (RequestKey),

AlbumKey nchar(10)   not null,

CustomerKey nchar(10)   not null,


RequestDate Date not null
);

#stores data on albums owned by Vince Vinyls
CREATE TABLE Album
(
AlbumKey nchar(10)   not null,

primary key (AlbumKey),

InventoryKey nchar(10)   not null,

PurchaseKey nchar(10)   not null,

RequestKey nchar(10)   not null,


AlbumName nvarchar(50) not null,

AlbumReleaseDate Date not null,

AlbumQuantity int not null, 

ConditionOfVinyl nvarchar(10) not null,

ConditionOfCaseSleeve nvarchar(10)not null

);

#contains inventory of all records
CREATE TABLE Inventory
(
InventoryKey nchar(10)   not null,

primary key (InventoryKey),

AlbumKey nchar(10)   not null,

PurchaseKey nchar(10)   not null,

SaleKey nchar(10)   not null

);

#stores price for all albums
CREATE TABLE SellAlbum
(
AlbumKey nchar(10)   not null,

primary key (AlbumKey),

Cost_To_Sell decimal(10,2) not null

);

#stores data on how much albums were bought for
CREATE TABLE BuyAlbum
(
AlbumKey nchar(10)   not null,

primary key (AlbumKey),

Cost_To_Buy decimal(10,2) not null

);

#contains data on artists of albums
CREATE TABLE Artist
(
AlbumKey nchar(10)   not null,

primary key (AlbumKey),

ArtistName nvarchar(50) not null

);

#record of purchases
CREATE TABLE Purchase
(
PurchaseKey nchar(10)   not null,

primary key (PurchaseKey),

TransactionsKey nchar(10)   not null,

AlbumKey nchar(10)   not null,

CustomerKey nchar(10)   not null,

PurchaseDate Date not null,

PurchaseTotal decimal(10,2) not null

);

#populate Customers table

INSERT INTO Customer VALUES ('A879','A229','E500'  ,'Jeremy', 'Stanley', 3863658967, 123, 'Willord Street', 'Lake City' , 'FL', 32024, 'jeremy.stanley85@gmail.com');

#popualte sale table

INSERT INTO Sale VALUES ('A229', 'B391', 'A879'  ,'2018-05-12', 20.00, 500.98);

#populate transaction table

INSERT INTO Transactions VALUES ('D333', 'A879');

#populate request table

INSERT INTO Request  VALUES ('E111', 'B391', 'A879', '2018-09-07');

#populate Album table

INSERT INTO Album  VALUES ('B391', 'N303', 'E500', 'E111', 'Rubber Soul', '1975-08-11', 1, 'fair', 'fair');

#popuulate inventory table

INSERT INTO Inventory  VALUES ('N303', 'B391', 'E500', 'A229');

#populate sell album table

INSERT INTO SellAlbum  VALUES ('B391', 500.98);

#populate buyalbum table

INSERT INTO BuyAlbum  VALUES ('B391', 350.49);

#populate arrtist table

INSERT INTO Artist  VALUES ('B391', 'Beatles');

#populate Purchase table

INSERT INTO Purchase  VALUES ('E500', 'D333', 'B391', 'A879', '2018-01-12', 500.98);

#------------------------End of File-------------------------------
