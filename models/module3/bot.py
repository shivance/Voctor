from random import random
from utils import *
from senti import sentiment


def start_session():
    wlcm_txt = welcome()
    #bot asks question user will respond 
    welcom_re = respond()