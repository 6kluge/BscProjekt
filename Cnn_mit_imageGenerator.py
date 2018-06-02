
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

# Initialising the CNN
classifier = Sequential()

#Step 1: Convolution
classifier.add(Convolution2D(32,(3,3), input_shape=(64 ,64 ,3),activation="relu"))
#activation function, um negative Werte auszuschließen

#Step 2: Pooling
classifier.add(MaxPooling2D(pool_size=(2,2)))
"""adding a second Convolutional Layer(Optional,sollte aber die Genauigkeit erhöhen)
classifier.add(Convolution2D(64,(3,3),activation="relu"))
classifier.add(MaxPooling2D(pool_size=(2,2)))
"""

#Step 3: Flattening
classifier.add(Flatten())

#Step 4: Full Connection
classifier.add(Dense(units=128, activation="relu"))
#Hier kann man mit der Knotenanzahl experimentieren 
classifier.add(Dense(units=1,activation="sigmoid"))
#Bei binärem output :"Sigmoid"
#Bei kategorien : "Softmax"

#Compiling the CNN
classifier.compile(optimizer= "adam" , loss= "binary_crossentropy", metrics=["accuracy"])
 #Statt "adam" würde auch "SGD" gehen
 #Bei der Bin-Challenge "categorical_crossentropy" benutzen
#Part 2 : Fitting the CNN to the images
from keras.preprocessing.image import ImageDataGenerator
 
train_datagen = ImageDataGenerator(
        rescale=1./255,)
test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(
        'dataset/training_set',
        target_size=(64, 64),
        class_mode='binary')

test_set = test_datagen.flow_from_directory(
        'dataset/test_set',
        target_size=(64, 64),
        class_mode='binary')

classifier.fit_generator(
        training_set,
        steps_per_epoch=8000,
        epochs=3,
        validation_data=test_set,
        validation_steps=2000)

classifier.save("Cnn.h5")

#Neue Prediction
from keras.models import load_model

classifier = load_model("Cnn.h5")

import numpy as np
from keras.preprocessing import image
test_image =image.load_img("dataset/single_prediction/Katze.jpg",target_size=(64,64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image,axis=0)
result = classifier.predict(test_image)
training_set.class_indices

if result[0][0]==1:
    prediction = "Ein Hund"
else:
    prediciton ="Eine Katze"
    
print(prediction)