Dependencies:

keras, 
tensorflow, 
cv2, 
PIL, 
matplotlib, 
pyttsx3, 
hunspell, 
tkinter, 
matplotlib, 
numpy, 
scikit-learn

unzip DATA.zip for the dataset and copy the files to the main directory
Files and methods:

digital_image_processing.py: compares Canny Edge with Custom Algorithm
1. func(path)

activeScreen.py: create a screen where user can place its hand
1. def makeScreen(img): 

src/UI.py: creates the user interface
class Application:
1. def GUI(self): 
2. def setGUI(self):
3. def makeElements(self):
4. def placeElements(self):
5. def load_model(self, ext):
6. def __init__(self):
7. def Buttons(self,i):
8. def video_loop(self):
9. def DRU(self,K):
10. def TKDI(self, K):
11. def SMN(self, K):
12. def Layer2(self, K):
13. def predict(self,test_image):
14. def display(self):
15. def speak(self):
16. def action1(self):
17. def action2(self):
18. def action3(self):
19. def destructor(self):

src/run.py: run in the GUI program

data_processing.py: uses keras.preprocessing.ImageDataGenerator
creates training_set, test_set for training and validation
test_datagen = ImageDataGenerator(rescale=1./255)
training_set = train_datagen.flow_from_directory('train/',
                                                 target_size=(128, 128),
                                                 batch_size=10,
                                                 color_mode='grayscale',
                                                 class_mode='categorical')

evaluation_metrics.py: returns classification report(F1, precision, recall, support) and confusion matrix

model.py: CNN model made using keras
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
