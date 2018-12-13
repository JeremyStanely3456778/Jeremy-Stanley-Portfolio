#Jeremy Stanley
# EDA on Macro.csv
# 09-24-2018
#Puprose is to attempt to find insights within data set in relation to nations's GDP
# witin a time period, etc. Using SciKit learning, pandas, matplotlib, with Mac OS and Ipython. 

# read in csv file 
import pandas as pd

GDP = pd.read_csv('/Users/JeremyStanley/Documents/Python_Data_Science/CSV data/macro.csv')

# Gain an Overview of data

print(GDP.head())

print(GDP.columns)

#print (GDP.shape)

#editing column names 

GDP.columns = ['Unnamed: 0', 'country', 'year', 'grossdomesticproduct', 'unemployment', 'capitalmobility', 'trade']

print(GDP.capitalmobility)

#check datatypes
print(GDP.dtypes)

#checking for missing/null datatypes
print(GDP.info())

# this is the code you use if you want to drop all nulls
#degrees = degrees.dropna()

# Graphical Analysis using matplotlib---------------------------------------------------------------------------->
import matplotlib.pyplot as plt
import numpy as np
#x and y values 
trade = GDP['trade']
year = GDP['year']

ax = plt.subplot()

#barchart 
plt.bar(year, trade)
plt.show()

#histogram for trade column
plt.hist(trade)
plt.show()

#histogram for unemployment column
unemployment = GDP['unemployment']

plt.hist(trade)
plt.show()

#scattorplot for trade and year
x = GDP['year']
y = GDP['trade']

plt.scatter(x, y)
plt.show()

US = GDP[GDP.country == 'United States']
y = GDP['year']



# new dataframe
USdf= pd.DataFrame(US)
print(USdf)

#scattor plot for USdf

USx = USdf.trade
USy = USdf.year

plt.scatter(USy, USx)
plt.show()


# New datarame for Japan
JAP = GDP[GDP.country == 'Japan']
y = GDP['year']
JAPdf= pd.DataFrame(JAP)

#scattor plot for USdf

JAPx = JAPdf.trade
JAPy = JAPdf.year
JAPunemployment = JAPdf.unemployment

plt.scatter(JAPy, JAPx)
plt.show()

#calculate correlation coefficient
print(np.corrcoef(JAPx, JAPy))

#bargraph of unemployment
plt.bar(JAPy, JAPunemployment)
plt.show()
print(np.corrcoef(JAPx, JAPunemployment))

# Dataframe for italy
ITALY = GDP[GDP.country == 'Italy']
Italydf= pd.DataFrame(ITALY)
print(Italydf)

#scattorplot for trade of italy
Italydfx = Italydf.year
Italydfy = Italydf.trade

plt.scatter(Italydfx, Italydfy)
plt.show()

##calculate correlation coefficient
print(np.corrcoef(Italydfx, Italydfy))


#scattorplot for unemployment italy
Italydf1 = Italydf.year
Italydf2 = Italydf.unemployment

plt.scatter(Italydf1, Italydf2)
plt.show()

##calculate correlation coefficient
print(np.corrcoef(Italydf1, Italydf2))


# Two layer barchart of trade(blue) and unemployment(red) of Italy
plt.bar(Italydfx, Italydfy, color='b')
plt.bar(Italydf1, Italydf2, color='r')
plt.show()


# Two layer scattorplot of trade(blue) and unemployment(red) of Italy
plt.scatter(Italydfx, Italydfy, color='b')
plt.scatter(Italydf1, Italydf2, color='r')
plt.show()

#bar chart capital mobility of japan and gdp trade(red)
JAPx1 = JAPdf.capitalmobility
JAPy2 = JAPdf.year
JAPy3 = JAPdf.grossdomesticproduct
JAPy4 = JAPdf.trade
JAPy5 = JAPdf.unemployment

plt.plot(JAPy2, JAPx1, linewidth=2.0)
plt.plot(JAPy2, JAPy3, linewidth=2.0, color='g')
plt.plot(JAPy2, JAPy4, linewidth=2.0, color='r')
plt.plot(JAPy2, JAPy5, linewidth=2.0, color='black')
plt.title('Japan')
plt.show()

#Italy line plot of gdp (green) and capitalmobility, trade(red)
Italydf3 = Italydf.capitalmobility
Italydf4 = Italydf.grossdomesticproduct
Italydf5 = Italydf.trade
Italydf6 = Italydf.unemployment

plt.plot(Italydf1, Italydf3, linewidth=2.0)
plt.plot(Italydf1, Italydf4, linewidth=2.0, color='g')
plt.plot(Italydf1, Italydf5, linewidth=2.0, color='r')
plt.plot(Italydf1, Italydf6, linewidth=2.0, color='black')
plt.title('Italy')
plt.show()


#GDP(red), trade(blue), capitalmobililty(green) lineplot
USx = USdf.trade
USy = USdf.year
USGDP = USdf.grossdomesticproduct
USCM = USdf.capitalmobility
USunemployment = USdf.unemployment

plt.plot(USy, USx, color= 'r')
plt.plot(USy, USGDP, color='g')
plt.plot(USy, USCM, color='b')
plt.plot(USy, USunemployment, color='black')
plt.title('United States')
plt.show() 

# Dataframe for west germany
WestGermany = GDP[GDP.country == 'West Germany']
WestGermanydf= pd.DataFrame(WestGermany)
print(WestGermanydf)



#trade, gdp, capital mobility line plot
WGgdp =  WestGermanydf.grossdomesticproduct
WGtrade = WestGermanydf.trade
WGCM = WestGermanydf.capitalmobility
WGyear = WestGermanydf.year
WGunemployment = WestGermanydf.unemployment

plt.plot(WGyear, WGtrade, color='r')
plt.plot(WGyear, WGCM, color='b')
plt.plot(WGyear, WGgdp, color='g')
plt.plot(WGyear, WGunemployment, color='black')
plt.title('West Germany')
plt.show()

print(USy)

#-----------------------------Regression Model for each country--------------------------->

#Regression Analysis for US


import numpy as np
from sklearn import linear_model

# initilizse regression model
reg = linear_model.LinearRegression()

#reshape arrays and create variables for model
x = JAPdf.year.values
y = JAPdf.capitalmobility.values

y = y.reshape(-1,1)
x = x.reshape(-1,1)

#fit the model to the data
reg.fit(x, y)

prediction_space = np.linspace(min(x), max(x)).reshape(-1,1)

#plot data points
plt.scatter(x, y, color='blue')


#places prediction line onto scattor plot 
plt.plot(prediction_space, reg.predict(prediction_space), color='red', linewidth=3)
plt.xlabel('years')
plt.ylabel('trade')
plt.title('Japan trade between 1965 -90')
plt.show()

# Ridge Resgression Model for US data 

from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split

#split training data
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state=42)

# ridge model
ridge = Ridge(alpha=0.2, normalize=True)

#fit training data to model
ridge.fit(X_train, y_train)

ridge_pred = ridge.predict(X_test)

#display resultss
print(ridge.score(X_test, y_test))

# Ridge CV for ridge analysis results

from sklearn.linear_model import RidgeCV

clf = RidgeCV(alphas=[0.2, 0.2, 0.5]).fit(x, y)

print(clf.score(x, y)) 

