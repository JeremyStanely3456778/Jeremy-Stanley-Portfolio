#---------------Begining of File-----------------------
#Jeremy Stanley
# Stores payroll related data  for use by managers and HR personnel to track hours, pay, and dispursement.

CREATE DATABASE PayrollDatabase;

USE PayrollDatabase;

#-- Creating Tables

CREATE TABLE ShiftSchedule
(
ShiftScheduleKey nchar(10) not null,

primary key (ShiftScheduleKey),

EmployeeKey nchar(10) not null,

ShiftStatusKey nchar(10) not null,

PayPeriodKey nchar(10) not null,

ShiftDate Date not null,

ShiftStartTime nvarchar(10) not null,

ShiftStartAMPM nvarchar(10) not null,


ShiftEndTime nvarchar(10) not null,

ShiftEndAMPM nvarchar(10) not null,

MealBreakStartTime nvarchar(10) not null,

MealBreakStartAMPM nvarchar(10) not null,

MealBreakEndTime nvarchar(10) not null,

MealBreakEndAMPM nvarchar(10) not null

);

CREATE TABLE Attendance
(
AttendanceKey nchar(10) not null,

primary key (AttendanceKey),


ShiftScheduleKey nchar(10) not null,

EmployeeKey nchar(10) not null,


ClockIn DATETIME not null,

ClockOut DATETIME not null,

MealClockOut DATETIME not null,

MealClockIn DATETIME not null
);

CREATE TABLE CancelShift 
(
CanceledShiftKey  nchar(10) not null,

primary key (CanceledShiftKey),


ShiftScheduleKey nchar(10) not null,

ShiftStatusKey nchar(10) not null,

ReasonForCancel nvarchar(50)
);

CREATE TABLE ShiftChange
(
ShiftChangeKey nchar(10),

primary key (ShiftChangeKey),

 
EmployeeKey nchar(10),
 
ShiftScheduleKey nchar(10),
 
DateSwitched Date,
 
ReasonForSwitch nvarchar(50)
);

CREATE TABLE Compensation
(
CompensationKey  nchar(10) not null,

primary key (CompensationKey),


EmployeeKey nchar(10) not null,

PayRateKey nchar(10) not null,

CompensationAmount float not null

);

CREATE TABLE PayPeriod
(
PayPeriodKey nchar(10) not null,

primary key (PayPeriodKey),


EmployeeKey nchar(10) not null,

ShiftScheduleKey nchar(10) not null,

PeriodStart Date not null,

PeriodEnd Date not null

);

CREATE TABLE PayRaise
(
PayRaiseKey nchar(10), 

primary key (PayRaiseKey),


EmployeeKey nchar(10), 

CompensationKey nchar(10),

RaiseAmount decimal (9),

BeginDate Date 

);

CREATE TABLE StaffPTO
(
PTOKey nchar(10) not null,

primary key (PTOKey),


EmployeeKey nchar(10) not null,

PTOStartDate Date not null,

PTOEndDate Date not null,

PTONumber int not null

);

CREATE TABLE EmployeeHours
(
HoursKey nchar(10) not null,

primary key (HoursKey),


EmployeeKey nchar(10) not null,

AttendanceKey nchar(10) not null,

TotalHours float not null

);

CREATE TABLE NetPay
(
NetPayKey nchar(10) not null,

primary key (NetPayKey),


EmployeeKey nchar(10) not null,

GrossPayKey nchar(10) not null,

DeductionsKey nchar(10) not null,

NetPay float not null,

YTDNetPay float not null

);

CREATE TABLE Deductions
(
DeductionsKey nchar(10) not null,

primary key (DeductionsKey),


EmployeeKey nchar(10) not null,

PayPeriodKey nchar(10) not null,


FedTax float not null,

YTDFedTax float not null,

SocSecTax float not null,

YTDSocSecTax float not null,

WorkComp float not null,

YTDWorkComp float not null,

MedicareTax float not null,

YTDMedicareTax float not null,

StateTax float not null,

YTDStateTax float not null,

LocalTax float not null,

YTDLocalTax float not null

);

