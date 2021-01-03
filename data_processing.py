from keras.preprocessing.image import ImageDataGenerator

#processed datasets for train, test, DRU, TKDI, SMN
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory('train/',
                                                 target_size=(128, 128),
                                                 batch_size=10,
                                                 color_mode='grayscale',
                                                 class_mode='categorical')

print(training_set.class_indices)

test_set = test_datagen.flow_from_directory('test/',
                                            target_size=(128 , 128),
                                            batch_size=10,
                                            color_mode='grayscale',
                                            class_mode='categorical') 

print(test_set.labels)

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_setDRU = train_datagen.flow_from_directory('DRU/',
                                                 target_size=(128, 128),
                                                 batch_size=10,
                                                 color_mode='grayscale',
                                                 class_mode='categorical')

print(training_setDRU.class_indices)

test_setDRU = test_datagen.flow_from_directory('DRU_test/',
                                            target_size=(128 , 128),
                                            batch_size=10,
                                            color_mode='grayscale',
                                            class_mode='categorical') 

print(test_setDRU.class_indices)

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_setSMN = train_datagen.flow_from_directory('SMN/',
                                                 target_size=(128, 128),
                                                 batch_size=10,
                                                 color_mode='grayscale',
                                                 class_mode='categorical')

print(training_setSMN.class_indices)

test_setSMN = test_datagen.flow_from_directory('SMN_test/',
                                            target_size=(128 , 128),
                                            batch_size=10,
                                            color_mode='grayscale',
                                            class_mode='categorical') 

print(test_setSMN.class_indices)

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_setTKDI = train_datagen.flow_from_directory('TKDI/',
                                                 target_size=(128, 128),
                                                 batch_size=10,
                                                 color_mode='grayscale',
                                                 class_mode='categorical')

print(training_setTKDI.class_indices)

test_setTKDI = test_datagen.flow_from_directory('TKDI_test/',
                                            target_size=(128 , 128),
                                            batch_size=10,
                                            color_mode='grayscale',
                                            class_mode='categorical') 

print(test_setTKDI.class_indices)

