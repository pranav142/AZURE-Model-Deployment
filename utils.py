import tensorflow as tf
import numpy as np


def predict_with_model(model, img_path):

    Disease_Mapping = {
        0: "melanoma",
        1: "melanocytic nevi",
        2: "basal cell carcinoma",
        3: "Actinic keratoses",
        4: "benign keratosis",
        5: "dermatofibroma",
        6: "vascular lesions", 
    }          

    img = tf.io.read_file(img_path)
    img = tf.image.decode_png(img, channels = 3)
    img = tf.image.convert_image_dtype(img, dtype=tf.float32)
    img = tf.image.resize(img, [100,100])
    img = tf.expand_dims(img, axis=0) 

    prediction = model.predict(img)
    print(prediction)
    prediction = np.argmax(prediction)

    prediction = Disease_Mapping[prediction]
    print(f"Prediction = {prediction}")
    return prediction