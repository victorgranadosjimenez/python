
import array as heroes
from typing import List

import random

heroes = ["riu", "zangieff", "mrbison", "ken","guille","blanca","sagat","honda", "vega"]

a = input("Player 1, Select hero: {} ".format(heroes))
a=a.lower()


while len(heroes)>=9:
    if a=="riu":
        heroes.remove("riu")

    elif a=="zangieff":
        heroes.remove("zangieff")

    elif a == "mrbison":
        heroes.remove("mrbison")

    elif a == "ken":
        heroes.remove("ken")

    elif a == "guille":
        heroes.remove("guille")

    elif a == "blanca":
        heroes.remove("blanca")

    elif a == "sagat":
        heroes.remove("sagat")

    elif a == "honda":
        heroes.remove("honda")

    elif a == "vega":
        heroes.remove("vega")

    else:
        print("sorry I could not get that name, type  it again please")
        a=input("Player 1, Select hero: {} ".format(heroes))


else:

        b = input("Player 2, Select hero: {}".format(heroes))
        b=b.lower()
        while b not in heroes:
            print("sorry I could not get that name, type  it again please")
            b = input("Player 2, Select hero: {} ".format(heroes))
        else:
                fight=[a,b]
                winner = random.choice(fight)
                print(a + " vs " + b)
                print("the winner is {} !!!!".format(winner))


