from random import random
from utils import *
from senti import sentiment
import webbrowser as wb

def start_session():
    print(welcome())
    #bot asks question user will respond 
    s = str(input())
    continue_session()
    
    print("Terminating chatbot because of inactive user in 3..2..1..")

c_neg = 0
c_pos = 0
c_neu = 0

def continue_session():
    phyVsmental()

    for i in range(2):
        normalQue()
        reply = str(input())
        music_enq()
    else:
        print("Okay ! you seem to be fine ... Focus on your work , okay ? Sleep properly and Take rest properly..Bye...")


start_session()