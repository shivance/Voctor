from random import random
from utils import *
from senti import sentiment


def start_session():
    wlcm_txt = welcome()
    #bot asks question user will respond 
    s = str(input())
    welcom_re = respond()
    
    if (welcom_re.lower()=="yepp"):
        continue_session()
    else:
        print("Terminating chatbot because of inactive user in 3..2..1..")

c_neg = 0
c_pos = 0
c_neu = 0

def continue_session():
    for i in range(7):
        normal_Que()
        reply = str(input())
        if (sentiment(reply)==-1)
            c_neg+=1
        elif (sentiment(reply)==0)
            c_neu+=1
        else:
            c_pos+=1
    
    if (c_neg>=4):
        li8_depr()
    else:
        print("Okay ! you seem to be fine ... Focus on your work , okay ? Sleep properly and Take rest properly..Bye ,,")