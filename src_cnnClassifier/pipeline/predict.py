import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing import image
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
import os



class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename


    
    def predict(self):
        # load model
        model = load_model(os.path.join("artifacts","training", "model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'Coccidiosis'
            return [{ "image" : prediction}]
        elif result[0] == 2:
            prediction = 'Cat'
            return [{ "image" : prediction}]
        elif result[0] == 3:
            prediction =  'Healthy Chick'
            return [{"image" : prediction}]
        elif result[0] == 4:
            prediction = 'Dog'
            result [{"image": prediction}]
