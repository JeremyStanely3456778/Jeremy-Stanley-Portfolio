#Jeremy Stanley

#Using Keras/CNN and numpy with python for image classification on skin tissue jpegs to detect whether an inputed image contains
# canverous tissue or not. The test and trainig data is divided into images of cancerous tissue(mishapen black moles or other skin growth, etc...) and 
# healthy tissue(light brown moles, pimples, freckles, etc..). The source of the dataset will taken from academic-medical image databases.  

#Created on November 15, 2018

#Import Packages from keras packages 
from keras.models import Sequential
from Keras.layers import Conv2D
from Keras.layers import Maxpooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Dropout
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
import numpy as np

# Implement CNN classifier
CNN_classifier = Sequential()

#input layer
CNN_classifier.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))

#2D convolutional layer
CNN_classifier.add(Conv2D(16, (5, 5), activation = 'relu'))

#set up first maxpooling for model
CNN_classifier.add(Maxpooling2D(pool_size = (2, 2)))

#2D convolutional layer for model
CNN_classifier.add(Conv2D(32, (3, 3), activation = 'relu'))

#2D convolutional layer for model
CNN_classifier.add(Conv2D(64, (3, 3), activation = 'relu'))

#2D convolutional layer for model
CNN_classifier.add(Conv2D(128, (2, 2), activation = 'relu'))

#setup second maxpooling for model
CNN_classifier.add(Maxpooling2D(pool_size = (2, 2)))

#iniate flattening
CNN_classifier.add(Flatten())

#First Fully connected layer of the Model
CNN_classifier.add(Dense(units = 512, activation = 'relu'))

#Dropout layer
CNN_classifier.add(Dropout(0.2))

# Second Fully connected layer of the Model
CNN_classifier.add(Dense(units = 1, activation = 'sigmoid')) # be tried with softmax activation function

#compile the CNN_classifier
CNN_classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

#fitting images to CNN_classifier
data_generator_training = ImageDataGenerator(rescale = 1./255, shear_range = 0.2, zoom_range = 0.2, horizontal_flip = True)

data_generator_test = ImageDataGenerator(rescale = 1./255)

training_data_set = data_generator_training.flow_from_directory('dataset/training_set', target = (64, 64), batch_size = 32, class_mode = 'binary')

test_data_set = data_generator_test.flow_from_directory('dataset/test_set', target_size = (64, 64), batch_size = 32, class_mode = 'binary')

CNN_classifier.fit_generator(training_data_set, steps_per_epoch = 100000, epochs = 60, validation_data = test_data_set, validation_steps = 50000)

# Making new predictions from model
inputed_test_image = image.load_img('dataset/single_prediction/cancerous_or_non_cancerous.jpg', target_size = (64, 64))

inputed_test_image = image.img_to_array(inputed_test_image)

inputed_test_image = np.expand_dims(inputed_test_image, axis = 0)

Result = CNN_classifier.predict(inputed_test_image)

training_data_set.class_indices
if Result[0][0] == 1:
    prediction = 'Positive' #if one is returned than image is positive for skin cancer
else:
    prediction = 'Negative' #if zero is returned than image negative for skin cancer
    
#Display result to console
print("The result is:" + Result + prediction)   
    