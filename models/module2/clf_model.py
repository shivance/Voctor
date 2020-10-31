import numpy as np
import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import VGG16
from tensorflow.keras.layers import MaxPooling2D, Dropout, Flatten
from tensorflow.keras.models import models
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer

trn_dtgn = ImageDataGenerator(
    rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)

trn_gnrtr = trn_dtgn.flow_from_directory('')
