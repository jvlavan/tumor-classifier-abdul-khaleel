from django.shortcuts import render
from django.core.files.uploadedfile import InMemoryUploadedFile
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io
import base64

def preprocess_image(file_object):
    img = Image.open(file_object)
    img = img.resize((256, 256))
    img_array = np.array(img)
    img_array = img_array.astype('float32') / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    return img_array

def classify_mri(request):
    if request.method == 'POST':
        # Load the trained model
        model = load_model('model.h5')

        # Preprocess the input images
        uploaded_files = request.FILES.getlist('images')
        predictions = []
        images_data = []

        for uploaded_file in uploaded_files:
            file_object = io.BytesIO(uploaded_file.read())
            array4d = preprocess_image(file_object)

            # Perform prediction using the loaded model
            prediction = model.predict(array4d)
            predicted_class = np.argmax(prediction)

            # Map the predicted class to a label
            labels = ['Glioma', 'Meningioma','No Tumor', 'Pituitary']
            predicted_class_label = labels[predicted_class]

            predictions.append(predicted_class_label)

            # Encode the image as base64
            imag_data = base64.b64encode(file_object.getvalue()).decode('utf-8')
            images_data.append(imag_data)

        # Pass the prediction results and image data to the template
        context = {'predictions_images': zip(predictions, images_data)}

        return render(request, 'result.html', context)

    else:
        return render(request, 'classify_mri.html')
