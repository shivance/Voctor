# This files contains all utility functions used in bot.py

import random
from senti import sentiment
import webbrowser as wb
# front page of whole project will start here


def welcome():
    greet_msg = ['Good Day', 'Hey', 'Hola', 'Hello', 'Ogin-ki-deska']
    inquires = [
        "How's it going?",
        "How are you doing?",
        "How are you feeling today?",
        "How are you feeling?",
        "How are you?",
        "How are you doing today?",
    ]

    wlcm = ((random.choice(greetings)) + " " + (random.choice(inquires)))

    print(wlcm)

    return wlcm

# This function will be responsible for physical vs mental care
# if you get a positive reply then go to physical problems webbie
# else go ahead and execute mental functions below

def phyVsmental():
    ques = ["Are you having physical symptoms like headache , insomnia or digestive issues ? ",
            "Have you caught cold ?",
            "Are you suffering from fever ?",
            "Are you facing any physical difficulty ?"
            ]

    s = str(input())
    print("Reply with Yes or no :) ")
    s = s.lower()
    if (s == "yes")
        print(negativeReply()+" Don't worry ! You've got me ... just hang in there...")
        #redirect to virtual health examiner
        #wb.open("")



def positiveReply():
    ls = ["Great!",
    "Whoa !",
    "Badhiya...",
    "Good to hear !",
    "Wonderful",
    "Awesome."
    "I'm glad to hear that.",
    "Oh happy day !",
    "That's so good to hear !",
    "That is so great !",
    "Waah !"
    ]

    return random.choice(ls)


def neutralReply():
    ls = ["Ohh", "Accha","Hmmm...","Okay ","ok"]
    return random.choice(ls)

def negativeReply():
    ls = ["Take care !",
        "Don't push yourself too hard",
        "Hey ! Hey ! just don't be too careless ... Trust me ! It'll affect you...Life is not about stopping"
        "That's too bad",
        "It's okay ",
        "I'm sorry"
        "That's okay we all have days like that"
        ]
    return random.choice(ls)

def music_res():
    ls = [
        "https://open.spotify.com/playlist/1wHNpiNzLhIMWUw1fl8wI0?si=iqapMTIPT1atrHF3B2edOg",
        "https://open.spotify.com/playlist/4FVHO7ro7mm2NcpHbSYWiH?si=b8lERxPqTnO3hck0wUuY0g",
        "https://open.spotify.com/playlist/5W3MXVdsVNEkAqYYzoAVwt?si=uyssBhcpS4yhK_bcIezW8g",
        "https://open.spotify.com/playlist/27W3WFEhHsrNCrb0y79fPo?si=QZeT9yFuTU2QFr7znLJtQQ",
        "https://open.spotify.com/playlist/6vHhQOHGABPPMcLumvTBpN?si=_3rXqy9dTJGMuxnF9XtLJQ",
        "https://open.spotify.com/playlist/2rN3mSrzUcgjlj1TcEDTX7?si=K9sDp-KPTs-iLLfEqU_kNw",
        "https://open.spotify.com/playlist/4gHPH0i2mD00zgEmWxONn4?si=T2B_CRi7REGjqr-L4ufAtA",
        "https://open.spotify.com/playlist/5Qvz8wZIRYbEUUFoPueKI5?si=Uv7e-zjnTV-AXhuU1YxnzQ"
    ]

    return random.choice(ls)

def music_enq():
    print("Do you like music ?")
    s = str(input())
    if (sentiment(s)>=0)
        print(positiveReply())
        print()
        wb.open(music_res())
    else:
        print(neutralReply())
        print()
        print(normalQue)
        print(positiveReply())
        print()
        relationship()
        dprsnActive()

def relationship():
    print("Are you in relationship ? Yes or no ;) ")
    s = str(input())
    if (s.lower()=="yes")
        print(rel_ls())
        s = str(input())
        if(sentiment(s)<0)
            wb.open(rel_redirect())


def rel_ls():
    ls = [
        "Had trouble in relationship ?",
        "Are you tensed coz of ur partner ?",
        "Are you able to balance your goals along with relationship ?"
    ]
    return (random.choice(ls))

