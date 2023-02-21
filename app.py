from flask import Flask, render_template, request
import tensorflow as tf
import os

from utils import predict_with_model

model = tf.keras.models.load_model("Saved_Model")

app = Flask(__name__)

Image_store = "Data"
app.config['UPLOAD_FOLDER'] = Image_store

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            image_file = request.files['image']
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
            image_file.save(image_path)

            prediction = predict_with_model(model, image_path)

            for filename in os.listdir(Image_store):
                file_path = os.path.join(Image_store, filename)
                os.remove(file_path)

        except Exception as error:
            prediction = "Please Upload a Image and Try Again"

        return render_template('index.html', prediction_text='{}'.format(prediction))

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)