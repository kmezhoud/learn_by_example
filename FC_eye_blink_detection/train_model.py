import os
import cv2
from PIL import Image
import numpy as np
from skimage.transform import resize

from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import AveragePooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.models import model_from_json
from keras.preprocessing.image import ImageDataGenerator
os.environ['KMP_DUPLICATE_LIB_OK']='True'

#from scipy.ndimage import imread
#from scipy.misc import imresize, imsave
#from imageio import imread

IMG_SIZE = 24

def collect():
	train_datagen = ImageDataGenerator(
			rescale=1./255,
			shear_range=0.2,
			horizontal_flip=True, 
		)

	val_datagen = ImageDataGenerator(
			rescale=1./255,
			shear_range=0.2,
			horizontal_flip=True,		)

	train_generator = train_datagen.flow_from_directory(
	    directory="dataset/train",
	    target_size=(IMG_SIZE, IMG_SIZE),
	    color_mode="grayscale",
	    batch_size=32,
	    class_mode="binary",
	    shuffle=True,
	    seed=42
	)

	val_generator = val_datagen.flow_from_directory(
	    directory="dataset/val",
	    target_size=(IMG_SIZE, IMG_SIZE),
	    color_mode="grayscale",
	    batch_size=32,
	    class_mode="binary",
	    shuffle=True,
	    seed=42
	)
	return train_generator, val_generator

def save_model(model):
	model_json = model.to_json()
	with open("model.json", "w") as json_file:
		json_file.write(model_json)
	# serialize weights to HDF5
	model.save_weights("model.h5")
	
def train(train_generator, val_generator):
	STEP_SIZE_TRAIN=train_generator.n//train_generator.batch_size
	STEP_SIZE_VALID=val_generator.n//val_generator.batch_size

	print('[LOG] Intialize Neural Network')
	
	model = Sequential()

	model.add(Conv2D(filters=6, kernel_size=(3, 3), activation='relu', input_shape=(IMG_SIZE,IMG_SIZE,1)))
	model.add(AveragePooling2D())

	model.add(Conv2D(filters=16, kernel_size=(3, 3), activation='relu'))
	model.add(AveragePooling2D())

	model.add(Flatten())

	model.add(Dense(units=120, activation='relu'))

	model.add(Dense(units=84, activation='relu'))

	model.add(Dense(units=1, activation = 'sigmoid'))


	model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

	model.fit_generator(generator=train_generator,
	                    steps_per_epoch=STEP_SIZE_TRAIN,
	                    validation_data=val_generator,
	                    validation_steps=STEP_SIZE_VALID,
	                    epochs=20
	)
	save_model(model)

dataset = collect()
train(dataset[0], dataset[1])
