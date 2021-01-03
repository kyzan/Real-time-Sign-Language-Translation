# Importing the Keras libraries and packages
from model import classifier
import matplotlib.pyplot as plt 
from data_processing import training_set, test_set
import os

#datasets https://drive.google.com/file/d/1DQoERO17DOEhEGqqWvva6pTRVGhJdU84/view?usp=sharing

os.environ["CUDA_VISIBLE_DEVICES"] = "1"

history = classifier.fit_generator(
        training_set,
        epochs=5,
        validation_data=test_set)
        
loss, acc = classifier.evaluate_generator(test_set , verbose=1)
print(loss, acc)

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.show()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.show()

model_json = classifier.to_json()
with open("model-bw.json", "w") as json_file:
    json_file.write(model_json)
classifier.save_weights('model-bw.h5')