CREATE TABLE GrossPay
(
GrossPayKey nchar(10) not null,

primary key (GrossPayKey),


EmployeeKey nchar(10) not null,

HoursKey nchar(10) not null,

PayPeriodKey nchar(10) not null,

GrossPay float not null,

YTDGrossPay float not null

);

CREATE TABLE DisbursementType
(
DispursementTypeKey nchar(10) not null,

primary key (DispursementTypeKey),


DispursementType  nvarchar(50) not null

);

CREATE TABLE ShiftStatus
(
ShiftStatusKey nchar(10) not null,

primary key (ShiftStatusKey),


StatusDescription nvarchar(50) not null

);

CREATE TABLE PayRate
(
PayRateKey nchar(10) not null,

primary key (PayRateKey),


PayRateDescription nvarchar(50) not null

);

CREATE TABLE Disbursement
(
DispursementKey nchar(10) not null,

primary key (DispursementKey),


EmployeeKey nchar(10) not null,

DispursementTypeKey nchar(10) not null,

DedeuctionsKey nchar(10) not null,

HoursKey nchar(10) not null,

PayPeriodKey nchar(10) not null,

NetPayKey nchar(10) not null,

GrossPay nchar(10) not null,

CompensationKey nchar(10) not null,

PTOKey nchar(10) not null,


CheckDate Date not null,

CheckNumber int, 

DirectDepositNumber int
);

CREATE TABLE UsedPTO
(
UsedPTOKey nchar(10) not null,

primary key (UsedPTOKey),


EmployeeKey nchar(10) not null,

PTOKey nchar(10) not null,

ShiftKey nchar(10) not null,

ReasonForPTO nchar(50)

);

#-------------End of Tables-----------------------

#-------------Populate Tables--------------------

INSERT INTO ShiftSchedule VALUES ('SHO1', '5127',  'A' ,'PP1' , '2018-11-18', '8:00 ', 'AM', '3:30', 'PM', '12:15', 'PM', '12:45', 'PM');

INSERT INTO Attendance  VALUES ('A1', 'SHO1', '5125', '2018-08-11 20:05:31', '2018-08-11 15:35:41', '2018-08-11 12:20:41', '2018-08-11 13:00:13');

INSERT INTO CancelShift VALUES ('C01', 'SHO2', 'C', 'Quit');

#INSERT INTO ShiftChange VALUES ( null, null, null, null, null); # kept all null 

INSERT INTO Compensation VALUES ('COMP1', '5125','Hourly', '9.25'); 

INSERT INTO ShiftStatus VALUES ('C', 'Canceled'); 

INSERT INTO ShiftStatus VALUES ('A', 'Active'); 

INSERT INTO PayRate VALUES ('SAL', 'Salary'); 

INSERT INTO PayRate VALUES ('HR', 'Hourly'); 

INSERT INTO PayPeriod VALUES ('PP1', '5125', 'SHO1', '2018-08-10', '2018-08-17'); 

INSERT INTO StaffPTO VALUES ('PTO1', '5125', '2018-08-10', '2019-01-01', '5'); 

INSERT INTO EmployeeHours VALUES ('H1', '5125', 'A1', '9.30'); 

INSERT INTO GrossPay VALUES ('GP1', '5125', 'PP1', 'H1', 76.62, 76.62); 

INSERT INTO Deductions VALUES ('D1', '5125', 'PP1', '3.00', '3.00', '1.00', '1.00', '1.00', '1.00', '2.00', '2.00', '3.00', '3.00', '2.00', '2.00'); 

INSERT INTO NetPay VALUES ('NP1', '5125', 'GP1', 'D1', '61.76', '61.76'); 

INSERT INTO DisbursementType VALUES ('CHK', 'Check' ); 

INSERT INTO DisbursementType VALUES ('DD', 'Direct Deposit' ); 

INSERT INTO Disbursement VALUES ('1', '5125', 'DD', 'D1', 'H1', 'PP1', 'NP1', 'GP1', 'COMP1', 'PTO1', '2018-08-17', null, '876912'); 

INSERT INTO UsedPTO VALUES ('UPTO1', '5125', 'PTO1', 'SHO1', ' family emergency' ); 

# ------------------------End of Table Population--------------------------------

#-------------------------End of File-------------------------------------------------
