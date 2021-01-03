from keras.models import model_from_json
from data_processing import test_set, training_set
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report

json_file = open("model-bw.json", "r")
model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(model_json)
loaded_model.load_weights("model-bw.h5")

A = test_set.labels
print(A.shape)

Y = loaded_model.predict_generator(test_set)
y = np.argmax(Y, axis =1)

print(y.shape)

print(classification_report(A, y))

print(confusion_matrix(A,y))