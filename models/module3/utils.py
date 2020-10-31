# This files contains all utility functions used in bot.py

import random
from senti import sentiment

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

        "Is it hard for you to do personal grooming ?",
        "Are you having thoughts of your own death ?",
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
            "Are you suffering from fever ?"
            ]

    s = str(input())
    print("Reply with Yes or no :) ")
    s = s.lower()
    if (s == "yes")
    # physical site direct
    else:
        depressionEnq()


def depressionEnq():
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
    ]


# a list of links to articles/videos/music/TED talks to cure depression
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
       "https://medium.com/the-ascent/5-proven-strategies-to-self-manage-your-psychological-wellness-96941cf083ff",
       

       ]