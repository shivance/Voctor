import os
import numpy as np
import tensorflow as tf
from django.conf import settings
from pathlib import Path

Tmodel = tf.keras.models.load_model(os.path.join(os.path.join(Path(__file__).resolve().parent,'dataset/'),'xraymodel.h5'))
def predict(img_path):
   img=tf.keras.preprocessing.image.load_img(img_path,target_size=(224,224))
   img =tf.keras.preprocessing.image.img_to_array(img)
   img = img[np.newaxis,:]
   a = Tmodel.predict(img)
   return max(a[0])

if __name__ == '__main__':
    print('Output : ',predict('../media/X-ray.jpg'))