def rel_redirect():
    ls =[
        "https://angrytherapist.medium.com/this-is-what-a-healthy-relationship-looks-like-8b8b2858e7a8",
        "https://medium.com/@antonchevalier/6-healthy-relationship-habits-that-might-surprise-you-ee6b02e94",
        "https://medium.com/@amyjmcdonnell/6-signs-youre-in-a-healthy-relationship-e86b8cd0452b",
        "https://medium.com/@whitneyvmorgan/healthy-relationships-have-these-two-things-a97a49327dd4"
    ]
    return (random.choice(ls))

def normalQue():
    ls = [
        "What do you like to do on weekends?",
        "Had lunch ?"
    ]
    return (random.choice(ls))

def motivate2talk():
    ls = [
        "You can talk don't worry !",
        "It's okay ...tell me !",
        "Don't worry ... talk to me !",
        "What's up ?"
    ]
    return (random.choice(ls))


def dprsnActive():
    
    for i in range(6):
        HdeprQ()
        print()
        print(motivate2talk())
        # best way to cure depression is cure depression is express yourself
        s = str(input())

    print("Hmmm... I get everything now ... I've something for you...")
    wb.open(DeprssionRedirect())


def HdeprQ():
    depr = [
        "How is your day going?",
        "How have you been?",
        "How have you been feeling?",
        "How have you been today?",
        "How have you been feeling today?",
        "Are you tasting food you eat ?",
        "Are you sleeping more or less than you normally do?".
        "Do you feel tired no more how you sleep ?",
        "Are you eating more or less than you normally do?",
        "Are you exercising daily ?".
        "Are you capable of enjoying things right now ?",
        "Is it hard for you to do personal grooming ?",
    ]

    lnk = random.choice(depr)
    return lnk


# a list of links to articles/videos/music/TED talks to cure depression
def DeprssionRedirect():
    res = ["https://www.youtube.com/watch?v=x_LqnfosZgw",
           "https://www.youtube.com/watch?v=wA-DC6Bwric",
            "https://www.youtube.com/watch?v=XCxHsgKY03I",
            "https://www.youtube.com/watch?v=Rv9SwZWVkOs",
            "https://www.youtube.com/watch?v=IDPDEKtd2yM",
            "https://www.youtube.com/watch?v=t9fP_b8Ebow",
            "https://www.youtube.com/watch?v=Fo3e_0ITVjo",
            "https://www.youtube.com/watch?v=MdZAMSyn_As",
            "https://www.youtube.com/watch?v=g6TUZm5wzLs",
            "https://www.youtube.com/watch?v=xbagFzcyNiM",
            "https://www.youtube.com/watch?v=iPGd6l76l9A",
            "https://www.youtube.com/watch?v = mMYhgTgE6MU",
            "https://www.youtube.com/watch?v=BZ-LI68xS8g",
            "https://www.youtube.com/watch?v=bC0hlK7WGcM",
            "https://www.youtube.com/watch?v=TQMbvJNRpLE",
            "https://www.youtube.com/watch?v=9vJRopau0g0",
            "https://www.youtube.com/watch?v=9UotQ5T-f1o",
            "https://www.youtube.com/watch?v=_8sOFxZsNZM",
            "https://www.youtube.com/watch?v=Cp99EErJT-I",
            "https://www.youtube.com/watch?v=MJH0C1Owb6M",
            "https://www.youtube.com/watch?v=e5_61YEI5KI",
            "https://medium.com/mind-cafe/everything-you-need-to-know-about-depression-e1627c11810b",
            "https://medium.com/in-fitness-and-in-health/4-powerful-ways-to-increase-your-rem-sleep-6cbb067a459f",
            "https://medium.com/just-jordin/the-price-we-pay-to-fit-in-8d35aecb0d53",
            "https://medium.com/the-ascent/5-proven-strategies-to-self-manage-your-psychological-wellness-96941cf083ff"
        ]
    lnk = random.choice(res)
    return lnk

def respond():
    reprompts = ["Are you still there?",
    "Hello?",
    "Did you leave ?",
    "Did you still want me to check in on you ?",
    "Are you there ?"
    ]

    help_message = "Type 'yepp' if you are resuming..."
    #print ((random.choice(reprompts))+(help_message))

    return ((random.choice(reprompts))+(help_message))