!pip install -q t5
import tensorflow.compat.v1 as tf
import tensorflow_datasets as tfds
import t5
import functools
import os
import time
import warnings
from contextlib import contextmanager
import logging as py_logging


BASE_DIR = ".//closed_book"
DATA_DIR = os.path.join(BASE_DIR, "data")
MODEL_DIR = "./"


tf.disable_v2_behavior()

def tf_verbosity_level(level):
  og_level = tf.logging.get_verbosity()
  tf.logging.set_verbosity(level)
  yield
  tf.logging.set_verbosity(og_level)