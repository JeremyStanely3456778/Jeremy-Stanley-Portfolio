#Jeremy Stanley
#Using Pandas, Keras, Numpy build RNN/ Long Term Short Term Model for Time Series Analysis
# of Sales data.
#Created on Wed Oct 31 16:14:02 2018


#import software packages
from pandas import DataFrame
from pandas import Series
from pandas import concat
from pandas import read_csv
from pandas import datetime
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from math import sqrt
from matplotlib import pyplot
import numpy

# date-time parsing function for loading the dataset
def parser(timedata):
    return datetime.strptime('190' + timedata, '%Y-%m')

# frome a sequence as a supervised learning problem
def timesseriesdata_to_supervised(data, lag = 1):
    dataframe = DataFrame(data)
    columns = [dataframe.shift(i) for i in range(1,lag + 1)]
    columns.append(dataframe)
    dataframe = concat(columns, axis = 1)
    dataframe.fillna(0, inplace = True)
    return dataframe


# create a differenced series
def difference(dataset, interval = 1):
    DifferenceVariable = list()
    for i in range(interval, len(dataset)):
        datavalue = dataset[i] - dataset[i - interval]
        DifferenceVariable.append(datavalue)
    return Series(DifferenceVariable)
    
# invert differenced values
def inverse_difference(history, yhat, interval = 1):
    return yhat + history[-interval]

# scale train and test data to [-1, 1]
def scale_data(traindata, testdata):
    #fit scaler
    scaler = MinMaxScaler(feature_range = (-1, 1))
    scaler = scaler.fit(traindata)
    #transform train data
    traindata = traindata.reshape(traindata.shape[0], traindata.shape[1])
    traindata_scaled = scaler.transform(traindata)
    #transform test data
    testdata = testdata.reshape(testdata.shape[0], testdata.shape[1])
    testdata_scaled = scaler.transform(testdata)
    return scaler, traindata_scaled, testdata_scaled
       
#inverse scaling of the data  for forcasted value
def invert_scale(scaler, X, value):
    new_row = [timedata for timedata in X] + [value]
    array = numpy.array(new_row)
    array = array.reshape(1, len(array))
    inverted = scaler.inverse_transform(array)
    return inverted[0, -1]

# fit an LSTM nueral network to training data
def fit_LSTM_Network(train, batch_size, nb_epoch, nuerons):
    X, y = train[:, 0:-1], train[:, -1]
    X = X.reshape(X.shape[0], 1, X.shape[1])
    RNNLSTM_model = Sequential()
    RNNLSTM_model.add(LSTM(nuerons, batch_input_shape = (batch_size, X.shape[1], X.shape[2]), stateful = False))
    RNNLSTM_model.add(Dense(1))
    RNNLSTM_model.compile(loss = 'mean_squared_error', optimizer = 'adam')
    for i in range(nb_epoch):
        RNNLSTM_model.fit(X, y, epochs = 1, batch_size = batch_size, verbose = 0, shuffle = False)
        RNNLSTM_model.reset_states()
    return RNNLSTM_model
    
# create a one step forecast
def forecast_LSTM_Model(RNNLSTM_model, batch_size, X):
    X = X.reshape(1, 1, len(X))
    yhat = RNNLSTM_model.predict(X, batch_size = batch_size)
    return yhat[0, 0]
    
 # load data to be analyzed
series = read_csv('/Users/JeremyStanley/Documents/Python_Data_Science/CSV data/shampoo.csv',header = 0, parse_dates = [0], index_col = 0, squeeze = True, date_parser = parser)   

#transform data to be stationary
raw_data_values = series.values
diff_values = difference(raw_data_values, 1)

# transform data to be supervised learning
supervised = timesseriesdata_to_supervised(diff_values, 1)
supervised_values = supervised.values

#split data into train and test-sets
train, test = supervised_values[0:-12], supervised_values[-12:]

#transform data into train and test-data
scaler, traindata_scaled, testdata_scaled = scale_data(train, test)
    

#fit the model
lstm_model = fit_LSTM_Network(traindata_scaled, 1, 1500, 1)
#forecast the entire training dataset to build up state for forecasting
traindata_reshaped = traindata_scaled[:, 0].reshape(len(traindata_scaled), 1, 1)
lstm_model.predict(traindata_reshaped, batch_size = 1)
#walk-forward validation on the test data
predictions = list()
for i in range(len(testdata_scaled)):
    # create 1 step forecast
    X, y = testdata_scaled[i, 0:-1], testdata_scaled[i, -1]
    yhat = forecast_LSTM_Model(lstm_model, 1, X)
    #invert scaling
    yhat = invert_scale(scaler, X, yhat)
    #invert differencing
    yhat = inverse_difference(raw_data_values, yhat, len(testdata_scaled) + 1 - i)
    #store the forcast data
    predictions.append(yhat)
    #display performance of built model
    
    #store forecast
    expected = raw_data_values[len(train) + i + 1]
    print('Month = %d, Predicted = %f, Expected = %f' % (i + 1, yhat, expected))
    
    
#report performance
rmse = sqrt(mean_squared_error(raw_data_values[-12:], predictions))    
print('Test RMSE: %.3f' % rmse)
# line plot of observed vs predicted
pyplot.plot(raw_data_values[-12:])
pyplot.plot(predictions)
pyplot.show()