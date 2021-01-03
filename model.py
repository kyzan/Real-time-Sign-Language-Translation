from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D, Flatten, Dense, Dropout
from keras import optimizers

#model 1

# classifier = Sequential()
# classifier.add(Convolution2D(32, (3, 3), input_shape=(128, 128, 1), activation='relu'))
# classifier.add(MaxPooling2D(pool_size=(2, 2)))
# classifier.add(Convolution2D(32, (3, 3), activation='relu'))
# classifier.add(MaxPooling2D(pool_size=(2, 2)))
# classifier.add(Flatten())
# classifier.add(Dense(units=128, activation='relu'))
# classifier.add(Dropout(0.40))
# classifier.add(Dense(units=96, activation='relu'))
# classifier.add(Dropout(0.40))
# classifier.add(Dense(units=64, activation='relu'))
# classifier.add(Dense(units=27, activation='softmax')) 
# classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
# classifier.summary()

#model 2 = model_final

classifier = Sequential()
classifier.add(Convolution2D(16, (2,2), input_shape=(128, 128, 1), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding='same'))
classifier.add(Convolution2D(32, (3,3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(3, 3), strides=(3, 3), padding='same'))
classifier.add(Convolution2D(64, (5,5), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(5, 5), strides=(5, 5), padding='same'))
classifier.add(Flatten())
classifier.add(Dense(128, activation='relu'))
classifier.add(Dropout(0.2))
classifier.add(Dense(27, activation='softmax'))
sgd = optimizers.SGD(lr=1e-2)
classifier.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

#model 3 = model

# classifier = Sequential()
# classifier.add(Convolution2D(32, (3,3), input_shape=(128,128,1), activation='relu'))
# classifier.add(MaxPooling2D(pool_size=(2,2)))
# classifier.add(Convolution2D(64, (3,3), activation='relu'))
# classifier.add(Convolution2D(64, (3,3), activation='relu'))
# classifier.add(MaxPooling2D(pool_size=(2,2)))
# classifier.add(Convolution2D(128, (3,3), activation='relu'))
# classifier.add(MaxPooling2D(pool_size=(2,2)))
# classifier.add(Convolution2D(128, (3,3), activation='relu'))
# classifier.add(MaxPooling2D(pool_size=(2,2)))
# classifier.add(Flatten())
# classifier.add(Dense(150, activation='relu'))
# classifier.add(Dropout(0.25))
# classifier.add(Dense(27, activation='softmax'))
# classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

classifier.summary()

from keras.utils import plot_model
plot_model(classifier, to_file="classifier.png", show_shapes=True)