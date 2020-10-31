# This files contains all utility functions used in bot.py

import random
from senti import sentiment

def welcome():
    greet_msg = ['Good Day','Hey','Hola','Hello','Ogin-ki-deska']
    inquires = [
        "How's it going?",
        "How are you doing?",
        "How are you feeling today?",
        "How are you feeling?",
        "How are you?",
        "How are you doing today?",
        "How is your day going?",
        "How have you been?",
        "How have you been feeling?",
        "How have you been today?",
        "How have you been feeling today?",
        "Are you tasting food you eat ?",
        "Are you sleeping more or less than you normally do?".
        "Do you feel tired no more how you sleep ?",
        "Are you capable of enjoying things right now ?",
        "Is it hard for you to do personal grooming ?",
        "Are you having thoughts of your own death ?",
        "Are you having physical symptoms like headache , insomnia or digestive issues ? "
        "Are you eating more or less than you normally do?",
        "Are you exercising daily ?".
    ]