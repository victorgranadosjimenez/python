
import array as arr
import random

class heroes():
    def  __init__(self, name):
        self.name = name

class fight():
    def __init__(self, winner):
        self.winner = winner

heroe1 = heroes("blanca")
heroe2 = heroes("guille")
heroe3 = heroes("honda")
heroe4 = heroes("riu")
heroe5 = heroes("ken")
heroe6 = heroes("mrbison")
heroe7 = heroes("vega")
heroe8 = heroes("sagat")
heroe9 = heroes("zangieff")

fight1 = fight = True

arr = ["riu", "zangieff", "mrbison", "ken","guille","blanca","sagat","honda", "vega"]

a = input("Player 1, Select hero: {} ".format(arr))
a=a.lower()

while len(arr)>=9:
    if a=="riu":
        arr.remove("riu")

    elif a=="zangieff":
        arr.remove("zangieff")

    elif a == "mrbison":
        arr.remove("mrbison")

    elif a == "ken":
        arr.remove("ken")

    elif a == "guille":
        arr.remove("guille")

    elif a == "blanca":
        arr.remove("blanca")

    elif a == "sagat":
        arr.remove("sagat")

    elif a == "honda":
        arr.remove("honda")

    elif a == "vega":
        arr.remove("vega")

    else:
        print("sorry I could not get that name, type  it again please")
        a=input("Player 1, Select hero: {} ".format(arr))


else:

        b = input("Player 2, Select hero: {}".format(arr))
        b=b.lower()
        while b not in arr:
            print("sorry I could not get that name, type  it again please")
            b = input("Player 2, Select hero: {} ".format(arr))
        else:
                fight1=[a,b]
                winner1 = random.choice(fight1)
                print(a + " vs " + b)
                print("the winner is {} !!!!".format(winner1))


